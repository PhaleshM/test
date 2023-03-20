from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Listing(models.Model):

    class ListObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(availibility=True)
        
    name = models.CharField(max_length=50, blank=False)
    productchoices={
        ("Tractor","Tractor"),
        ("Plough","Plough"),
        ("Cultivator","Cultivator"),
        ("Rotavator","Rotavator"),
        ("Trailer","Trailer"),
        ("Baler","Baler"),
        ("Seed Drill","Seed_Drill"),
        ("Sprayer","Sprayer"),
        ("Harvester","Harvester"),
    }
    ratechoices={
        ('H',"per hour"),
        ('D',"per day"),
        ('K',"per Km"),
    }
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product=models.CharField(choices=productchoices, max_length=50)
    description=models.TextField()
    ratecriteria=models.CharField(choices=ratechoices,max_length=1)
    rate=models.IntegerField()
    slug = models.CharField(max_length=80, blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    availibility=models.BooleanField(default=True)
    objects = models.Manager()  # default manager
    listsobjects = ListObjects()  # custom manager
    def save(self, *args, **kwargs):
        urlslug=str(self.name)+str(self.user)
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s" % (self.name)
    
    class ListObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(availibility=True)
    
class ListingImage(models.Model):
    name = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to="products")


    def __str__(self):
        return "%s" % (self.name.name)
