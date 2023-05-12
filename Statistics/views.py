from django.shortcuts import render


# Create your views here.
def take_input(request):
    return render(request, 'index.html')