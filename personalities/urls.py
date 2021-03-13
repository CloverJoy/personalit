from django.urls import path
from . import views
# personalities/
# personalities/1
urlpatterns = [
    path('', views.index, name='index')
]
