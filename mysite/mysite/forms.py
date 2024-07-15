"""from django import forms

class userForms(forms.Form):
    num1=forms.CharField(label="Value 1",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label="Value 2",widget=forms.TextInput(attrs={'class':"form-control"}))
    num3=forms.CharField(label="Value 3",widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField()"""
    
from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(label='Your Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Name *'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Email Address *'}))
    phone = forms.CharField(label='Phone', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Number *'}))
    referral = forms.CharField(label='Who should I thank for sending you my way?', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Who should I thank for sending you my way?'}))
    date = forms.DateField(label='Date', required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'style': 'height:60px', 'type': 'date'}))
    occassion = forms.CharField(label='Occasion', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Occasion'}))
    location = forms.CharField(label='Event Location', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Location'}))
    currency = forms.ChoiceField(label='Currency', choices=[('INR', 'INR'), ('USD', 'USD')], widget=forms.Select(attrs={'class': 'form-select', 'style': 'height:60px'}))
    budget = forms.CharField(label='Your Budget', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:60px', 'placeholder': 'Budget'}))
    comments = forms.CharField(label='Message, Questions?', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height:200px', 'rows': 3, 'placeholder': 'Message'}))
    