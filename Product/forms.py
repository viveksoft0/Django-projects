from django.forms import ModelForm, fields

from .models import Product



class ProductForm(ModelForm):

    """Form definition for MODELNAME."""
    

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Product
        fields = [
            'name',
            'weight',
            'price',
            
        ]
        