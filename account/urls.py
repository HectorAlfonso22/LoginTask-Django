from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup/', views.UserCreateAndLoginView.as_view(), name='signup'),
    
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='account/login.html'
    ), name='login'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('detail_user/<int:pk>/', views.UserDetail.as_view(), name='detail_user'),
    
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='edit_user'),
    
    path('change_password/', views.PasswordChange.as_view(), name='change_password'),
    
    path('delete_user/<int:pk>/', views.UserDelete.as_view(), name='delete_user'),
]
