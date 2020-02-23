from rest_framework import serializers
from api.models import MenuCard, Menu


class MenuCardSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False, read_only=True)
    menu_type = serializers.CharField(required=False, )
    slug = serializers.CharField(required=True, )
    image = serializers.ImageField(required=False, )

    class Meta:
        model = MenuCard
        fields = [
            'id',
            'menu_type',
            'slug',
            'image'
        ]
        read_only_fields = ['id', ]

class MenuSerializer(serializers.ModelSerializer):

    price = serializers.CharField()
    category_id = serializers.IntegerField(required=False, read_only=True, )
    category = MenuCardSerializer(many=False, )

    class Meta:
        model = Menu
        fields = [
            'category_id',
            'category',
            'item_name',
            'slug',
            'image',
            'description',
            'price',
            'stock',
            'available'
        ]
        read_only_fields = ['category_id', ]
        # depth = 1

    def create(self, validated_data):
        # category = validated_data.pop('category')
        print(validated_data)
        return Menu.objects.create(**validated_data)
        # return category
