from django.shortcuts import render


def home(request):
    return render(request, 'page1/page1.html')
