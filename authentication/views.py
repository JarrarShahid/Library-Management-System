from django.shortcuts import render

import json
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            with open('authentication/users.json', 'r') as f:
                users = json.load(f)
        except Exception as e:
            messages.error(request, "Error reading user database.")
            return redirect('custom_login')

        for user in users:
            if user['username'] == username and user['password'] == password:
                request.session['username'] = username
                messages.success(request, "Login successful.")
                return redirect('booksPreview')  # Change to your home page URL name

        messages.error(request, "Invalid username or password.")
        return redirect('custom_login')

    return render(request, 'login.html')


def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('custom_login')
