from .models import Post
from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(myresume)
admin.site.register(Contact)
admin.site.register(newsletter)
admin.site.register(Project)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('created_on',)

