from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=100)
    optimal_conditions = models.TextField()  # Describe optimal conditions
    fertilizer_recommendations = models.TextField()

    def str(self):
        return self.name