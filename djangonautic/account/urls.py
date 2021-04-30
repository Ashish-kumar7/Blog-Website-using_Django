from django.urls import path , re_path
from . import views

app_name='account'

urlpatterns = [
    path('signup/',views.signup_veiw,name="signup"),
    path('login/',views.login_veiw,name="login"),
    path('logout/',views.logout_veiw,name="logout")
]