from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Plant, Category
from .models import ContactMessage


admin.site.register(Plant)
admin.site.register(Category)  
admin.site.register(ContactMessage)
