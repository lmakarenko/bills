from django.db import models
from django.utils import timezone

class counter_type(models.Model):
    #author = models.ForeignKey('auth.User')
    #title = models.CharField(max_length=200)
    #text = models.TextField()
    #created_date = models.DateTimeField(
    #        default=timezone.now)
    #published_date = models.DateTimeField(
    #        blank=True, null=True)
    name = models.CharField(max_length=64)
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class counter(models.Model):
    counter_type = models.ForeignKey(
        'counter_type',
        on_delete=models.SET_NULL,
	null=True
    )
    num = models.DecimalField(
        max_digits=10,
	decimal_places=0
    )
    name = models.CharField(
        max_length=64
    )
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class counter_data(models.Model):
    counter = models.ForeignKey(
        'counter',
        on_delete=models.CASCADE
    )
    data = models.DecimalField(
        max_digits=12,
	decimal_places=0
    )
    reg_date = models.DateTimeField(
        default=timezone.now
    )
    def publish(self):
        self.save()

    def __str__(self):
        return str(self.reg_date) + ': ' + str(self.data)

