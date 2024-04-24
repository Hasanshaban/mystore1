from django.contrib import admin
from .models import Clothing,Color,Size,Order,ImageModel,Size_info

# Register your models here.
admin.site.register(Clothing)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(ImageModel)
admin.site.register(Size_info)

