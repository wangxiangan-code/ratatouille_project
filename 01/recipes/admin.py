from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)  # 👈 註冊 Recipe 模型進後台
