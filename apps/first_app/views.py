from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

# def index(request):
#     context = {
#         "somekey":"somevalue"
#     }
#     return render(request, 'index.html', context)

# def index(request):
#     context = {
#     "time": strftime("%y-%m-%d %H:%M %p", gmtime())     # string format time
#     }
#     return render(request, 'index.html',context)



def index(request):
    context = {
    "time": strftime('%b %d, % %Y %I:%M%p',gmtime())     # string parse time
    }
    return render(request, 'index.html',context)
