from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


LANG_TYPE_CHOICES = [
    ('COMPILED', 'Compiled Language'),
    ('INTERPRETED', 'Interpreted Language'),
    ('SYSTEM', 'System Programming Language'),
]

RATING_CHOICES = [
    ('1','ONE STAR'),
    ('2','TWO STAR'),
    ('3','THREE STAR'),
    ('4','FOUR STAR'),
    ('5','FIVE STAR')
    
]


class Lang(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField('')
    logo = models.ImageField(upload_to='langs/')
    date_added = models.DateTimeField(default=timezone.now)
    lang_type = models.CharField(max_length=20, choices=LANG_TYPE_CHOICES)

    def __str__(self):
        return self.name
    
#one to many
class Review(models.Model):
    lang = models.ForeignKey(Lang,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=50,choices=RATING_CHOICES)
    comment = models.TextField('')
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.lang.name}'
  

# many to many
class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    langs = models.ManyToManyField(Lang,related_name="langs")
    adapted_date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return self.name
    
    
# one to one
class Engine(models.Model):
    name = models.CharField(max_length=50)
    lang = models.OneToOneField(Lang,related_name='lang_engine',on_delete=models.CASCADE)
    launched_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name