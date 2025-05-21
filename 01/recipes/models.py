from django.db import models

class Recipe(models.Model):
    # 在这里添加你的字段
    title = models.CharField(max_length=200)
    description = models.TextField()

# class Ingredient(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50)  # 肉類、蔬菜、海鮮、其他

    def __str__(self):
        return self.name
   #回傳食譜名稱，方便後台辨識
