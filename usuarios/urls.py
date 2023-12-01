from django.urls import path, include
from .views import UserSignUpView, UserLoginView, UserEditView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(),name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('edit/', UserEditView.as_view(), name="edit"),
]