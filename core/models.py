from django.db import models

# Create your models here.


class About(models.Model):
    body = models.TextField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return "Princewil About"


class CodingSkill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class CV(models.Model):
    link = models.URLField()

    def __str__(self):
        return "Princewil Resume"


class Education(models.Model):
    year_of_entry = models.CharField(max_length=4)
    institution_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.institution_name
    

class Experience(models.Model):
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=7, default="current")
    institution_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.institution_name


class Niche(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField

    def __str__(self):
        return str(self.title)


class Profile(models.Model):
    role = models.CharField(max_length=255)
    picture = models.URLField()

    def __str__(self):
        return "Princewil Profile"


class Social(models.Model):
    github = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return "Princewil Social"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.client_name


class Title(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
