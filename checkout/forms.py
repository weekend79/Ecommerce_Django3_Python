from django import forms
from .models import Order


# Payment Form
class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2023, 2039)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='CVV code', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


# Order form 

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'postaddress', 'street_address1', 'street_address2',
            'county'
        )
