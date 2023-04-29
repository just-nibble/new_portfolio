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
    

class CV(models.Model):
    link = models.URLField()

    def __str__(self):
        return "Princewil Resume"


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
