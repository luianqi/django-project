from .models import Info
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'surname', 'story', 'date']

        # widgets = {
        #     'name': TextInput(attrs= {
        #         'class': 'form-control',
        #         'placeholder': 'First Name',
                
        #     }),
        #     'surname': TextInput(attrs= {
        #         'class': 'form-control',
        #         'placeholder': 'Last Name',
              
        #     }),
        #     'story': Textarea(attrs= {
        #         'class': 'form-control',
        #         'placeholder': 'Write Your Story',
         
        #     }),
        #     'date': DateTimeInput(attrs= {
        #         'class': 'form-control',
        #         'placeholder': 'Date',
         
    
        #     })
        # }