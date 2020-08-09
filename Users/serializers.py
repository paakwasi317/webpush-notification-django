from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from drf_writable_nested import WritableNestedModelSerializer
from Users.models import Users





class UserSerializer(serializers.ModelSerializer):
    othernames =    serializers.CharField(allow_blank=True, max_length=200)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Users.objects.all())]
            )

    password = serializers.CharField(min_length=8)

    class Meta:
        model = Users
        fields = ['email', 'firstname', 'lastname', 'othernames', 'username', 'isadmin', 'phone', 'referral_code','location', 'password', 'profilepic']
        write_only_fields = ['password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class NoPasswwordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','email', 'firstname', 'lastname', 'othernames', 'username', 'isadmin', 'phone', 'referral_code','location', 'profilepic']


class CompUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['firstname', 'lastname', 'othernames','phone', 'location']