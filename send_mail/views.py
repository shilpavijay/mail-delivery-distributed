from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.
def sendMail(request):
    return render(request,'send_mail.html')