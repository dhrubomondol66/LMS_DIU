from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet, MemberViewSet, BorrowViewSet,
    dashboard, books_page, members_page, borrows_page
)

# ---------------------------
# API Router
# ---------------------------
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrows', BorrowViewSet)

# ---------------------------
# Frontend Pages
# ---------------------------
frontend_urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('books-page/', books_page, name='books'),
    path('members-page/', members_page, name='members'),
    path('borrows-page/', borrows_page, name='borrows'),
]

# ---------------------------
# Combine URLs
# ---------------------------
urlpatterns = [
    path('', include(router.urls)),   # API routes under /api/
] + frontend_urlpatterns
