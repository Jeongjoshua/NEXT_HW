from django.db import models
from django.utils import timezone

class SelectedDate(models.Model):
    selected_date = models.DateField()

def default_selected_date():
    return timezone.now() + timezone.timedelta(days=1)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    selected_date = models.DateField(default=default_selected_date)
    current_date = models.DateTimeField(default=timezone.now)

    def get_days_left(self):
        current_date = timezone.localtime(timezone.now()).date()
        difference = (self.selected_date - current_date).days

        if difference == 0:
            return "D-Day"
        elif difference > 0:
            return f"D-{difference}"
        else:
            return f"D+{abs(difference)}"

            
    def __str__(self):
        return self.title
