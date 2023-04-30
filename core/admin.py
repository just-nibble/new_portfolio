from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(
    [
        models.About, models.CV, models.CodingSkill,
        models.Education, models.Experience, models.Niche,
        models.Portfolio,
        models.Profile, models.Social, models.Testimonial,
        models.Title
    ]
)