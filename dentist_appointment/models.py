from django.db import models
from django.utils import timezone
# from Dentalclinic.dentist_appointment.views import appointment, service
class Service(models.Model):
    service_name=models.CharField(max_length=35)
    service_image=models.ImageField(blank=True,upload_to='uploads/')
    created_at =  models.DateTimeField(default = timezone.now)
    def __str__ (self):
        return self.service_name

class Doctor(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  
    doctor_name=models.CharField(max_length=35)
    doctor_service=models.CharField(max_length=25)
    consultation_fee = models.DecimalField(max_digits=6, decimal_places=2)
    available_days=models.CharField(max_length=15)
    available_time=models.CharField(max_length=25)
    doctor_email=models.EmailField(max_length=50)
    doctor_image=models.ImageField(blank=True,upload_to='uploads/')
    created_at =  models.DateTimeField(default = timezone.now)


    def __str__ (self):
        return self.doctor_name


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=35)
    select_service=models.CharField(max_length=100, null=True) 
    select_doctor=models.CharField(max_length=100)
#     DAYS_OF_WEEK = (
#     (0, 'Monday'),
#     (1, 'Tuesday'),
#     (2, 'Wednesday'),
#     (3, 'Thursday'),
#     (4, 'Friday'),
#     (5, 'Saturday'),
#     (6, 'Sunday'),
# )

#     select_days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
#     select_date=models.DateField(max_length=15)
    patient_email=models.EmailField(max_length=50)
    # created_at =  models.DateTimeField(default = timezone.now)


    def __str__ (self):
        return self.doctor

  
class Testimonial(models.Model):
    user_name=models.CharField(max_length=35)
    reviews=models.TextField(max_length=1000)
    created_at =  models.DateTimeField(default = timezone.now)

    def __str__ (self):
        return self.user_name
