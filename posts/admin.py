from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from posts.models import Post, Category

#admin.site.register(Post)
admin.site.register(Category)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['owner']
    list_display = ['title', 'image_html', 'category_list', 'owner_name', 'status']
    list_editable = ['status']
    list_filter = ['owner', 'status']
    search_fields = ['title', 'owner__first_name', 'owner__last_name', 'owner__user_name']
    list_per_page = 7

    def owner_name(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    def category_list(self, obj):
        return mark_safe(", ".join(str(cat) for cat in obj.category.all()))

    owner_name.short_description = 'Owner\'s name'
    owner_name.admin_order_field = 'owner__first_name'

    def image_html(self, post):
        if post.image:
            return mark_safe('<img src="{0}" alr="{1} title="{2}" width="100">'.format(post.image.url, post.title, post.title))
        else:
            return ''

    image_html.short_description = 'Image'
    image_html.admin_order_field = 'image'

    readonly_fields = ['created_on', 'modified_on']
    fieldsets = [
        [None, {
            'fields': ['title', 'image', 'owner']
        }],
        ['Description', {
            'fields': ['text', 'body']
        }],
        ['Attributtes', {
            'fields': ['category', 'status']
        }],
        ['Importante dates', {
            'fields': ['created_on', 'modified_on'],
            'classes': ['collapse']
        }]
    ]
