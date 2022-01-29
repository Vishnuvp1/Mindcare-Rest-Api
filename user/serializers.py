from rest_framework import serializers
from user.models import AccountModel

class RegistrationSeializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = AccountModel
        fields = ['first_name', 'last_name', 'email', 'phone',  'password', 'password2']

        extra_kwargs = {
            'passowrd': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'Password and Confirm Password should be same.'})

        if  AccountModel.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists!'})

        account =  AccountModel(email=self.validated_data['email'], phone=self.validated_data['phone'])
        account.set_password(password)
        account.save()

        return account