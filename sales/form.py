from django import forms
from .models import *


class ShopForm(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('shop_name', 'contact', 'location', 'category', 'contact_person', 'branded', 'email', 'password', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'discount')


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('shop_name', 'image', 'offer_name', 'valid_from', 'valid_till', 'discount')


class ProductSearchForm(forms.Form):
    product_column = forms.CharField(max_length=222)
    keyword_product = forms.CharField(max_length=222)

