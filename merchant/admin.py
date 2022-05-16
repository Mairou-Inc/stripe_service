from django.contrib import admin
from merchant.models import *


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Item._meta.fields]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=[field.name for field in User._meta.fields if field.name not in ['password']]
    # list_id_fields=['comment', 'user', 'article']


# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display=[field.name for field in Article._meta.fields]
#     # filter_horizontal = ['comment']
#     list_id_fields=['user']
