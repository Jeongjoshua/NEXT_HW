from django.db import models
from django.utils import timezone
from pytz import timezone

# Create your models here.
class Category(models.TextChoices):
    HOBBY = 'hobby', 'Hobby'
    FOOD = 'food', 'Food'
    PROGRAMMING = 'programming', 'Programming'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.HOBBY,
    )
    published_date = models.DateTimeField(default=timezone('Asia/Seoul').localize)
                                        
    def __str__(self):
        return self.title