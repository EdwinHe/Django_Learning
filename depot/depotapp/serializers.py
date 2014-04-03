from rest_framework import serializers
from depotapp.models import Cart, LineItem, Product

## WHOLE FILE FOR REST FRAMEWORK

class CartSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cart
		fields = ('total_price', 'status')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('title', 'description', 'image_url', 'price', 'date_available')

class LineItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LineItem
		fields = ('cart', 'product', 'quantity')
	
	# Nested Objects (foreign keys) need to set serializer explicitly 
	#cart = CartSerializer()
	#product = ProductSerializer()
	cart = serializers.PrimaryKeyRelatedField()
	product = serializers.PrimaryKeyRelatedField()
	quantity = serializers.IntegerField()




		