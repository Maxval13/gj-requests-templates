from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        is_main = False
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                is_main = True
                count += 1
        if not is_main:
            raise ValidationError('Укажите основной раздел')
        elif count > 1:
            raise ValidationError('Основной раздел уже выбран')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline, ]
    list_filter = ['tags']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
