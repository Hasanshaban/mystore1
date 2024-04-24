"""
URL configuration for mystore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from clothes import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='home_view'),
    path('about/',views.about_view,name='about_view'),
    path('contact/',views.contact_view,name='contact_view'),
    path('products/',views.clothes_listview,name='clothes_listview'),
    path('single-product/',views.cloth_info_view,name='cloth_info_view'),
    path('products/<int:clothes_id>/',views.clothes_info,name='cloth_info'),
    path('order_list/',views.orderview,name='orderview'),
    path('signup/',views.signupview,name='signupview'),
    path('signin/',views.signinview,name='signinview'),
    path('logout/',views.user_logout,name='user_logout'),
    path('getorder/',views.get_order,name='get_order'),
    path('orderview/',views.orderview,name='orderview'),
    path('get_orderuser/',views.get_orderuser,name='get_orderuser'),
    path('my_user/',views.User_view,name='User_view'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)