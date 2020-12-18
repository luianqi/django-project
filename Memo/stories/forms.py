from .models import Info
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'surname', 'story', 'date']

        widgets = {
            'name': TextInput(attrs= {
                'class': 'input__field',
                'placeholder': ''
            }),
            'surname': TextInput(attrs= {
                'class': 'input__field',
                'placeholder': ''
            }),
            'story': Textarea(attrs= {
                'class': 'input__field',
                'placeholder': ''
            }),
            'date': DateTimeInput(attrs= {
                'class': 'input__field',
                'placeholder': ''
    
            })
        }