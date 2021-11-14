from django.forms import fields
from django.shortcuts import render
from django.views.generic import ListView,UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = "Product/product_list.html"
    context_object_name = 'productlist'
    


class ProductCreate(CreateView):
    model = Product
    template_name="Product/createview_form.html"
    fields=['name','weight','price','created_at']
    success_url=reverse_lazy('product')


class Product_UpdateView(UpdateView):
    model = Product
    fields=['name','weight','price','updated_at']
    template_name = "Product/product_update_form.html"
    success_url=reverse_lazy('product')


class Delete_view(DeleteView):
    model=Product
    success_url=reverse_lazy('product')
