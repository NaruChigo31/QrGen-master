"""qrgen URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from firstpages.views import *
from editor.views import *
from userpages.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", show_main, name = "main"),
    path("auth/", show_auth, name = "login"),
    path("reg/", show_reg, name = "reg"),
    path("editor/", show_editor, name = "editor"),
    path("profile/", show_profile, name="profile"),
    path("all-qr/",show_all_qr ,name="all-qr"),
    path("payment/", show_pay, name = "payment"),
    path("redirect/<qr_pk>",show_redirect_page, name = "redirect"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
