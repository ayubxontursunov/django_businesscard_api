from rest_framework.response import Response
from .serializers import BusinessCardSerializer  # Import your serializer

from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse, Http404
from django.conf import settings
from rest_framework.decorators import api_view
import os
from .elegant_card import create_businesscard


@api_view(["GET"])
def root(request):
    return Response({"message": "Hello REST_API",
                     "/card/firstname": "to download card",
                     "/register": "to submit user details"})


# from .utils import create_businesscard  # Import your function to create business card


class RegisterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Handle GET request
        return Response({
            "job_title": "your-title",
            "email": "your-email",
            "fname": "your-firstname",
            "sname": "your-surname",
            "phone": "your-phonenumber",
            "github": "your-github"

        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BusinessCardSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            create_businesscard(user_data)  # Custom function to create business card

            # You can optionally save the serializer if needed
            # serializer.save()

            return Response({"message": "Successfully registered"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_items(request, name):
    name += ".png"
    image_path = os.path.join(settings.MEDIA_ROOT, name)

    if not os.path.exists(image_path):
        raise Http404("Image does not exist")

    with open(image_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/png")  # Adjust the content type as needed
        response['Content-Disposition'] = f'attachment; filename="{name}"'
        return response
