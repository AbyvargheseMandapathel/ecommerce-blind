import pyttsx3
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Process the username and password and authenticate the user
        # Your login logic goes here
        
        return render(request, 'login_success.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Process the username and password and create a new user
        user = User.objects.create_user(username=username, password=password)
        
        # Text-to-speech
        engine = pyttsx3.init()
        engine.say("Account created successfully!")
        engine.runAndWait()
        
        return render(request, 'signup_success.html')
    else:
        return render(request, 'signup.html')
    
def signup_success(request):
    return render(request, 'signup_success.html')
