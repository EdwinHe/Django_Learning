from django import forms
from depotapp import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        

    def clean_price(self):
        price = self.cleaned_data['price']
        if price<=0:
            raise forms.ValidationError("Price must be greater than zero")
        return price
    
    def clean_image_url(self):
        url = self.cleaned_data['image_url']
        if not url.endswith(('.jpg', '.png', '.gif')):
            raise forms.ValidationError('Image format must be jpg, png or gif')
        return url