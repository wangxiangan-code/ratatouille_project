from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def pageone_view(request):
    return render(request, 'pageone.html')

@login_required
def pagetwo_view(request):
    return render(request, 'pagetwo.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
