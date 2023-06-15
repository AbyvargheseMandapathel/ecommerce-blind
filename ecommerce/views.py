import pyttsx3
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login


User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User credentials are valid, log in the user
            auth_login(request, user)
            return redirect('login_success')
        else:
            # User credentials are invalid, show an error message or redirect to login page with error
            return render(request, 'login.html', {'error': 'Invalid credentials'})
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

def login_success(request):
    # Assuming you have retrieved the username from the logged-in user
    username = request.user.username
    
    # Render the template with the username in the context
    return render(request, 'login_success.html', {'username': username})
