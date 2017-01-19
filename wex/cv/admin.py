from django.contrib import admin

from .models import (CV, Experience, Paragraph, PersonalData, Skill, Technology,
                     Education)


class ExperienceInline(admin.StackedInline):
    model = Experience


class ParagraphInline(admin.StackedInline):
    model = Paragraph


class PersonalDataInline(admin.StackedInline):
    model = PersonalData
    extra = 1


class TechnologyInline(admin.StackedInline):
    model = Technology


class SkillInline(admin.StackedInline):
    model = Skill


class CVAdmin(admin.ModelAdmin):
    inlines = [PersonalDataInline, SkillInline, ExperienceInline,
               TechnologyInline]
admin.site.register(CV, CVAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline, ]
admin.site.register(Experience, ExperienceAdmin)


class ParagraphAdmin(admin.ModelAdmin):
    pass
admin.site.register(Paragraph, ParagraphAdmin)


class PersonalDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(PersonalData, PersonalDataAdmin)


class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill, SkillAdmin)


class TechnologyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Technology, TechnologyAdmin)


class EducationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Education, EducationAdmin)
