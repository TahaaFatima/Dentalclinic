import email
from django.shortcuts import render, get_object_or_404
from . models import Service,Doctor, Patient,Testimonial
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    testimonial_data = Testimonial.objects.all()
    context = {
       'testimonial_info' :  testimonial_data
    }    
    
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def appointment(request,user_data_id):
    user_data = Doctor.objects.get( pk=user_data_id)
    user_data_service = Service.objects.filter(doctor=user_data_id)

    context = {
       'user_data_info' :  user_data,
    }
   
        

    return render(request,"appointment.html",context)


def price(request):
    return render(request,"price.html")

# def contact(request):
#     return render(request,"contact.html")    

def service(request):
    service_data = Service.objects.all()
    context = {
       'service_info' :  service_data
    }
    return render(request,"service.html",context)
    

def doctorchoices(request,doctor_choice_id):
    doctor_choice_data =Service.objects.get( pk=doctor_choice_id)
    doctor_choice_in_data=Doctor.objects.filter(service=doctor_choice_data)
    context = {
       'doctor_choice_info'        :    doctor_choice_data,
       'doctor_choice_in_data_info':    doctor_choice_in_data
    }
    return render(request,"doctorchoices.html",context)


def doctorDetails(request,detail_id):
    detail_data = get_object_or_404(Doctor, pk=detail_id)
    context = {
       'single_doctor_info' :  detail_data
    }
    return render(request, 'doctordetails.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Subject:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['subject'])
        send_mail('You got a mail!', message, '', ['hashmihumna57@gmail.com']) # TODO: enter your email address
        
    return render(request, 'contact.html',)


def save_data(request):
    if request.method=="POST":
        service = request.POST.get('service')
        doctor = request.POST.get('doctor')
        name=request.POST.get('name')
        email=request.POST.get('email')
        form_data = {
            'name':name,
            'email':email,
            'service':service,
            'doctor':doctor,
        }
        message = '''
        From:\n\t\t{}\n
        Service:\n\t\t{}\n
        Doctor:\n\t\t{}\n
        Email:\n\t\t{}\n
        '''.format(form_data['name'], form_data['service'], form_data['doctor'],form_data['email'])
        send_mail('You got a mail!', message, '', ['hashmihumna57@gmail.com'])  
    return render(request, 'submit.html',)