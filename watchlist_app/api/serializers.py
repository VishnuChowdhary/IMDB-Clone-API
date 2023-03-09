from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        
    # Object Level Validator
    def validate(self, data):
        if data['title'] == data['description']:
            return serializers.ValidationError("Title and Description should be diffrent")
        else:
            return data
    
    # Field Level validator
    def validate_name(self, value):
        if len(value) < 2:
            return serializers.ValidationError("Name is Too short")
        else:
            return value
    

"""
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('name', instance.description)
        instance.active = validated_data.get('name', instance.active)
        instance.save()
        return instance
    
    # Object Level Validator
    def validate(self, data):
        if data['title'] == data['description']:
            return serializers.ValidationError("Title and Description should be diffrent")
        else:
            return data
    
    # Field Level validator
    def validate_name(self, value):
        if len(value) < 2:
            return serializers.ValidationError("Name is Too short")
        else:
            return value
"""