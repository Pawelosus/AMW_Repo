from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Gallery
from .serializers import GallerySerializer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


@csrf_exempt
def gallery_list(request):
    if request.method == 'GET':
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(galleries, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GallerySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def gallery_detail(request, pk):
    try:
        gallery = Gallery.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GallerySerializer(gallery)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GallerySerializer(gallery, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        gallery.delete()
        return HttpResponse(status=204)