from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.
CATEGORY_CHOICES = (
    ('seed','SEED AND PLANT'),
    ('fertilizers', 'FERTILIZERS'),
    ('traps','TRAPS'),
    ('pesticides','PESTICIDES'),
)
class product(models.Model):
    product_name = models.CharField(max_length = 50)
    product_image = models.ImageField(upload_to='upload/')
    video = EmbedVideoField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='green')
    product_describe = models.TextField()
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

