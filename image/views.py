from django.shortcuts import render
from .forms import ImageForm
from image.handlers.image import ImageHandler


def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            ImageHandler(img_obj.image.name)

            return render(
                request,
                'index.html',
                context={
                    'form': form,
                    'img_obj': img_obj
                }
            )
    else:
        form = ImageForm()

    return render(
        request,
        'index.html',
        context={'form': form}
    )

