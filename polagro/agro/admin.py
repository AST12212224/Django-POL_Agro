from django.contrib import admin
from .models import product, Contact
from embed_video.admin import AdminVideoMixin

admin.site.register(product)
admin.site.register(Contact)



