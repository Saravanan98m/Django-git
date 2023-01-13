from django.shortcuts import render
from django.http import HttpResponse
from.models import staff

# Create your views here.
def portion(request):
    s = staff.objects.all()
    return render(request, 'index.html', {'s': s})
    #return HttpResponse("<h1>Welcome To School<h1>")
