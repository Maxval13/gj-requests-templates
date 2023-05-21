from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название тега', blank=True, null=True)
    articles = models.ManyToManyField(Article, related_name='tags', through='Scope')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['id']

    def __str__(self):
        return self.name


class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scope', verbose_name='Тег')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='scope')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Тег статьи'
        verbose_name_plural = 'Теги статьи'
        ordering = ['-is_main']

