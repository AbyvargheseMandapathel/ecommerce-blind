import pyttsx3
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import Product
from django.http import JsonResponse
from django.db.models import Q



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
            # Text-to-speech
            engine = pyttsx3.init()
            engine.say(f"{username} successfully logged in.")
            engine.runAndWait()
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            # Text-to-speech
            engine = pyttsx3.init()
            engine.say(f"Invalid Credentials")
            engine.runAndWait()
            # User credentials are invalid, show an error message and redirect to login page with error
            messages.error(request, 'Invalid credentials')
            return redirect('login')  # Replace 'login' with the URL name of your login page
    else:
        # Clear any existing error messages
        storage = get_messages(request)
        storage.used = True
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

        return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        return render(request, 'signup.html')

def signup_success(request):
    return redirect('home')

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})

def home(request):
    username = request.user.username

    # Retrieve products from the database
    products = Product.objects.all()

    context = {
        'username': username,
        'products': products,
    }

    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    return redirect('login')  # Replace 'login' with the URL name of your login page

def search_products(query):
    # Perform the search query on the Product model
    # You can customize the search logic based on your needs
    # This example searches for products whose name or description contains the query
    results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    # Process the search results or format them as needed
    # For example, you can serialize the results to JSON or extract specific fields
    
    # Return the processed results
    return results

def process_voice_input(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        # Perform the search based on the query
        # Retrieve matching products from the database
        # Process the search results as needed
        results = search_products(query)
        # Return the results as a JSON response
        return JsonResponse(results, safe=False)
    
    
