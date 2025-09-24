from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to="customer_logo")
  
    def __str__(self):
        return self.name


class DemoRequest(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    



class Features(models.Model):
    
    image = models.ImageField(upload_to="features/image")
    icon = models.FileField(upload_to="features/icon")
    icon_background = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=128)
    author_designation = models.CharField(max_length=128)
    testimonial_logo = models.FileField(upload_to="features/logo")
  
    def __str__(self):
        return self.title
    


class Reviews(models.Model):
    
    image = models.ImageField(upload_to="reviews/image")
    testimonial_logo = models.FileField(upload_to="reviews/logo")
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=128,default="#")
  
    def __str__(self):
        return self.title
    


class Testimonials(models.Model):
    
    image = models.ImageField(upload_to="testimonials/image")
    testimonial_logo = models.FileField(upload_to="testimonials/logo")
    title = models.CharField(max_length=128)
    testimonial_name = models.CharField(max_length=128)
    author_job = models.CharField(max_length=128)
    author_designation = models.CharField(max_length=128)
  
  
    def __str__(self):
        return self.testimonial_name
    
class midFeatures(models.Model):
    
    image = models.FileField(upload_to="midfeatures/image")
    title = models.CharField(max_length=128)
    description = models.TextField()
    link = models.CharField(default="#", max_length=256)

  
    def __str__(self):
        return self.title
    
class Products(models.Model):
    
    logo = models.FileField(upload_to="products/logo")
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to="products/image")
    bg_color = models.CharField(max_length=128)
    
    
  
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    
    image = models.ImageField(upload_to="blog/image")
    blog_type = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    link = models.CharField(default="#", max_length=256)
    # bg_color = models.CharField(max_length=128)
    
    
  
    def __str__(self):
        return self.title
    

