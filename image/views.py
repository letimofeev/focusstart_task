from django.shortcuts import render

from image.handlers.image import ImageHandler
from .forms import (
    ImageForm,
)


def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)

        if image_form.is_valid():
            image_form.save()
            color = image_form.cleaned_data['color']

            # Get the current instance object to display in the template
            img_model_obj = image_form.instance
            img_obj = ImageHandler(img_model_obj.image.name)

            color_count = img_obj.color_counter(color)

            return render(
                request,
                'index.html',
                context={
                    'image_form': image_form,
                    'img_model_obj': img_model_obj,
                    'color_count': color_count,
                }
            )
    else:
        image_form = ImageForm()

    return render(
        request,
        'index.html',
        context={'image_form': image_form}
    )

