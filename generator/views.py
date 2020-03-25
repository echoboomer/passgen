from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
  return render(request, 'generator/home.html')

def password(request):
  # Establish base lowercase characters.
  characters = list('abcdefghijklmnopqrstuvwxyz')

  # Establish length passed in via request.
  length = int(request.GET.get('length'))

  # Establish the password that will be returned to the page.
  returned_password = ''

  # Establish additional character types if desired.
  if request.GET.get('uppercase'):
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

  if request.GET.get('special_characters'):
    characters.extend(list('!@#$%^&*()-=_+'))

  if request.GET.get('numbers'):
    characters.extend(list('1234567890'))

  # Loop for generating password.
  for _ in range(length):
    returned_password += random.choice(characters)
  
  return render(request, 'generator/password.html', {'password': returned_password})
