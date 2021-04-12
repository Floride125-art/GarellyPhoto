from django.shortcuts import render
from imagegarelly.models import imggal

def imagedisplay(request):
    resultsdisplay= imggal.objects.all()
    return render(request, 'index.html', {'imggal':resultsdisplay})
