from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        """
        Define cómo se representa un Post como una string
        :return:
        """
        return '{0}'.format(self.name)

