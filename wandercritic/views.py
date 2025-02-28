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
    context_dict = {}
    return render(request, 'wandercritic/index.html', context=context_dict)


def explore(request):
    context_dict = {}
    return render(request, 'wandercritic/explore.html', context=context_dict)