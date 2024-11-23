Rest API

	1. pip install djangorestframework
	2. # myproject/settings.py 
	INSTALLED_APPS = [
	'rest_framework', 
	]
	3. 
	from django.db import models
	
	class Item(models.Model):
	    name = models.CharField(max_length=100)
	    description = models.TextField()
	
	    def __str__(self):
	        return self.name
	4. python manage.py makemigrations
	python manage.py migrate
	5. Create serializers.py on app
	
	from rest_framework import serializers
	from .models import Item
	
	class ItemSerializer(serializers.ModelSerializer):
	    class Meta:
	        model = Item
	        fields = ['id', 'name', 'description']
	6. Go to views

	from django.shortcuts import render
	from .models import Item
	from rest_framework.decorators import api_view
	from rest_framework.response import Response
	from .serializers import ItemSerializer
	# Create your views here.
	
	@api_view(['POST'])
	def add_name(request):
	    itemserializer = ItemSerializer(data = request.data)
	    if itemserializer.is_valid():
	        itemserializer.save()
	        return Response(itemserializer.data)
	    else:
	        return Response(itemserializer.errors)
	
	@api_view(['GET'])
	def get_name(request):
	    name_obj = Item.objects.all()
	    serializer = ItemSerializer(name_obj,many = True)
	    return Response(serializer.data)   
	 
	@api_view(['PUT'])
	def update_name(request,name_id):
	    try:
	        name_obj = Item.objects.get(id = name_id)
	        itemserializer = ItemSerializer(instance = name_obj,data = request.data,partial = True)
	        if itemserializer.is_valid():
	            itemserializer.save()
	            return Response(itemserializer.data)
	        else:
	            return Response(itemserializer.errors)
	    except Item.DoesNotExist:
	        return Resoponse('Name not exist')
	
	@api_view(['DELETE'])
	def delete_book(request,id):
	    try:
	        name_obj = Item.objects.get(id=id)
	        name_obj.delete()
	        return Response('Name deleted successfully')
	    except Item.DoesNotExist:
	        return Response({'message':'Name not found'})
	7.  Go to app urls.py
	
	from django.urls import path
	from Adminapp import views 
	urlpatterns = [
	    path('items/', views.add_name, name='item-list'),
	    path('list/items/', views.get_name, name='item-detail'),
	    path('update/<int:name_id>/', views.update_name, name='update-name'),
	    path('delete/<int:id>/', views.delete_book, name='delete-book'),
	]

	8. Go to project url.py
	path('api/', include('Adminapp.urls')),
	
	9. py manage.py runserver
go to thunderclient extension
