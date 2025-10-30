from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Book, Member, Borrow
from .serializer import BookSerializer, MemberSerializer, BorrowSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def books_page(request):
    return render(request, 'books.html')

def members_page(request):
    return render(request, 'members.html')

def borrows_page(request):
    return render(request, 'borrows.html')

