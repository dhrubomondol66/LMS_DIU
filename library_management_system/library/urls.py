from django.urls import path, include
from .views import (
    dashboard, books_page, members_page, borrows_page,
    register_user, login_user, logout_user,
    BookViewSet, MemberViewSet, BorrowViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrows', BorrowViewSet)

urlpatterns = [
    # Frontend pages
    path('dashboard/', dashboard, name='dashboard'),
    path('books-page/', books_page, name='books'),
    path('members-page/', members_page, name='members'),
    path('borrows-page/', borrows_page, name='borrows'),

    # Auth
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # API
    path('', include(router.urls)),
]
