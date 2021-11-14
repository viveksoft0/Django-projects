from typing import Text
from django.forms import fields
from django.shortcuts import render
from django.views.generic import ListView,UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from django.views import View
from .forms import ProductForm
from django.http import HttpResponseRedirect

# Create your views here.
# templateView, View

class ProductList(ListView):
    model = Product
    template_name = "Product/product_list.html"
    context_object_name = 'productlist'

    def get_queryset(self):
        queryset = Product.objects.using(alias='product_db').all()
        return queryset
    


# class ProductCreate(CreateView):
#     model = Product
#     template_name="Product/createview_form.html"
#     fields=['name','weight','price','created_at']
#     success_url=reverse_lazy('product')

class ProductCreate(View):
    form_class = ProductForm
    # initial = {'key': 'value'}
    template_name = 'Product/createview_form.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            print(form.data)
            Product.objects.using(alias='product_db').create(name=form.data["name"], weight=form.data["weight"], price=form.data["price"])
            return HttpResponseRedirect('/products')

        return render(request, self.template_name, {'form': form})

class Product_UpdateView(UpdateView):
    model = Product
    fields=['name','weight','price','updated_at']
    template_name = "Product/product_update_form.html"
    success_url=reverse_lazy('product')


class Delete_view(DeleteView):
    model=Product
    success_url=reverse_lazy('product')
