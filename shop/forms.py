from django import forms
from .models import PaymentInfo


class PaymentInfoForm(forms.ModelForm):

    class Meta:
        model = PaymentInfo
        fields = ("email", "first_name", "last_name", "address", "mobile_number", "city", "state", "zipcode", "discount")

