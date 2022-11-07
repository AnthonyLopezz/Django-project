from StoreApp.models import Product, CategoryProd
from django import forms


class FormProduct(forms.ModelForm):
    name = forms.CharField(label="Name", required=True, max_length=25,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Description", required=True, max_length=500,
                                  widget=forms.Textarea(attrs={'class': 'form-control'}))
    size = forms.CharField(label="Size", required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(label="Type", required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label="Price", required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = {'name',
                  'category',
                  'image',
                  'description',
                  'size',
                  'type',
                  'price'}
