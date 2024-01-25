"""MaryCakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core import views as core_views
from productos.views import *
from productos import views as productos_views
from user.views import *
from user.forms import *
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('contact/', core_views.contact, name="contact"),
    path('register/', register.as_view(), name="register"),
    path('postre/', productos_views.postre, name="postre"),
    path('torta/', productos_views.torta, name="torta"),
    path('torta/<slug>/', detailTor.as_view(), name="torta-detail"),
    path('postre/<slug>/', detailPost.as_view(), name="postre-detail"),
    path('compra/<slug>/', detailCart.as_view(), name="detailcart"),
    path('compra2/<slug>/', detailCart2.as_view(), name="detailcart2"),
   path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name = 'user/login.html',authentication_form=loginForm) , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
