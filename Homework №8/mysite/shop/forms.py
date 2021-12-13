from django.forms import ModelForm, TextInput, Textarea

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "category", "product_image", "description"]
