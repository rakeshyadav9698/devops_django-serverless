from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.GetProductList.as_view(), name='item-list'),
    path('add', views.AddProduct.as_view(), name='create'),
    path('delete', views.DeleteProduct.as_view(), name='delete'),
]