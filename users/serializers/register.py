from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 
                  'first_name', 'last_name', 'city', 
                  'country', 'phone', 'born_date', 'experience_with_ia', 
                  'organization_type', 'organization', 'why_us')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            city=validated_data['city'], 
            country=validated_data['country'],
            phone=validated_data['phone'],
            born_date=validated_data['born_date'],
            experience_with_ia=validated_data['experience_with_ia'],
            organiation_type=validated_data['organization_type'],
            organization=validated_data['organization'],
            why_us=validated_data['why_us'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user