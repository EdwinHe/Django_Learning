from django import forms
from depotapp import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

