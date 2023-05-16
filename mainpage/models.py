from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Games(models.Model):
    game_name = models.CharField(max_length = 20)
    game_photo = models.ImageField(upload_to = 'media')
    game_info = models.TextField()
    game_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.game_name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

class TournirsCategory(models.Model):
    category_tournirs = models.CharField(max_length = 20)

    def __str__(self):
        return self.category_tournirs

    class Meta:
        verbose_name_plural = 'Категории Турниров'

class StarkTournirs(models.Model):
    tournirs_name = 'StarkGaming'
    tournirs_time = models.TextField()
    tournirs_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tournirs_time

    class Meta:
        verbose_name_plural = 'StarkGaming'

class CyberiumTournirs(models.Model):
    tournirs_name = 'Cyberium'
    tournirs_time = models.TextField()
    tournirs_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tournirs_time

    class Meta:
        verbose_name_plural = 'Cyberium'

class CyberArenaTournirs(models.Model):
    tournirs_name = 'CyberArena'
    tournirs_time = models.TextField()
    tournirs_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tournirs_time

    class Meta:
        verbose_name_plural = 'CyberArena'

