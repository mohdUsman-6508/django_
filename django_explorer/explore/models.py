from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICE=[
    ('ML','MASALA'),
    ('GR','GINGER'),
    ('KL','KIWI'),
    ('PL','PLAIN')
  ]
  name=models.CharField(max_length=100)
  image=models.ImageField(upload_to="chais/")
  date_added=models.DateTimeField(default=timezone.now)
  type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
  description=models.TextField(default='')

  def __str__(self):
    return self.name


# One to Many

class ChaiReview(models.Model):
  RATING_CHOICE=[('1','1'),
                 ('2','2'),
                 ('3','3'),
                 ('4','4'),
                 ('5','5')]
  chai=models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name='reviews')
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  rating=models.TextField(max_length=2,choices=RATING_CHOICE)
  comment=models.TextField()
  date_added=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'{self.user.username} review for {self.chai.name}'
  

# Many to many

class Store(models.Model):
  name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  chai_varieties=models.ManyToManyField(ChaiVariety,related_name='stores')

  def __str__(self):
    return self.name
  

# One to one

class ChaiCertificate(models.Model):
  name =models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificate')
  certificate_number=models.DateTimeField(default=timezone.now)
  valid_until=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f'Certificate for {self.name.chai}'














