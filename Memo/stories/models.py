from django.db import models


class Info(models.Model):
    name = models.CharField('First Name', max_length=15)
    surname = models.CharField('Last Name', max_length=15)
    story = models.TextField('Story')
    date = models.DateField('Date')

    def __str__(self):
        return self.name
