from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LoginForm
from .models import User

def nuclear(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            query = "SELECT * FROM nuclear_user WHERE USERNAME='{0}' AND PASSWORD='{1}';".format(
                username, password)
            a = list(User.objects.raw(query));
            
            if a:
                a = a[0]

            context = {
                "form": LoginForm(),
                "user": a,
                "sent_form": True
            }
            return render(request, 'nuclear/nuclear.html', context)
    else:
        form = LoginForm()
        context = {
            "form": form,
            "user": False,
            "sent_form": False
        }
        return render(request, "nuclear/nuclear.html", context)