from django.db import models
from django.urls import reverse


class Blog(models.Model):
    COLOR = (
        ('black', 'черный'),
        ('white', 'белый')
    )
    title = models.CharField(verbose_name='Название', max_length=255)
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    color = models.CharField(choices=COLOR, verbose_name='Цвет блока', max_length=50)

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title