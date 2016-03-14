from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from lawyer.forms import UserDetailForm,LegalInfoForm,BasicDetailForm,BarInfoForm
from django.template import RequestContext
from django.contrib.auth import authenticate
from lawyer.models import UserDetail
def home(request):
    item=UserDetail.objects.all()
    return render_to_response('base.html', {'item':item})


def UserInfo(request):
    if request.method=='POST':
        form=UserDetailForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            gender=form.cleaned_data['gender']
            birthday=form.cleaned_data['birthday']
            mobile=form.cleaned_data['mobile']
            education=form.cleaned_data['education']
            user=authenticate(name=name,username=username,password=password,email=email,gender=gender,
            birthday=birthday,mobile=mobile,education=education)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form=UserDetailForm()
        return render_to_response('signup.html',{'form':form},context_instance=RequestContext(request))
    
    
def LegalInfo(request):
    if request.method=='POST':
        pass
    else:
        form=LegalInfoForm()
        return render_to_response('legal.html',{'form':form},context_instance=RequestContext(request))
    
    
    
def BasicInfo(request):
    if request.method=='POST':
        pass
    else:
        form=BasicDetailForm()
        return render_to_response('basic.html',{'form':form},context_instance=RequestContext(request))        

def BarInfo(request):
    if request.method=='POST':
        pass
    else:
        form=BarInfoForm()
        return render_to_response('bar2.html',{'form':form},context_instance=RequestContext(request))    

def Login(request):
    return render_to_response('login.html',{})