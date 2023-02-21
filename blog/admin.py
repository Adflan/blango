from django.contrib import admin
from blog.models import Tag, Post

# attributes (prepopulated fields) of the subclass determine how
# the model is displayed. Used in this way puts some JavaScript
# into the admin page so that SLUG field updates when TITLE field
# changes. Many ways to customise the Model Admin (exclude, fields, 
# list_display, etc...) - Adam learning note

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')

admin.site.register(Post, PostAdmin)


