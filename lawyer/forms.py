from django import forms
from django.forms import ModelForm
from lawyer.models import UserDetail,Legal,BasicDetail,BarInfo

class UserDetailForm(ModelForm):
    CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), 
        required=True,
        max_length=75)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), 
        label="Confirm your password",
        required=True)
    
    birthday= forms.CharField(label=u'D.O.B',widget=forms.DateInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True)
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    mobile= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True)
    education= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=200,
        required=True)
    class Meta:
        model=UserDetail
        exclude=('user',)
        
class LegalInfoForm(ModelForm):
    court= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    state= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    office_address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    
    class Meta:
        model=Legal
        fields=['practice_areas','court','state','office_address']
        
class BasicDetailForm(ModelForm):
    experience= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    honours= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    publications= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    
    class Meta:
        model=BasicDetail
        fields=['summary','experience','honours','publications']  
        
        
class BarInfoForm(ModelForm):
    state= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    bar_id= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    year= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=100,
        required=True)
    
    class Meta:
        model=BarInfo
        fields=['state','bar_id','year','profile_pic']        
            
    
        