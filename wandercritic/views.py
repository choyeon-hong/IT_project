# from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# from wandercritic.forms import UserForm
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    return render(request, 'wandercritic/index.html')


def explore(request):
    return render(request, 'wandercritic/explore.html')


def about(request):
    return render(request, 'wandercritic/about.html')


def contact(request):
    return render(request, 'wandercritic/contact.html')


def become_agent(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'wandercritic/become_agent.html')


def report(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'wandercritic/report.html')


def policy(request, policy_type):
    # Map policy types to their template names
    policy_templates = {
        'review': 'review',
        'user': 'user',
        'travel-agent': 'travel-agent',
        'privacy': 'privacy',
    }
    
    if policy_type not in policy_templates:
        return redirect('wandercritic:index')
        
    template_name = policy_templates[policy_type]
    return render(request, f'wandercritic/policies/{template_name}.html')