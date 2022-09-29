from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('appointment/<int:user_data_id>', views.appointment,name='appointment'),
    path('contact/', views.contact,name='contact'),
    path('price/', views.price,name='price'),
    path('service/', views.service, name='service'),
    path('service/<int:doctor_choice_id>', views.doctorchoices, name='doctorchoices'),
    path('doctorchoices/', views.doctorchoices,name='doctorchoices'),
    path('doctorchoices/<int:detail_id>', views.doctorDetails, name='details'),
    path('save_data/', views.save_data,name='submit'),
    # path('submit/', views.submit,name='submit'),
]
