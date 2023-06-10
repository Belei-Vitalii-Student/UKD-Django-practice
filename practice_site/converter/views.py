from django.shortcuts import render
from .forms import ImageUploadForm
from .models import MyImageModel
from PIL import Image
import os

def index(request):
    history = MyImageModel.objects.all()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            color_hex = form.cleaned_data['color']
            my_image = MyImageModel(image=image)
            my_image.save()

            img = Image.open(image)
            save_path = os.path.join('images', image.name.replace('.png', '.jpg'))
            color_tuple = tuple(int(color_hex[i:i+2], 16) for i in (1, 3, 5))

            converted_image = Image.new('RGBA', img.size, color_tuple)
            converted_image.paste(img, (0, 0), img)
            converted_image = converted_image.convert('RGB')
            converted_image.save(os.path.join('media', save_path), format='JPEG')

            return render(request, 'converter/index.html', {'image': image, 'converted': save_path, 'form': form, 'current_image': image, 'history': history})
    else:
        form = ImageUploadForm()
    return render(request, 'converter/index.html', {'form': form, 'history': history})