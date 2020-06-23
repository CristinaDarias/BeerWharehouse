from django.db import models

# Create your models here.
from beers.core.models import CommonInfo
from beers.utils import image_upload_location


class Company(CommonInfo):
    name = models.CharField('Name', max_length=50)
    # tax_number = models.IntegerField('Tax Number', unique=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_YELLOW = 1
    COLOR_AMBER = 2
    COLOR_BROWN = 3
    COLOR_BLACK = 4

    COLOR_CHOICES = (
        (1, 'yellow'),
        (2, 'amber'),
        (3, 'brown'),
        (4, 'black')
    )

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField('Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    isFilter = models.BooleanField('Is filtered', default=False)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey(Company, related_name="beers", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alchol_than(self, alcohol):
        return self.abv > alcohol


class SpecialIngredient(CommonInfo):
    name = models.CharField('Name', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, related_name="special_ingredients")

    class Meta:
        verbose_name = "Special Ingredient"
        verbose_name_plural = "Special Ingredients"
        ordering = ['name']

    def __str__(self):
        return self.name
