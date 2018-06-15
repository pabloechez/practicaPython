import os

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        """
        Define cómo se representa un Post como una string
        :return:
        """
        return '{0}'.format(self.name)


class Post(models.Model):
    PENDING = 'PEN'
    APPROVED = 'APR'
    FINISHED = 'FIN'
    STATUSES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (FINISHED, 'Finished')

    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    body = models.TextField()
    image = models.FileField(null=True)
    category = models.ManyToManyField(Category)

    status = models.CharField(max_length=3, choices=STATUSES, default=PENDING)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def filename_extension(self):
        basename, extension = os.path.splitext(os.path.basename(self.image.name))
        return extension

    def __str__(self):
        """
        Define cómo se representa un Post como una string
        :return:
        """
        categories = ", ".join(str(cat) for cat in self.category.all())
        return '{0} ({1})'.format(self.title, categories)