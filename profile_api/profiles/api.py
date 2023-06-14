from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'first_name', 'last_name']

@api_view(['POST', 'PATCH'])
def create_or_update_profile(request):
    try:
        profile = UserProfile.objects.get(pk=request.data.get('id'))
    except UserProfile.DoesNotExist:
        profile = None

    serializer = UserProfileSerializer(instance=profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)