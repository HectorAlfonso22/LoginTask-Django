from django import forms


class TaskCreationForm(forms.Form):
    title = forms.CharField(label='Título', max_length=255)  
    content = forms.CharField(label='Contenido', widget=forms.Textarea())  
