from django.contrib.auth.models import User
from django import forms


#For Adding and Compare User information using this Class
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')


#For Adding Question require a format on form which follow following labels which also set
#in activeuser_ques.html
class ActiveQuesForm(forms.Form):
    question_text = forms.CharField(label ='Enter question',)
    choice_1= forms.CharField(label ='Choice 1')
    choice_2= forms.CharField(label ='Choice 2')
    choice_3= forms.CharField(label ='Choice 3')
