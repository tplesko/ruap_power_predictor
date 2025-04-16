from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    prediction_value = models.FloatField()
    advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction by {self.user.username} on {self.date_time}"
