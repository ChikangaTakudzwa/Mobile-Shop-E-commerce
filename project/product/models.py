from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    model = models.SlugField()
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price

    def get_thubmnail(self):
        # check to see if already exist and return it
        if self.thumbnail:
            return self.thumbnail.url
        else:
            # if thumbnail dont exist check if image if available
            if self.image:
                # if true call the make_thumbnail method and make thumbnail out of image
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240.jpg'

    # make thumbnail method, take in image and default size
    def make_thumbnail(self, image, size=(300, 300)):
        # use the Image class from PIL to open image file
        img = Image.open(image)
        # convert to RGB
        img.convert('RGB')
        # generate thumbnail
        img.thumbnail(size)

        # saving image to the server
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        # make method return the saved image
        thumbnail = FIle(thumb_io, name=image.name)
        return thumbnail