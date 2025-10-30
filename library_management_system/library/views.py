from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Member, Borrow
from .serializer import BookSerializer, MemberSerializer, BorrowSerializer
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

def dashboard(request):
    return render(request, 'dashboard.html')

def books_page(request):
    return render(request, 'books.html')

def members_page(request):
    return render(request, 'members.html')

def borrows_page(request):
    return render(request, 'borrows.html')