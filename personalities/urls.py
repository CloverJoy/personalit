from django.urls import path
from . import views
# personalities/
# personalities/1
app_name = 'personality'

urlpatterns = [
    path('', views.index, name='index'),
    path('<personality_mbtitype>', views.detail, name='detail')
]
