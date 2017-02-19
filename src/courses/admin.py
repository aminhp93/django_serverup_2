from django.contrib import admin

from .forms import LectureAdminForm
from .models import Course, Lecture, MyCourse
# Register your models here.

class LectureInline(admin.TabularInline):
	model = Lecture
	form = LectureAdminForm
	prepopulated_fields = {"slug": ("title",)}
	#raw_id_fields = ['video']
	extra = 1

class CourseAdmin(admin.ModelAdmin):
	inlines = [LectureInline]
	list_filter = ['title', 'timestamp']
	list_display = ['title', 'updated', 'timestamp']
	readonly_fields = ['updated', 'timestamp']
	search_fields = ['title', 'description']

	class Meta:
		model = Course


admin.site.register(Course, CourseAdmin)
admin.site.register(MyCourse)
