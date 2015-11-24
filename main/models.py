from django.db import models
from django.contrib.auth.models import User

class Contest(models.Model):
    contest_name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.contest_name
