from rest_framework import serializers
from depotapp.models import Cart, LineItem, Product

## WHOLE FILE FOR REST FRAMEWORK

class CartSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cart
		fields = ('id', 'user', 'total_price', 'status') # Step 10 Add 'user'
		
	# Step 10
	user = serializers.PrimaryKeyRelatedField()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'title', 'description', 'image_url', 'price', 'date_available')

class LineItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LineItem
		fields = ('id', 'cart', 'product', 'quantity')
	
	# **Nested Objects (foreign keys) need to set serializer explicitly
	# cart = CartSerializer()
	# product = ProductSerializer()
	# **Or use serializers.PrimaryKeyRelatedField() to present them as primary key (id)
	
	#id = serializers.Field()   # Found this redundant in Step 10
	cart = serializers.PrimaryKeyRelatedField()
	product = serializers.PrimaryKeyRelatedField()
	#quantity = serializers.IntegerField()   # Found this redundant in Step 10




		