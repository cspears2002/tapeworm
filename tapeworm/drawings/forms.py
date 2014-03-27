from django.forms import ModelForm
from django.contrib.auth.models import User
from drawings.models import Drawing

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'password')