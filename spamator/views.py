from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def checksms(request):
    sms=request.POST['smstext']
    messages.success(request,'0')
    return redirect('index')