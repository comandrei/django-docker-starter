"""rocky URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from curs_manager.views import salut, studenti, contact, cursuri, curs, promoveaza_an, contact_2, add_curs, edit_curs, login, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("salut", salut),
    path("studenti", studenti),
    path("login", login),
    path("logout", logout_view),
    path("curs/<str:curs_nume>-<int:curs_id>", curs, name="detaliu-curs"),
    path("curs/<str:curs_nume>-<int:curs_id>/edit", edit_curs),
    path("cursuri", cursuri, name="lista-cursuri"),
    path("cursuri/adauga", add_curs),
    path("contact", contact),
    path("contact/", contact_2),
    path("promoveaza/<int:param_an>", promoveaza_an),
    path('__debug__/', include('debug_toolbar.urls')),
]
