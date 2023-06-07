from django import forms
from agenda.models import Task


    

class TaskModelForm(forms.ModelForm):
    class Meta:
         model = Task
         fields = '__all__'
         
def clean_descricao(self):
     descricao= self.cleaned_data.get('descricao')
     if descricao.lenght<50:
        self.add.error('descricao', 'o campo descrição precisa ter no mínimo 50 caracteres')
        return descricao
         
       
     