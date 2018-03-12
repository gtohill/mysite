from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from django.template import loader
from resources.models import Register
from resources.forms import RegistrationForm
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("<h2>Hey World</h2>")


def parents(request):
    template = loader.get_template('webapp/parents.html')
    return HttpResponse(template.render())


def courses(request):
    template = loader.get_template('webapp/courses.html')
    return HttpResponse(template.render())


def contact(request):
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

    return render(request, 'webapp/contact.html', {'form': form})



def beginner(request):
    template = loader.get_template('webapp/beginner.html')
    return HttpResponse(template.render())


def novice(request):
    template = loader.get_template('webapp/novice.html')
    return HttpResponse(template.render())


def intermediate(request):
    template = loader.get_template('webapp/intermediate.html')
    return HttpResponse(template.render())


def rasppi(request):
    template = loader.get_template('webapp/rasppi.html')
    return HttpResponse(template.render())


def webdesign(request):
    template = loader.get_template('webapp/webdesign.html')
    return HttpResponse(template.render())


def homepage(request):
    user = User.objects.get(pk=1)
    output = "User Name is "+str(user)
    template = loader.get_template('webapp/homepage.html')

    context = {
        'output': output,
    }
    return HttpResponse(template.render(context, request))
