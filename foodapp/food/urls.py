from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexClassView.as_view(),name="index"),
    path('<int:pk>/',views.detailClassBasedView.as_view(),name='detail'),
    path('add/',views.CreateItem.as_view(),name='create_item'),
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),


]
