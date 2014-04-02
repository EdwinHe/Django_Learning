from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, unique = True)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    date_available = models.DateField()
        
class Cart(models.Model):
    total_price = models.DecimalField(max_digits = 8, decimal_places = 2, default = 0)
    
    SHOPPING = 'SP'
    DISCARDED = 'DC'
    CHECKEDOUT = 'CO'
    
    STATUS_CHOICS = (
        (SHOPPING, 'Shopping'),
        (DISCARDED, 'Discarded'),
        (CHECKEDOUT, 'CheckedOut'),
    )
    status = models.CharField(max_length=2,
                    choices=STATUS_CHOICS,
                    default=SHOPPING)
    
class LineItem(models.Model):
    cart = models.ForeignKey(Cart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    
    def add_to_cart(self):
        pass
    #unit_price = models.DecimalField(max_digits=8,decimal_places=2)
    
        
# class Cart(object):
#     def __init__(self, *args, **kwargs):
#         self.items = []
#         self.total_price = 0
#         
#     def add_product(self,product):
#         self.total_price += product.price
#         for item in self.items:
#             if item.product.id == product.id:
#                 item.quantity += 1 
#                 return
#         self.items.append(LineItem(product=product,unit_price=product.price,quantity=1))
        
    