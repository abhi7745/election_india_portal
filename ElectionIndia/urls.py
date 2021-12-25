"""ElectionIndia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import Users_App.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Users_App.views.index,name='index_url'),

    path('signup/', Users_App.views.signup,name='signup_url'),
    path('login/', Users_App.views.loginpage,name='login_url'),

    # ////////////////////////////////////////////////////////////////////
    # Custom admin area
    path('admindashboard/', Users_App.views.admin_dashboard,name='admin_url'),

    # ///////////////////////////////////////////////////////////////////
    # ward manager area
    path('ward_manager/', Users_App.views.ward_manager,name='ward_manager_url'),
    path('manager_profile/', Users_App.views.ward_man_profile,name='manager_profile_url'),
    path('election_setter/', Users_App.views.election_setter,name='election_setter_url'),
    path('add_booth_member/', Users_App.views.add_booth_member,name='add_booth_member_url'),

    # ///////////////////////////////////////////////////////////////////
    # both member area
    path('booth_member/', Users_App.views.booth_member,name='booth_member_url'),
]
