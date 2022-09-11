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
    "Book Name": "Your name",
    "Book Email": "Your Email",
    "Book Phone": "Your Phone",
    "Book Date": "Date of Check-In (YYYY-MM-DD)",
    "Book Time": "Time of Check-In (HH:MM:SS)",
    "Book N People": "# of People",
    "Book Subject": "Subject",
    "Book Message": "Message"
}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            'rows': 5
        })
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = CONTACT_PLACE_HOLDERS.get(field.label.title())


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'Book Date': forms.DateInput(format='%Y-%m-%d', attrs={"type": "datetime-local"}),
            'Book Time': forms.DateInput(format='%H:%M:%S', attrs={"type": "datetime-local"}),
            "Phone Number": PhoneNumberPrefixWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = BOOKING_PLACE_HOLDERS.get(field.label.title())
