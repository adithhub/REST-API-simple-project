from django.urls import path
from Adminapp import views 

urlpatterns = [
    path('items/', views.add_name, name='item-list'),
    path('list/items/', views.get_name, name='item-detail'),
    path('update/<int:name_id>/', views.update_name, name='update-name'),
    path('delete/<int:id>/', views.delete_book, name='delete-book'),
]