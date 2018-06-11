from django.core.exceptions import ValidationError
from django.forms import ModelForm

from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['owner', 'status']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image is not None and 'image' not in image.content_type:
            raise ValidationError('La imagen no es válida')
        return image


