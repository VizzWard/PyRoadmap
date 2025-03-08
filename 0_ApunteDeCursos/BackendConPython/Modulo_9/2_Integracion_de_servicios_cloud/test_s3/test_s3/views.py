from django.shortcuts import render


from images.models import ImageModel

def index(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        aws_image = ImageModel.objects.create(
            name=image.name,
            image=image
        )

        print(f"Imagen subida a S3: {aws_image.image.url}")  # Verifica la URL


    return render(request, 'index.html', {
    })