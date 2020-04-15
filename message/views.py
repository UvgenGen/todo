from django.views.generic.base import View
from django.shortcuts import render
from .forms import MessageForm
from .models import Message


class ToDoView(View):
    def get(self, request, *args, **kwargs):
        form = MessageForm()
        messages = Message.objects.all().order_by('-id')
        context = {
            'form': form,
            'messages': messages,
        }
        return render(request, 'message.html', context)
