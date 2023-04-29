from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(
    [
        models.About, models.CV, models.Niche,
        models.Profile, models.Social, models.Testimonial,
        models.Title
    ]
)