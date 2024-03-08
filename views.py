from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = UserForm()

    return render(request, 'accounts/register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            # You can add login logic here
            return redirect('home')
        except User.DoesNotExist:
            pass

    return render(request, 'accounts/signin.html')
