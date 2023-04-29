from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(
    [
        models.About, models.CV, models.Education,
        models.Experience, models.Niche,
        models.Profile, models.Social, models.Testimonial,
        models.Title
    ]
)