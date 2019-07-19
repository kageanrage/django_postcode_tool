from django.db import models

# Create your models here.


class PostcodeList(models.Model):
    title = models.CharField(default="", max_length=100)
    text = models.TextField()
    csv = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    def convert_to_csv(self):
        text_string = str(self.text)
        return text_string.replace('\r', ',').replace('\n', "")

    def count_of_postcodes(self):
        char_count = 0
        if self.convert_to_csv() == "":
            num_of_postcodes = 0
        elif self.convert_to_csv() == None:
            num_of_postcodes = 0
        else:
            for char in self.convert_to_csv():
                if char == ",":
                    char_count += 1
            num_of_postcodes = char_count + 1
        return num_of_postcodes

    def csv_preview(self):
        return self.convert_to_csv()[0:49]