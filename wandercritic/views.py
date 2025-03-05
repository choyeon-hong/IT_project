from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Place, PlaceImage, TravelAgentApplication, Report
from .forms import PlaceForm, PlaceImageForm, TravelAgentApplicationForm

def is_superuser(user):
    return user.is_superuser

def index(request):
    return render(request, 'wandercritic/index.html')

def explore(request):
    places = Place.objects.all().order_by('-created_at')
    return render(request, 'wandercritic/explore.html', {'places': places})

def about(request):
    return render(request, 'wandercritic/about.html')

def contact(request):
    return render(request, 'wandercritic/contact.html')

@login_required
def become_agent(request):
    # If already a travel agent, redirect to place creation
    if request.user.is_travel_agent:
        messages.info(request, "You are already a travel agent!")
        return redirect('wandercritic:place_create')
    
    # Check for pending application
    pending_application = TravelAgentApplication.objects.filter(
        user=request.user,
        status='pending'
    ).first()
    
    if pending_application:
        return render(request, 'wandercritic/become_agent.html', {
            'pending_application': pending_application
        })
    
    if request.method == 'POST':
        form = TravelAgentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, 
                "Your application has been submitted successfully! We'll review it soon.")
            return redirect('wandercritic:become_agent')
    else:
        form = TravelAgentApplicationForm()
    
    return render(request, 'wandercritic/become_agent.html', {'form': form})

def report(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'wandercritic/report.html')

def policy(request, policy_type):
    template_name = f'wandercritic/policies/{policy_type}.html'
    return render(request, template_name)

def place_list(request):
    places = Place.objects.all().order_by('-created_at')
    return render(request, 'wandercritic/place_list.html', {'places': places})

def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)
    return render(request, 'wandercritic/place_detail.html', {'place': place})

@login_required
def place_create(request):
    if not request.user.is_travel_agent:
        messages.error(request, "Only travel agents can create new places.")
        return redirect('wandercritic:explore')
        
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.created_by = request.user
            place.save()
            form.save_m2m()  # Save many-to-many relationships
            
            # Handle additional images
            images = request.FILES.getlist('additional_images')
            for image in images:
                PlaceImage.objects.create(place=place, image=image)
                
            messages.success(request, f"{place.name} has been created successfully!")
            return redirect('wandercritic:place_detail', slug=place.slug)
    else:
        form = PlaceForm()
    
    return render(request, 'wandercritic/place_form.html', {'form': form})

@login_required
def place_edit(request, slug):
    place = get_object_or_404(Place, slug=slug)
    
    if not request.user.is_travel_agent and request.user != place.created_by:
        messages.error(request, "You don't have permission to edit this place.")
        return redirect('wandercritic:place_detail', slug=slug)
    
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            place = form.save()
            
            # Handle additional images
            images = request.FILES.getlist('additional_images')
            for image in images:
                PlaceImage.objects.create(place=place, image=image)
                
            messages.success(request, f"{place.name} has been updated successfully!")
            return redirect('wandercritic:place_detail', slug=place.slug)
    else:
        form = PlaceForm(instance=place)
    
    return render(request, 'wandercritic/place_form.html', {'form': form})

@user_passes_test(is_superuser)
def admin_applications(request):
    applications = TravelAgentApplication.objects.filter(status='pending')
    return render(request, 'wandercritic/admin/applications.html', {
        'applications': applications
    })

@user_passes_test(is_superuser)
def admin_application_action(request, application_id, action):
    application = get_object_or_404(TravelAgentApplication, id=application_id)
    
    if action == 'approve':
        application.approve()
        messages.success(request, f"Application by {application.full_name} has been approved.")
    elif action == 'reject':
        application.reject()
        messages.success(request, f"Application by {application.full_name} has been rejected.")
    
    return redirect('wandercritic:admin_applications')

@user_passes_test(is_superuser)
def admin_reports(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'wandercritic/admin/reports.html', {
        'reports': reports
    })

@user_passes_test(is_superuser)
def admin_report_action(request, report_id, action):
    report = get_object_or_404(Report, id=report_id)
    
    if action == 'resolve':
        report.resolve(request.user)
        messages.success(request, f"Report on {report.place.name} has been resolved.")
    elif action == 'dismiss':
        report.dismiss(request.user)
        messages.success(request, f"Report on {report.place.name} has been dismissed.")
    
    return redirect('wandercritic:admin_reports')