from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('essential_oil', 'Essential Oil'),
        ('diffuser', 'Diffuser'),
        ('roll_on', 'Roll On'),
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Price in euros"
    )
    stock = models.IntegerField()
    features = models.TextField(
        blank=True,
        help_text="Key features of the product"
    )
    contents = models.TextField(
        blank=True,
        help_text="Contents of the product, if applicable"
    )
    image = models.ImageField(
        upload_to='product_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
