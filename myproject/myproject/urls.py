from django.contrib import admin
from django.urls import path
from calendar_app import views as calendar_views
from user_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', calendar_views.show_date, name='calendar'),
    path('user/', user_views.show_user_info, name='user'),
]
