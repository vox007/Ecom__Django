from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)

    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username
