from django.contrib import admin
from .models import Article,Newsletter,Gallery,Comments,Videos,Spotlight
# Register your models here.
admin.site.register(Article)
admin.site.register(Newsletter)
admin.site.register(Gallery)
admin.site.register(Comments)

admin.site.register(Videos)
admin.site.register(Spotlight)