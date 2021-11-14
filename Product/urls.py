from django import urls
from django.urls import path
from .views import ProductList,ProductCreate,Product_UpdateView,Delete_view

urlpatterns = [
    path('products/',ProductList.as_view(),name='product'),
    path('create/',ProductCreate.as_view(),name='create'),
    path('product/<int:pk>/',Product_UpdateView.as_view(),name='update'),
    path('<pk>/delete/',Delete_view.as_view(),name='delete'),
    
]