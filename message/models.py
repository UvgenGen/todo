from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):

    text = models.TextField()
    text_color = models.CharField(max_length=7, default='#FF0000')
    bg_color = models.CharField(max_length=7, default='#FF0000')

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})
