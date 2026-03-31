from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image
from rembg import remove
import io

def remove_bg(request):
    if request.method == "POST" and request.FILES.get("image"):
        input_data = request.FILES["image"].read()
        output_data = remove(input_data)

        return HttpResponse(output_data, content_type="image/png")

    return render(request, "upload.html", {"button_text": "Usuń"})

def gray(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]

        img = Image.open(image_file)

        gray_img = img.convert("L")

        buffer = io.BytesIO()
        gray_img.save(buffer, format="PNG")
        buffer.seek(0)

        return HttpResponse(buffer.getvalue(), content_type="image/png")

    return render(request, "upload.html", {"button_text": "Zamień"})