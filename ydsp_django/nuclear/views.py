from django.shortcuts import render

def nuclear(request):
    return render(request, "nuclear/nuclear.html", {})