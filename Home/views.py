from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from Home.models import *
from django.contrib import messages
from django.apps import apps

# Create your views here.


def home(request):
    if request.method == 'POST':
        farmerName = request.POST.get('username')
        tractorName = request.POST.get('tractorName')
        harrow = request.POST.get('Harrow')
        cultivator = request.POST.get('Cultivator')
        rotavator = request.POST.get('Rotavator')
        plough = request.POST.get('Plough')
        paddy_thrasher = request.POST.get('Paddy_Thrasher')
        dumping_trailer = request.POST.get('Dumping_Trailer')
        wheel_trailer = request.POST.get('4_wheel_Trailer')

        if farmerName =='' or tractorName == '':
            return redirect('/')
        else:
            # checking if the username is already taken or not
            if Farmer.objects.filter(username=farmerName).exists():
                messages.success(request, 'Name is already taken!')
                return redirect('/')
            else:
                name = farmerName.split(' ')
                if len(name) > 1:
                    messages.success(request, 'Username should not contain spaces!')
                    return redirect('/')
                farmer = Farmer(username=farmerName, tractorName=tractorName)
                farmer.save()
                implement = Implement(owner=farmer, harrow=harrow, cultivator=cultivator, rotavator=rotavator, plough=plough,
                                    paddy_thrasher=paddy_thrasher, dumping_trailer=dumping_trailer, wheel_trailer=wheel_trailer)
                implement.save()

                messages.success(request, 'Submitted!')
                return render(request, 'home.html')

    return render(request, 'home.html')


def tractorsList(request):
    FarmersData = Farmer.objects.all()
    return render(request, 'tractorsList.html', {'FarmersData':FarmersData})


def farmerpage(request):
    url = request.get_full_path()
    url = url.split('=')
    username = url[1]
    implement = Implement.objects.all()
    for user in implement:
        if str(user) == username:
            context = {
                'username':username,
                'tractorName':user.owner.tractorName,
                'user':user
            }
            return render(request, 'farmerpage.html', context)
    else:
        messages.success(request, "User does not exist!")