from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# from wandercritic.models import Category
# from wandercritic.models import Page
# from wandercritic.forms import CategoryForm
# from wandercritic.forms import PageForm
from django.shortcuts import redirect
from django.urls import reverse
from wandercritic.forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):

    context_dict = {}
    return render(request, 'wandercritic/index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # profile = profile_form.save(commit=False)
            # profile.user = user 

            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']

            # profile.save()

            registered = True
        else:
            print(user_form.errors)

    else: #if request is not 'POST', render blank forms: ready for user input
        user_form = UserForm()
        # profile_form = UserProfileForm()

    return render(request, 
                  'wandercritic/register.html', 
                  context = {'user_form': user_form,
                            # 'profile_form': profile_form,
                            'registered': registered})


def user_login(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user :
            if user.is_active :
                login(request, user)
                return redirect(reverse('wandercritic:index'))
            else :
                return HttpResponse("Your account is disabled.")
        else :
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else :
        return render(request, 'wandercritic/login.html')
    
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('wandercritic:index'))


def explore(request):
    context_dict = {}
    return render(request, 'wandercritic/explore.html', context=context_dict)