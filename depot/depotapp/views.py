# Step 1
from django.shortcuts import render
from django.http import HttpResponse

# Step 2
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from depotapp.forms import ProductForm
from depotapp.models import Product, Cart, LineItem

# Step 4
import datetime
from django.core import serializers

# Step 7 FOR REST FRAMEWORK 
from rest_framework import viewsets
from rest_framework import serializers
from depotapp.serializers import CartSerializer, LineItemSerializer, ProductSerializer

from django.db.models import Q

# Step 10
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# Step 1
def depotapp_test(request):
    return HttpResponse('Welcome to depotapp!')

# Step 2
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    t = get_template('depotapp/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

@login_required
def list_product(request):
    list_items = Product.objects.all()
    paginator = Paginator(list_items ,10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('depotapp/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def view_product(request, id):
    product_instance = Product.objects.get(id = id)

    t=get_template('depotapp/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request, id):

    product_instance = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance = product_instance)

    if form.is_valid():
        form.save()

    t=get_template('depotapp/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

#@login_required
def store_view(request):
    
    products = Product.objects.filter(date_available__lt=datetime.datetime.now().date()).order_by("-date_available")
    
    # Step 8
    # === Step 10 ===
    #import pdb;pdb.set_trace()
    if request.user.is_authenticated():
        try:
            cart = Cart.objects.get(user = request.user.id)
        except:
            cart = Cart.objects.create(user = request.user, total_price = 0.00, status = Cart.SHOPPING) 
            
        cart_id = cart.id
        
    else:
        cart_id = 0
    
    # ===============
    
    if cart_id == 0:
        cart = None
        lineitems = None
    else:
        cart = Cart.objects.get(id = cart_id)
        lineitems = LineItem.objects.filter(cart__exact = cart_id)
    
    t = get_template('depotapp/store.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def view_cart(request, id):
    ## MODEL CHANGE
    
    #item1 = LineItem(product = Product.objects.get(pk=1), unit_price = 30, quantity = 1)
    #item2 = LineItem(product = Product.objects.get(pk=2), unit_price = 40, quantity = 1)
    
    #cart = Cart()
    #cart.items=[item1,item2]
    #cart.total_price = 100
    
    #import pdb; pdb.set_trace()
    #cart = request.session.get("cart", None)
    a_cart = Cart.objects.get(id = id)
    list_items = LineItem.objects.filter(cart__exact = id)
    t = get_template('depotapp/view_cart.html')
            
    c = RequestContext(request,{"a_cart": a_cart, "list_items": list_items})        
    return HttpResponse(t.render(c))

def add_to_cart(request, id):
      # Original Code
#     product = Product.objects.get(id = id)
#     cart = request.session.get("cart",None)
#     if not cart:
#         cart = Cart()
#         request.session["cart"] = cart
#     cart.add_product(product)
#     request.session['cart'] = cart
#     return view_cart(request)

    cart_id = 1 #Hard-code for now, it will be linked to customer who logged in.
    product = Product.objects.get(id = id)
    cart = Cart.objects.get(id__exact = cart_id)
    items_in_cart = LineItem.objects.filter(cart__exact = cart_id)
    
    # If any item in cart is the same product we are adding to cart
    # Change the quantity, otherwise, new LineItem add.
    cart.total_price += product.price
    cart.save()
    for item in items_in_cart:
        if item.product.id == int(id):
            item.quantity += 1
            item.save()
            break
    else:
        LineItem.objects.create(cart = cart, product = product, quantity = 1)

    return view_cart(request, cart_id)


def clean_cart(request, id):
# # Original Code
# def clean_cart(request):  
#     request.session['cart'] = Cart()  
#     return view_cart(request)  

    LineItem.objects.filter(cart__exact = id).delete()
    cart = Cart.objects.get(id__exact = id)
    cart.total_price = 0
    cart.status = Cart.SHOPPING
    cart.save()

    return HttpResponseRedirect(reverse('depotapp:store_view'))





def view_cart_serialize(request):
    
#def view_cart(request):
#     cart = request.session.get("cart",None)
#     t = get_template('depotapp/view_cart.html')
# 
#     if not cart:
#         cart = Cart()
#         request.session["cart"] = cart
#             
#     c = RequestContext(request,locals())  #{'cart': cart}      
#     return HttpResponse(t.render(c))
    
    t = get_template('depotapp/view_cart_serialize.html')
    
    list_items = LineItem.objects.all()
    list_items_ser = serializers.serialize('json', list_items)
    request.session["list_items_ser"] = list_items_ser
        
    c = RequestContext(request,{'list_items':list_items})        
    return HttpResponse(t.render(c)) #content_type="application/json"


## Step 7. FOR REST FRAMEWORK
class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class LineItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    model = LineItem
    #queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer
    
    def get_queryset(self):
        #import pdb;pdb.set_trace()
        # Ideally, cart is linked with user and user is retrieved by self.request.user
        queryset = LineItem.objects.all()
          
        cartid = self.request.QUERY_PARAMS.get('cartid', None)
        productid = self.request.QUERY_PARAMS.get('productid', None)
        
        if cartid and productid:
            queryset = LineItem.objects.filter(Q(cart__exact = cartid) & Q(product__exact = productid))
        elif cartid:
            queryset = LineItem.objects.filter(cart__exact = cartid)
        elif productid:
            queryset = LineItem.objects.filter(cart__exact = productid)
        
        return queryset
    
    
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
def login_view(request):
    #import pdb;pdb.set_trace()
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #return store_view(request)
                return HttpResponseRedirect(reverse('depotapp:store_view'))
            else:
                return HttpResponse("Account Disabled!")
        else:
            return HttpResponse("Login Failed!")
    except:
        return HttpResponseRedirect(reverse('depotapp:store_view'))
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('depotapp:store_view'))

