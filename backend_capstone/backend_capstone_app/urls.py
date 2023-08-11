from django.urls import path
from . import views
urlpatterns = [
    path('menu-items/',views.BookingListCreate.as_view()),
]