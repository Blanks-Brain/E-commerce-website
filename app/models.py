from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

STATE_CHOICES=(
    ('Mirpur1', 'Mirpur1'),
    ('Mirpur2', 'Mirpur2'),
    ('Mirpur6', 'Mirpur6'),
    ('Mirpur10', 'Mirpur10'),
    ('Mirpur11', 'Mirpur11'),
    ('Mirpur11.5', 'Mirpur11.5'),
    ('Mirpur12', 'Mirpur12'),
    ('Mirpur13', 'Mirpur13'),
    ('Mirpur14', 'Mirpur14'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=150)
    locality = models.CharField(max_length = 200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length=80)
    
    def __str__(self):
        return str(self.id)

BRAND_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('E', 'Earphone'),
    ('Ta', 'Tab'),
    ('Ot','Other'),

)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length = 100)
    category = models.CharField(max_length=2,choices = BRAND_CHOICES)
    image = models.ImageField(upload_to='productimg')
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id) 
    
    @property
    def total_price(self):
        return self.quantity * self.product.selling_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50,choices =STATUS_CHOICES, default ="Pending" )
    
    def __str__(self):
        return str(self.id)

