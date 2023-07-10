from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Video)
admin.site.register(Comments)
admin.site.register(VideoLinks)
admin.site.register(CommentLinks)
