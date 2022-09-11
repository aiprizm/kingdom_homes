import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, BookingForm
from kingdom_homes.settings import EMAIL_HOST_USER

# Create your views here.


def index(request):
    contact_form = ContactForm()
    booking_form = BookingForm()
    context = {
        "contact_form": contact_form,
        "booking_form": booking_form
    }
    return render(request, 'website/index.html', context)


def inner_page(request):
    context = {}
    return render(request, 'website/sample-inner-page.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Kingdom Homes Inquiry"
            print(form.cleaned_data)
            body = {
                'Name': form.cleaned_data['name'],
                'Email': form.cleaned_data['email'],
                'Subject': form.cleaned_data['subject'],
                'Message': form.cleaned_data['message'],
            }
            email_header = "A new client is trying to contact you:"
            message = "\n".join([email_header] + [f"{key}: {value}" for key, value in body.items()])
            response = "Your message has been sent. Thank you!"
            try:
                send_mail(subject, message, body.get('email'), [EMAIL_HOST_USER])
            except BadHeaderError:
                response = "Bad Header Sent"
                return HttpResponse(response)
            return HttpResponse(response, status=200)
        else:
            response = {}
            return JsonResponse(response, status=403)
    else:
        form = ContactForm()
    return render(request, 'website/index.html', {'form': form})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Kingdom Homes Booking Request"
            print(form.cleaned_data)
            body = {
                    'Name': form.cleaned_data['name'],
                    'Email': form.cleaned_data['email'],
                    "Phone": form.cleaned_data['phone'],
                    "Date": form.cleaned_data['date'],
                    "People": form.cleaned_data['people'],
                    "Message": form.cleaned_data['message']
                }
            email_header = "A new client is trying to contact you:"
            message = "\n".join([email_header] + [f"{key}: {str(value)}" for key, value in body.items()])
            response = "Your message has been sent. Thank you!"
            try:
                send_mail(subject, message, body.get('email'), [EMAIL_HOST_USER])
            except BadHeaderError:
                response = "Bad Header Sent"
                return HttpResponse(response)
            return HttpResponse(response, status=200)
        else:
            response = {}
            return JsonResponse(response, status=403)
    else:
        form = ContactForm()
    return render(request, 'website/index.html', {'form': form})

# def about(request):
#     context = {}
#     return render(request, 'website/about.html', context)
#
#
# def privacy(request):
#     context = {}
#     return render(request, 'website/privacy-policy.html', context)
#
#
# def disclaimer(request):
#     context = {}
#     return render(request, 'website/disclaimer.html', context)
