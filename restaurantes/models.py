from django.db import models
# Create your models here.


class Comments(models.Model):
    restaurant_name = models.CharField(max_length=200, null=True)
    comment = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.comment


class Restaurant(models.Model):
    owner = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    fund_date = models.DateField(
        blank=True, null=True)
    comments = models.ForeignKey(Comments, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
