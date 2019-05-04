from django.contrib import admin
from django.contrib.auth import authenticate
from .models import Choice,Question,User
#from .forms import UserInfo

#user=authenticate(username='deny',password='apr201912')
#if user is not None:
#    return(self,hasattr)
#else
#    def __self__(self,quit)


 
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_filter = ['pub_date']    
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(User)    
