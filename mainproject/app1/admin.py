from django.contrib import admin

# Register your models here.
from .models import admission
from .models import admission2

from .models import feedbackform
admin.site.register(feedbackform)
admin.site.register(admission)
admin.site.register(admission2)





