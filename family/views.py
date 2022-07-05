from re import search
from django.shortcuts import render, redirect, get_object_or_404
from .import urls
from .models import FamilyHead, FamilyMembers
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login_req')    
def index(request):
    head_count = FamilyHead.objects.all().count()
    init_count = 0
    for fam_head in FamilyHead.objects.all():
        init_count = init_count + fam_head.familymembers_set.filter(initiation='YES').count()
    
    search_input = request.GET.get('search-area')
    if search_input:
        or_lookup = (
            Q(full_name__icontains=search_input) | Q(family_code__icontains=search_input) | Q(address__icontains=search_input) |Q(email__icontains=search_input) | Q(phone_number__icontains=search_input)
        )
        head = FamilyHead.objects.filter(or_lookup)
    else:
        head = FamilyHead.objects.all()
        head = head.exclude(id = request.user.familyhead.id)
        search_input=''
    return render(request, 'index.html', {'head':head, 'search_input':search_input, 'head_count':head_count, 'init_count':init_count})
    
        
def loginReq(request):
    return render(request, 'login_req.html')

@login_required(login_url='/login_req')    
def userProfile(request):
    # familyhead = get_object_or_404(FamilyHead, id=pk)
    head_count = FamilyHead.objects.get(pk = request.user.id)
    init_count = head_count.familymembers_set.filter(initiation='YES').count()
    return render(request, 'user_profile.html', context={'init_count':init_count})

@login_required(login_url='/login_req')    
def updateFamilyMember(request, pk):
    # familyhead = get_object_or_404(FamilyHead, id=pk)
    member = request.user.familyhead.familymembers_set.get(id = pk)
    if request.method == 'POST':
        member.full_name =  request.POST['full_name']
        member.email = request.POST['email']
        member.phone_number = request.POST['phone_number']
        member.address = request.POST['address']
        member.relationship = request.POST['relationship']
        member.age = request.POST['age']
        member.initiation = request.POST['initiation']
        member.save()
        return redirect('/user_profile/')
    return render(request, 'update_family_member.html', {'member':member})


@login_required(login_url='/login_req')    
def addMember(request):
    if request.method =='POST':
        request.user.familyhead.familymembers_set.create(
            full_name =  request.POST['full_name'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            address = request.POST['address'],
            relationship = request.POST['relationship'],
            age = request.POST['age'],
            initiation = request.POST['initiation'],
        )
        return redirect('/user_profile/')
    return render(request, 'addFamilyMember.html')


@login_required(login_url='/login_req')    
def updateHead(request):
    if request.method =='POST':        
        request.user.familyhead.full_name =  request.POST['full_name']
        request.user.familyhead.email = request.POST['email']
        request.user.familyhead.phone_number = request.POST['phone_number']
        request.user.familyhead.address = request.POST['address']
        request.user.familyhead.ritwik = request.POST['ritwik']
        request.user.familyhead.date_of_init = request.POST['date_of_init']
        request.user.familyhead.save()
        return redirect('/user_profile/')

    return render(request, 'updatehead.html')


@login_required(login_url='/login_req')    
def deleteFamilyMember(request, pk):
    # familyhead = get_object_or_404(FamilyHead, id=pk)
    member = request.user.familyhead.familymembers_set.get(id = pk)
    if request.method == 'POST':
        member.delete()
        return redirect('/user_profile/')
    return render(request, 'delete_family_member.html', {'member' : member})


@login_required(login_url='/login_req')    
def viewProfile(request, pk):
    thatfamily = get_object_or_404(FamilyHead, id=pk)
    return render(request, 'view_profile.html', {'thatfamily' : thatfamily})