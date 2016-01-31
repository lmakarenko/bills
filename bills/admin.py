# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import counter_type, counter, counter_data

admin.site.register(counter_type)
admin.site.register(counter)
admin.site.register(counter_data)
