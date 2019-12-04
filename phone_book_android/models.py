from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modify_time = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class Phone(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='phone_book_android/phone_image/', blank=True, null=True)

    def __str__(self):
        return 'Phone(%s, %s)' %(self.name, self.phone)
