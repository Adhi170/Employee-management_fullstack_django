from django import  forms
from employee_app.models import employee_models

class employee_forms(forms.ModelForm):
    class Meta:
        model=employee_models
        fields="__all__"
       

