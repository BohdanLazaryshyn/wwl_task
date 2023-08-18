from django import forms

from producer.models import Employee


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password",
                                widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ('username', 'email', "position")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd["password2"]:
            raise forms.ValidationError("'Passwords don\'t match.'")
        return cd['password2']


class OrderSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name..."})
    )