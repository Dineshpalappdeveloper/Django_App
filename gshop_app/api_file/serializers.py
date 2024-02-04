from rest_framework import serializers
from ..models import CarList

# validators


def alphanumeric(value):
    if not value.isalnum():
        raise serializers.ValidationError(
            {'chassisnumber': 'Chassis number must be alphanumeric'})
    return value


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        # all attributes
        # fields = '__all__'
        # exclude = ['name'] kisi ek field ko nahi lena ho to
        exclude = ['name']
        # if specified,
        # fields = ('id', 'name', 'description', 'is_active',)


# class CarSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # is_active = serializers.BooleanField(read_only=True)
    # chassisnumber = serializers.CharField(validators=[alphanumeric])
    # price = serializers.DecimalField(max_digits=9, decimal_places=2)

    # def create(self, validated_data):
    #     return CarList.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.is_active = validated_data.get(
    #         'is_active', instance.is_active)
    #     instance.chassisnumber = validated_data.get(
    #         'chassisnumber', instance.chassisnumber)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.save()
    #     return instance

    # field labels validation

    def validate_price(self, value):
        if value <= 20000.00:
            raise serializers.ValidationError(
                'Price must be greater than 20000.00')
        return value

    # object validation

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                {'name': 'Name and description must be different'})
        return data
