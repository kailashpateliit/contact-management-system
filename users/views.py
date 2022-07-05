from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from family.models import FamilyHead
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            f_user = User.objects.get(username = username)
            print(f_user)
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/create_head/' + str(f_user.id))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def createHead(request, pk):
    if request.method =='POST':
        new = FamilyHead(
            family_user = User.objects.get(id = pk),
            full_name =  request.POST['full_name'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            address = request.POST['address'],
            birthday = request.POST['dob'],
            family_code = request.POST['family_code']
        )
        new.save()
        return redirect('/login/')
    return render(request, 'create_head.html')
