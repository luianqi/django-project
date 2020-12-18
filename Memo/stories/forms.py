from .models import Info
from django.forms import ModelForm


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'surname', 'story', 'date']