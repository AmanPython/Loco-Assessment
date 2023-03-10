"""loco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from transaction.views import TransactionViews

# router = routers.DefaultRouter()
# router.register(r'transactionservice', TransactionViews, basename="transactionservice")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('transactionservice', include('rest_framework.urls', namespace='transactionservice'))
# ]


from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactionservice/',include('transaction.urls')),
    path(r'swagger-docs/', schema_view)
]