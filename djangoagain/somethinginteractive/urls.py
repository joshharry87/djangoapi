from django.urls import path

from . import views


app_name = "somethinginteractive"

urlpatterns = [
    path('', views.get_booking, name="booking")
]
