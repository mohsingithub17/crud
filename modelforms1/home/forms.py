from .models import Emp
from django.forms import ModelForm
class EmpForm(ModelForm):
    class Meta:
        model=Emp
        fields="__all__"