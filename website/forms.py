from django import forms
from .models import Contact, Booking
from phonenumbers import is_valid_number, is_possible_number
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError

# Create your forms here.

CONTACT_PLACE_HOLDERS = {
    "Name": "What is your name?",
    "Email": "What is your email address?",
    "Subject": "Subject",
    "Message": "Message",
}

BOOKING_PLACE_HOLDERS = {
    "Name": "Your name",
    "Email": "Your Email",
    "Phone": "Your Phone",
    "Date": "Date and Time of Check-In",
    "People": "# of People",
    "Message": "Message"
}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'Address': forms.Textarea(attrs={'rows': 5}),
            "Phone Number": PhoneNumberPrefixWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = CONTACT_PLACE_HOLDERS.get(field.label.title())


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'Address': forms.Textarea(attrs={'rows': 5}),
            "Phone Number": PhoneNumberPrefixWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = CONTACT_PLACE_HOLDERS.get(field.label.title())
