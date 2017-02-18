from django.contrib import admin

from .models import Course, Lecture
# Register your models here.

class LectureInline(admin.TabularInline):
	model = Lecture

class CourseAdmin(admin.ModelAdmin):
	inlines = [LectureInline]
	list_filter = ['title', 'timestamp']
	list_display = ['title', 'updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	search_fields = ['title', 'description']

	class Meta:
		model = Course


admin.site.register(Course, CourseAdmin)
