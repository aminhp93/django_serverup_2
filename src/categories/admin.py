from django.contrib import admin

from .forms import CategoryAdminForm
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_filter = ["updated", "timestamp"]
	list_display = ['title', 'updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	search_fields = ['title']
	ordering = ['title']
	form = CategoryAdminForm

	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)