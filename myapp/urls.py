from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('home/',views.home),
    path('reg-std/', views.regStudent),
    path('update-std/', views.updateStudent),
    path('delete-std/', views.delStudent),
    path('get-std/', views.getStudents),
]
