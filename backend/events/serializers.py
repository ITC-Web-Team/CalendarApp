from rest_framework import serializers
from .models import *

class UserCategorySerializer(serializers.Serializer):
    model=UserCategory
    fields='__all__'

    def create(self,validated_data):
        return UserCategory.objects.create(**validated_data)
    
    def update():
        return
    


class BodySerializer(serializers.Serializer):
    model=Body
    fields='__all__'

    def create(self, validated_data):
        return Body.objects.create(**validated_data)
    
    def update():
        return



class UserSerializer(serializers.Serializer):
    user_category=serializers.PrimaryKeyRelatedField(
        many=True, queryset=UserCategory.objects.all()
    )
    body=serializers.PrimaryKeyRelatedField(
        many=True, queryset=Body.objects.all()
    )
    class Meta:
        model = User
        fields = '__all__'
    
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