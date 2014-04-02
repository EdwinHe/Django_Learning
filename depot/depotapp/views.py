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

def store_view(request):
    products = Product.objects.filter(date_available__lt=datetime.datetime.now().date()).order_by("-date_available")
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
            
    c = RequestContext(request,locals())        
    return HttpResponse(t.render(c))

