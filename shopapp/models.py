from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    product_pic = models.ImageField(upload_to = 'posts/')
    description = models.TextField(max_length=255)
    price =models.IntegerField()

    def __str__(self):
        return self.name
    
    # def create_product(self):
    #     self.save()
        
    # def delete_product(self):
    #     self.delete()
    
    @classmethod
    def get_product_by_id(cls,id):
        product = cls.objects.filter(id= id).all()
        return product
    @classmethod
    def search_by_name(cls, search_term):
        product = cls.objects.filter(name__icontains=search_term)
        return product
 
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.TextField(max_length=240, null=True)
    location = models.CharField(max_length=255, null=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,  blank=False, related_name='products')
    
    def __str__(self):
        return self.user
    
    def create_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['posted_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()