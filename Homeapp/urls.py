from django.contrib import admin
from django.urls import path, include
from .views import (home_view,
    student_view,
    libralian_view,
    std_login_view,
    std_signup_view,
    libralian_signup_view,
    libralian_login_view,
        )

app = "Homeapp"
urlpatterns = [ 

    path('Home/', home_view ,name = "home_url"),
    path('Home/student/', student_view ,name = "student_url"),
    path('Home/libralian/', libralian_view ,name = "libralian_url"),
    path('Home/student/std_login/', std_login_view ,name = "std_login_url"),
    path('Home/student/std_signup/', std_signup_view ,name = "std_signin_url"),
    path('Home/libralian/libralian_signup/', libralian_signup_view ,name = "libralian_signup_url"),
    path('Home/libralian/libralian_login/', libralian_login_view ,name = "libralian_login_url"),

]