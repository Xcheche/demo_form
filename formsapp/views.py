from django.shortcuts import render

from .forms import UserRegistrationForm

# Create your views here.


def user_registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            print("Form is valid")
            print("Username: ", form.cleaned_data["username"])
            print("Email: ", form.cleaned_data["email"])
            print("Password: ", form.cleaned_data["password"])
            print("Confirm Password: ", form.cleaned_data["confirm_password"])

    return render(request, "formsapp/user_registration.html", {"form": form})
