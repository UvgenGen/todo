from django.contrib import admin
from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'text_color': TextInput(attrs={'type': 'color'}),
            'bg_color': TextInput(attrs={'type': 'color'}),
        }


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
