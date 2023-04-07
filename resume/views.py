from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes

from .models import Resume
from .serializers import ResumeSerializer


@api_view(['GET', 'PATCH'])
@authentication_classes([TokenAuthentication])
def resume(request):
    if request.user.is_anonymous:
        raise Http404()

    r = get_object_or_404(Resume, email=request.user.email)

    if request.method == 'GET':
        serializer = ResumeSerializer(r)
        return JsonResponse(serializer.data)

    if request.method == 'PATCH':
        if serializer.is_valid():
            # TODO Patch Resume object.
            pass
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=405)

