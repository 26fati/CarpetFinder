from django.db import models
from django.db import models
from django.contrib.auth.models import User
from carpet.models import Carpet

class Conversation(models.Model):
    carpet = models.ForeignKey(Carpet, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


class ConversationMessage(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)