from django.contrib import admin
from courses.models import Course , Tag , Prerequisite , Learning , Video , Payment  , UserCourse

# Register your models here.
class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin , LearningAdmin , PrerequisiteAdmin , VideoAdmin ]

admin.site.register(Course , CourseAdmin)
admin.site.register(UserCourse)
admin.site.register(Payment)
