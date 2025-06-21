from django.urls import path
from .views import*

urlpatterns = [
          path('login/',LoginView.as_view(),name="login"),
          path('signup/', Registerationform.as_view(),name="signup"),
          path('signup-form/',RegisterView.as_view(),name='signupSubmit'),
    
]