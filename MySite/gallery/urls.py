from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    #path('navigator/<int:navigator_id/>', get_navigator),


]