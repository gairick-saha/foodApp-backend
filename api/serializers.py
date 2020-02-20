from rest_framework import serializers
from api.models import MenuCard, Menu


class MenuCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCard
        fields = ['Menu_Type', 'slug', 'image']
        read_only_field = ('Menu_Type', )

class MenuSerializer(serializers.ModelSerializer):
    
    # category = MenuCardSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
