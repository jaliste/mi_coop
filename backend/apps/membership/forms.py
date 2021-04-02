from django import forms
from .models import CoopMember, ContactInfo
from kale_coop.users.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args,**kwargs)
        self.fields['email'].disabled = True

class MemberForm(forms.ModelForm):

    class Meta:
        model = CoopMember
        fields = ['national_id','birthdate','nationality','gender','civil_status','occupation']

class AcceptConditionsForm(forms.ModelForm):
    class Meta:
        model = CoopMember
        fields = ['contact_by_email','reasons_to_apply','referral']

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone_number','have_whatsapp','phone_is_whatsapp','whatsapp_number','join_whatsapp_group']

class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


