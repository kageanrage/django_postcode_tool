from django.db import models

# Create your models here.


class PostcodeList(models.Model):
    title = models.CharField(default="", max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    def convert_to_csv(self):
        text_string = str(self.text)
        return text_string.replace('\r', ',').replace('\n', "")

