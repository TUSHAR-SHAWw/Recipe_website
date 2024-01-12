from django.utils.text import slugify
import uuid
def gerenate_slug(self,title=str)->str:
    from .models import Recipe
    title=slugify(title)
    while(Recipe.objects.filter(slug=title).exists()):
        title= f'{title}-{uuid.uuid4().hex[:4]}'
    return title