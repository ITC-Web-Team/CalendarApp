from rest_framework import serializers
from .models import User, Event

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields='__all__'

        def create(self, validated_data):
            return User.objects.create(**validated_data)
        
        def update(self, user, validated_data):

            user.save()
            return user
        
class EventSerializer(serializers.Serializer):
    class Meta:
        model = Event
        fields='__all__'

        def create(self, validated_data):
            return Event.objects.create(**validated_data)
        
        def update(self, event, validated_data):

            event.save()
            return event