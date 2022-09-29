from django.contrib import admin
from .models import Service,Doctor,Patient,Testimonial

# Register your models here.
admin.site.register(Service)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Testimonial)
