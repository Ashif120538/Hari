from django.db import models

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'{self.sender}: {self.message}'