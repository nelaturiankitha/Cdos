# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path
from .views import index, show

urlpatterns = [
    # /spence/
    path('', index, name='index'),
    # /spence/id e.g. /spence/1
    path('<int:item_id>/', show, name='show'),
]
