from django.contrib import admin
from myblog.models import Post
from myblog.models import Category

class CategoryInline(admin.StackedInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'author', 'published_date',)
    inlines = [
        CategoryInline,
    ]
admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
admin.site.register(Category, CategoryAdmin)


