from django.contrib import admin
from .models import Lang,Engine,Review,Enterprise

# Register your models here.

class ReviewInLine(admin.TabularInline):
  model = Review
  extra = 1
  
  
class LangAdmin(admin.ModelAdmin):
  list_display = ('name','lang_type','date_added')
  inlines = [ReviewInLine]
  
  
class EngineAdmin(admin.ModelAdmin):
  list_display = ('name','lang',)
  
  

class EnterpriseAdmin(admin.ModelAdmin):
  list_display = ('name','adapted_date')
  filter_horizontal = ('langs',)


admin.site.register(Lang,LangAdmin)
admin.site.register(Engine,EngineAdmin)
admin.site.register(Enterprise,EnterpriseAdmin)


