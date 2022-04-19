from django.contrib import admin

from Accounts.models import UserExtension
from .models import Post

# Register your models here.

admin.site.register(Post)
admin.site.register(UserExtension)