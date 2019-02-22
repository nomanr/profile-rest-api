from rest_framework import serializers

from . import models 

class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects"""


    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_date):
        """Create and return a new user"""

        user = models.UserProfile(
            email = validated_date['email'],
            name = validated_date['name'], 
        )

        user.set_password(validated_date['password'])
        user.save()

        return user

class ProfileFeelItemSerializer(serializers.ModelSerializer):
    """A serializer for our profile feed item"""

    class Meta: 
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only' : True}}
