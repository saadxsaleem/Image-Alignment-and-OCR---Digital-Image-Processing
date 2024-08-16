import cv2
import numpy as np
import os
import uuid  
from django.shortcuts import render
from django.http import JsonResponse
from .newcode import ocr, edgeDetection, findContour, scan,remove_shadow,enhance_saturation
from django.conf import settings
from django.http import HttpResponse



def upload(request):
    return render(request, 'upload.html')

def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        processed_image_path = processImage(image, image_file)
        return JsonResponse({'processed_image_path': processed_image_path})
    return JsonResponse({'error': 'Image file not provided'})

def removeshad(request):
    if request.method == 'POST':
        imagepath = request.POST.get('imagePath')  
        shadowsrm(imagepath)
        return JsonResponse({'processed_image_path': imagepath})
    return JsonResponse({'error': 'Image file not provided'})

def performOCR(request):
    if request.method == 'POST':
        imagepath = request.POST.get('imagePath')
        if not imagepath:
            return JsonResponse({'error': 'Image path not provided'}, status=400)

        text_file_path = doOCR(imagepath)

        # Return the path of the text file to the client
        return JsonResponse({'text_file_path': text_file_path})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def download_text_file(request):
    text_file_path = request.GET.get('text_file_path')
    if not text_file_path or not os.path.exists(text_file_path):
        return JsonResponse({'error': 'Text file not found'}, status=404)

    with open(text_file_path, 'r') as file:
        response = HttpResponse(file.read(), content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(text_file_path)}'
        return response

def doOCR(imagepath):
    processed_image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
    image_name = os.path.basename(imagepath)
    processed_image_path = os.path.join(processed_image_dir, image_name)

    image = cv2.imread(processed_image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {processed_image_path}")
    
    text = ocr(image)  

   
    text_file_path = os.path.join(processed_image_dir, f"{os.path.splitext(image_name)[0]}.txt")
    with open(text_file_path, 'w') as text_file:
        text_file.write(text)
    
    return text_file_path

def brightenImage(request):
    if request.method == 'POST':
        imagepath = request.POST.get('imagePath')

        processed_image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
        image_name = os.path.basename(imagepath)
        processed_image_path = os.path.join(processed_image_dir, image_name)

        image = cv2.imread(processed_image_path)

        brightened_image = cv2.convertScaleAbs(image, alpha=1.05, beta=0)
        cv2.imwrite(processed_image_path, brightened_image)

        # Return the path of the text file to the client
        return JsonResponse({'processed_image_path': imagepath})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def saturateImage(request):
    if request.method == 'POST':
        imagepath = request.POST.get('imagePath')

        processed_image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
        image_name = os.path.basename(imagepath)
        processed_image_path = os.path.join(processed_image_dir, image_name)

        image = cv2.imread(processed_image_path)

        enhancedImage = enhance_saturation(image)
        cv2.imwrite(processed_image_path, enhancedImage)

        # Return the path of the text file to the client
        return JsonResponse({'processed_image_path': imagepath})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def shadowsrm(imagepath):
    processed_image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
    image_name = os.path.basename(imagepath)
    processed_image_path = os.path.join(processed_image_dir, image_name)

    image = cv2.imread(processed_image_path)
   
    new = remove_shadow(image)
    cv2.imwrite(processed_image_path, new)
    return new


def processImage(image, image_file):

    EdgedImage = edgeDetection(image)  
    screenCnt = findContour(EdgedImage)
    newImage = image
    if screenCnt.size > 0:
        newImage = scan(screenCnt, image)   
    
    
    processed_image_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')

    
    filename = str(uuid.uuid4()) + '.jpg'
    processed_image_path = os.path.join(processed_image_dir, filename)

  
    cv2.imwrite(processed_image_path, newImage)

    return filename


   

