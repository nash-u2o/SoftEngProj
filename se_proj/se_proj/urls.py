"""se_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import edu_app.views as views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name="index"),
    path("assignments/<int:class_id>", views.assignments, name="assignments"),
    path("base/", views.base, name="base"),
    path("classpage/", views.classpage, name="classpage"),
    path("text/", views.text, name="text"),
    path("", views.login, name="login"),
    path("modules/", views.modules, name="modules"),
    path("home/", views.home, name="home"),
    path("info/<int:class_id>/", views.info, name="info"),
    path("test/", views.test, name="test"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("students/<int:class_id>", views.students, name="students"),
]
