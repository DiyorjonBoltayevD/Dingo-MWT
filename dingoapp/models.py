import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator
from django.db import models


class TagModel(models.Model):
    tag = models.CharField("Tag", max_length=100)

    def __str__(self):
        return self.tag


class FoodModel(models.Model):
    title = models.CharField(verbose_name="Title", max_length=155)
    about = models.TextField(verbose_name='About')
    exclusive = models.BooleanField(verbose_name="Exclusive", default=False)
    price = models.FloatField(verbose_name="Price",
                              validators=(MinValueValidator(0),
                                          MaxValueValidator(9999)
                                          ))
    picture = models.ImageField(upload_to='food/')
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)
    category = models.ManyToManyField("Category", verbose_name="Category")
    tags = models.ManyToManyField(TagModel, verbose_name="Tags", blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(verbose_name="Category name", max_length=150)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ["created"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ChefLevel(models.Model):
    ch_level = models.CharField(verbose_name="Chef Level", max_length=50)

    def __str__(self):
        return self.ch_level


class Chefs(models.Model):
    full_name = models.CharField(verbose_name="Title", max_length=255)
    picture = models.ImageField(verbose_name="Picture", upload_to='chef/')
    level = models.ForeignKey(to=ChefLevel, on_delete=models.CASCADE)
    facebook = models.URLField(verbose_name="Facebook", blank=True, null=True, default="#")
    X_twitter = models.URLField(verbose_name="X", blank=True, null=True, default="#")
    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True, default="#")
    skype = models.URLField(verbose_name="Skype", blank=True, null=True, default="#")

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"

    def __str__(self):
        return self.full_name


def past_date_validator(value):
    current_date = datetime.datetime.today()
    if value.hour == current_date:
        raise ValidationError("The date cannot be in the past. ")
    return value


def past_time_validator(value):
    current_time = datetime.datetime.now()

    if value.hour < current_time.hour and current_time.date() == datetime.date.today():
        raise ValidationError("The time cannot be in past for today.")

    return str(value.hour)


class BookingModel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, blank=True, null=True)
    num_of_g = models.IntegerField(verbose_name="Number of guests")
    phone_number = models.CharField(verbose_name="Phone number", max_length=13)
    date = models.DateTimeField(verbose_name="Date", validators=[past_date_validator])
    time = models.TimeField(verbose_name="Time", validators=[past_time_validator])
    note = models.TextField(verbose_name="Note", blank=True, null=True)

    def __str__(self):
        return self.name
