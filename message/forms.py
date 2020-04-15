from django.forms import ModelForm
from django.forms.widgets import TextInput


from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('text', 'text_color', 'bg_color',)
        widgets = {
            'text_color': TextInput(attrs={'type': 'color'}),
            'bg_color': TextInput(attrs={'type': 'color'}),
        }
