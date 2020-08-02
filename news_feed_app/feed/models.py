from django.db import models 

# A model to represent a news category such as Sports and Science.
# A user is able to filter their news feed.
class Category(models.Model):
    name = models.CharField(max_length=200) 
    selected = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
