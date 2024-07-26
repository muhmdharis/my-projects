from django.contrib import admin
from .models import chat , exchange , product , verify , cart , order 
# Register your models here.
admin.site.register(chat)

admin.site.register(exchange)

admin.site.register(product)

admin.site.register(verify)

admin.site.register(cart)

admin.site.register(order)  