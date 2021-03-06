"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from webapp.views import homepage, google0a519d9b267460d1, sitemap
from resources.views import resources
from resources.views import orientation


urlpatterns = [
    path('', homepage),
    path('google0a519d9b267460d1.html/', google0a519d9b267460d1),
    path('sitemap.xml', sitemap),
    path('orientation/', orientation),
    path('resources/', resources),
    path('webapp/', include('webapp.urls')),
    path('resources/', include('resources.urls')),
    path('admin/', admin.site.urls),
]
