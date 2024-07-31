from django import forms
from django.core.validators import RegexValidator # inbuilt validator regex
from django.core.validators import MinLengthValidator # inbuilt validator min length



class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'Male'), ('female', 'Female')]
    username = forms.CharField(label="Username", max_length=20,required=False)
    full_name = forms.CharField(label="Full Name", max_length=30)
    email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput)
    nickname = forms.CharField(
        label="Nickname", 
        max_length=10,
        validators=[
            RegexValidator( # inbuilt regex validator
                regex='^[a-zA-Z]*$', 
                message='Nickname must contain only alphabetic characters',
                code='invalid_nickname'
            )
        ]
    )
    maiden_name = forms.CharField(
        label="Maiden Name", 
        max_length=20,  # This sets the maximum length
        validators=[MinLengthValidator(5)]  # This sets the minimum length if needed inbuilt validator
    )

    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(
        label="Password",
        help_text="Must be at least 8 characters long",
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )
    ssn=forms.IntegerField()
    
    # Added validation for
""" None single validation for fullname
def clean_full_name(self):
        inputfullname = self.cleaned_data['full_name']
        if len(inputfullname) > 30:
            raise forms.ValidationError("Full name cannot be more than 30 characters")
        return 
    
    
"""
    
#*****Single validation for all fields*****
""" Single validation for all fields
# validation for username
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username == "admin":
            raise forms.ValidationError("Username cannot be 'admin'")
        return cleaned_data

    # Added validation for password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    # Added validation for email
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if "@" not in email:
            raise forms.ValidationError("Email must contain '@'")
        return cleaned_data
"""