from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, commit=True):
        our_user = super().save(commit=False)
        if commit:
            our_user.save()
            UserAccount.objects.create(user=our_user)
            return our_user


class DespositForm(forms.Form):
    amount = forms.IntegerField()

    def clean_amount(self):
        min_deposit = 100
        amount = self.cleaned_data["amount"]
        if amount < min_deposit:
            raise forms.ValidationError(
                f'Minimum deposit amount $100'
            )
        return amount
