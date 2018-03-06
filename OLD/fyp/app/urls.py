from django.conf.urls import url, include
from app.views import *


urlpatterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
]
