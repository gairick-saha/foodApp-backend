from rest_framework import serializers
from api.models import MenuCard, Menu


class MenuCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCard
        fields = '__all__'
        read_only_fields = ('Menu_Type', )

class MenuSerializer(serializers.ModelSerializer):

    category = MenuCardSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
