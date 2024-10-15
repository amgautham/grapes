from django.urls import path,include
from . import views
urlpatterns = [

    path('create/',views.add_form,name="create"),
    path('show/',views.show_table,name="show"),
    path('update/<int:pk>/',views.update_table,name="update"),
    path('delete/<int:pk>/',views.delete_table,name="delete"),
]