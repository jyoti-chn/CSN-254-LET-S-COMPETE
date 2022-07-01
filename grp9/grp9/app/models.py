from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)


    def _str_(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('H','Hackathons'),
    ('C','Courses'),
    ('I','Internships'),
    ('S','Scholarships'),
    ('CE','CulEvents'),

)
class Product(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField()
    mini_description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to="productimg")
    eligibility = models.TextField()
    dateofevent = models.DateTimeField()


    def _str_(self):
        return str(self.id)


class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES =(
    ('Registered','Registered'),
    ('Pending','Pending'),
)


class EventRegistered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

