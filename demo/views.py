from django.shortcuts import render
# Create your views here.

def home(request):
    return render (request,'home.html')
def chat(request):
    return render (request,'chat.html')
def setting(request):
    return render (request,'setting.html')
def notification(request):
    return render (request,'notification.html')
