from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def checksms(request):
    sms=request.POST['smstext']
    result=sms
    if result == '1':  #Ham
        messages.success(request, '0')
    else:            #Spam
        messages.warning(request, '0')
    return redirect('index')