from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Todo(models.Model):
    title = models.CharField(_('title'), max_length=220)
    body = models.TextField(_('body'))
    
    