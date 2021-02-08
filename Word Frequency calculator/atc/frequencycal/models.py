from django.db import models

class Word_cal(models.Model):
    url_l = models.URLField(help_text="Enter usl of site")

    words = models.TextField()

    count = models.IntegerField()

    class Meta:
        ordering = ['url_l','-count']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.url_l} , {self.words} , {self.count}'



