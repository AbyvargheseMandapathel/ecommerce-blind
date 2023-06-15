import speech_recognition as sr
import pyttsx3
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def login(request):
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        command = r.recognize_google(audio)
        
        # Process the recognized command and authenticate the user
        # Your login logic goes here
        
        return render(request, 'login_success.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        command = r.recognize_google(audio)
        
        # Process the recognized command and create a new user
        User.objects.create_user(username=command, password='password')
        
        # Text-to-speech
        engine = pyttsx3.init()
        engine.say("Account created successfully!")
        engine.runAndWait()
        
        return render(request, 'signup_success.html')
    else:
        return render(request, 'signup.html')
