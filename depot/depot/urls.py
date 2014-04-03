from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

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
    # url(r'^admin/', include(admin.site.urls)),   
    url(r'^depotapp/', include('depotapp.urls', namespace = 'depotapp')),
    
    # REST Framework
    url(r'^API/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

