from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True) # blank=True - не обязательно для заполнения для поля Текст
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True) # null=True - не обязательно для заполнения для поля даты
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title