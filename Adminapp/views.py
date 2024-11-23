from django.shortcuts import render  # Import render function, but it's not used here.
from .models import Item  # Import the Item model to interact with the database.
from rest_framework.decorators import api_view  # Import the api_view decorator to specify which HTTP methods a view should handle.
from rest_framework.response import Response  # Import the Response class to send data back in HTTP responses.
from .serializers import ItemSerializer  # Import the ItemSerializer to convert the model data to/from JSON.

# Create your views here.

# View to handle POST requests and add a new item.
@api_view(['POST'])  # Only allows POST requests for this view.
def add_name(request):  # Define the function to handle the incoming request.
    itemserializer = ItemSerializer(data=request.data)  # Initialize the serializer with the data from the request (request.data).
    
    if itemserializer.is_valid():  # Check if the provided data is valid according to the serializer's validation rules.
        itemserializer.save()  # If the data is valid, save the new Item to the database.
        return Response(itemserializer.data)  # Return the serialized data of the newly created Item.
    else:
        return Response(itemserializer.errors)  # If the data is invalid, return the validation errors.

# View to handle GET requests and fetch all items.
@api_view(['GET'])  # Only allows GET requests for this view.
def get_name(request):  # Define the function to handle the incoming request.
    name_obj = Item.objects.all()  # Retrieve all Item objects from the database.
    serializer = ItemSerializer(name_obj, many=True)  # Serialize the queryset (many=True indicates multiple objects).
    return Response(serializer.data)  # Return the serialized data as a JSON response.

# View to handle PUT requests and update an existing item.
@api_view(['PUT'])  # Only allows PUT requests for this view (typically used for updating data).
def update_name(request, name_id):  # The function takes 'name_id' from the URL to identify the item.
    try:
        name_obj = Item.objects.get(id=name_id)  # Try to get the Item with the given 'name_id'.
        itemserializer = ItemSerializer(instance=name_obj, data=request.data, partial=True)  # Initialize the serializer with existing data ('instance') and new data ('data').
        if itemserializer.is_valid():  # Check if the data is valid.
            itemserializer.save()  # Save the updated data to the database.
            return Response(itemserializer.data)  # Return the updated item data.
        else:
            return Response(itemserializer.errors)  # If the data is invalid, return validation errors.
    except Item.DoesNotExist:  # If no item with the given 'name_id' exists in the database.
        return Response('Name not exist')  # Return a response indicating the item was not found.

# View to handle DELETE requests and delete an existing item.
@api_view(['DELETE'])  # Only allows DELETE requests for this view.
def delete_book(request, id):  # The function takes 'id' from the URL to identify the item.
    try:
        name_obj = Item.objects.get(id=id)  # Try to get the Item with the given 'id'.
        name_obj.delete()  # If the item exists, delete it from the database.
        return Response('Name deleted successfully')  # Return a success message indicating the item was deleted.
    except Item.DoesNotExist:  # If no item with the given 'id' exists in the database.
        return Response({'message': 'Name not found'})  # Return a response indicating the item was not found.
