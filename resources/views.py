from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrationForm, OrientationForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import Register
from os import *
# Create your views here.


def resources(request):
    template = loader.get_template('resources/resources.html')
    return HttpResponse(template.render())


def london(request):
    template = loader.get_template('resources/london.html')
    return HttpResponse(template.render())


def mississauga(request):
    template = loader.get_template('resources/mississauga.html')
    return HttpResponse(template.render())


def waterloo(request):
    template = loader.get_template('resources/waterloo.html')
    return HttpResponse(template.render())


def faq(request):
    template = loader.get_template('resources/faq.html')
    return HttpResponse(template.render())


def registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            sender = form.cleaned_data['email']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            location = form.cleaned_data['location']
            status = form.cleaned_data['status']
            age = form.cleaned_data['age']
            question = form.cleaned_data['questions']
            cc_myself = form.cleaned_data['cc_myself']

            item = Register(name=name, phone=phone, email=sender, age=age, location=location, status=status, question=question)
            item.save()

            recipients = ['kreateinkode@gmail.com', sender]
            if cc_myself:
                recipients.append(sender)

            subject = 'Inquiry - Course Registration'
            message = 'Name: ' + name + '\n' + 'Phone: ' + phone + '\n' + 'Location: ' + location + '\n'\
            + 'Status: ' + status + '\n' + 'Age: ' + age + '\n' \
            + 'Question: ' + question

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('../../resources/thank_you/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'resources/registration.html', {'form': form})


def thank_you(request):
    template = loader.get_template('resources/thank_you.html')
    return HttpResponse(template.render())


def orientation(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrientationForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            sender = form.cleaned_data['email']
            name = form.cleaned_data['name']
            questions = form.cleaned_data['questions']
            confirmed = form.cleaned_data['confirm']
            # save information
            """
            item = Register(name=name, phone=phone, email=sender, age=age, location=location, status=status, question=question)
            item.save()
            """
            recipients = ['kreateinkode@gmail.com', sender]
            """
            if cc_myself:
                recipients.append(sender)
            """
            subject = 'Register - Summer Camp Orientation'
            message = 'Name: ' + name + '\n' + 'Question: ' + questions

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('../../resources/thank_you/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrientationForm()
        return render(request, 'resources/orientation.html', {'form': form})


