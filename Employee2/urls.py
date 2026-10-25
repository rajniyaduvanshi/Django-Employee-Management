
from django.contrib import admin
from django.urls import path
from App2 import views

urlpatterns = [
    path('', views.display, name='home'),
    path('admin/', admin.site.urls),

    path('empdata/', views.display, name='empdata'),
    path('addEmp/', views.addEmp, name='addEmp'),
    path('editdata/<int:id>/', views.editdata, name='editdata'),
    path('deletedata/<int:id>/', views.deletedata, name='deletedata'),

    path('department/', views.department, name='department'),
    path('department/delete/<int:id>/', views.delete_department, name='delete_department'),

    path('company/', views.company, name='company'),
    path('company/edit/<int:id>/', views.edit_company, name='edit_company'),
    path('company/delete/<int:id>/', views.delete_company, name='delete_company'),
]
