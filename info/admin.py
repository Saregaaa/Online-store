import site
from django.contrib import admin

from info.models import FAQ, Contact

# Register your models here.
admin.site.register(Contact)

admin.site.register(FAQ)