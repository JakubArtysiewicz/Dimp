from django.http import HttpResponse
from django.shortcuts import render
from rembg import remove


def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        input_data = request.FILES["image"].read()
        output_data = remove(input_data)

        return HttpResponse(output_data, content_type="image/png")

    return render(request, "upload.html")