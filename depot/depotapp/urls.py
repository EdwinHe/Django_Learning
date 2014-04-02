from django.conf.urls import patterns, include, url
from depotapp import views

urlpatterns = patterns('',
    # Step 1
    url(r'^$', views.depotapp_test, name = 'depotapp'),

    # Step 2
    url(r'product/create/$', views.create_product, name = 'create'),  
    url(r'product/list/$', views.list_product, name = 'list'),  
    url(r'product/edit/(?P<id>[^/]+)/$', views.edit_product, name = 'edit'),  
    url(r'product/view/(?P<id>[^/]+)/$', views.view_product, name = 'view'), 
    
    # Step 4
    url(r'store/$', views.store_view, name = 'store'),  
    url(r'cart/view/(?P<id>[^/]+)/$', views.view_cart, name = 'cart'),
)
