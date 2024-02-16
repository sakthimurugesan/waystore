from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')]
    profile_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'required': True, 'class': 'form-check-label'}),
        choices=GENDER_CHOICES
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "Email"}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "First Name"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "Last Name"}))
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'required': True, 'class': 'form-control', 'type': 'date'}),
        help_text='Please enter your date of birth in the format YYYY-MM-DD.'
    )
    door_no = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "Door No"}))
    street_name = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "Street"}))
    city = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "City"}))
    district = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "District"}))
    pincode = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "Pincode",}))
    state = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control', 'placeholder': "State"}))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'required': True, 'class': "form-control", 'style': 'resize: none;', 'cols': "70","rows":"5"}))
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={"required": True, 'class': 'form-control','type':"password", 'placeholder': "Password"}))
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={"required": True, 'class': 'form-control', 'type': "password", 'placeholder': "Repeat password"}))



    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    class Meta:
        model = CustomUser
        fields = (
        'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'door_no', 'street_name', 'city', 'district',
        'address', 'pincode', 'state','profile_photo')


class CustomUserChangeForm(UserChangeForm):
    
    profile_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = (
        'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'door_no', 'street_name', 'city', 'district',
        'address', 'pincode', 'state','profile_photo')
