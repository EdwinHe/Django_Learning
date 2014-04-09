from django.conf.urls import patterns, include, url

from django.contrib import admin # Step 9
admin.autodiscover()

# REST Framework
from rest_framework import routers
from depotapp import views

router = routers.DefaultRouter() 
router.register('cart', views.CartViewSet)
router.register('lineitem', views.LineItemViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'depot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),   
    url(r'^depotapp/', include('depotapp.urls', namespace = 'depotapp')),
    
    # REST Framework
    url(r'^API/', include(router.urls)),
    
    # Admin Step 9
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/',  include(admin.site.urls)), # admin site
    
    # Auth - Step 10
    url(r'^accounts/login/$', views.login_view, name = 'login'),
    url(r'^accounts/logout/$', views.logout_view, name = 'logout'),
)

