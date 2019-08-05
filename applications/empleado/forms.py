from django import forms  
from applications.empleado.models import Employee  

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"

    def clean_eemail(self):
        email = self.cleaned_data.get("eemail")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        #if not "hotmail" in dominio:
        #    raise forms.ValidationError("Por favor utilizar un email con dominio hotmail")
        return email