from .models import Info
from django.forms import ModelForm, DateField, Textarea, CharField


class InfoForm(ModelForm):
    name = CharField()
    surname = CharField()
    story = Textarea()
    date = DateField()
    class Meta:
        model = Info
        fields = ['name', 'surname', 'story', 'date']

# text = forms.CharField(
#         widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))