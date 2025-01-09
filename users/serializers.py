from rest_framework import serializers
from .models import Customer, RestaurantOwner
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class CustomerSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required = False)
    class Meta:
        model = Customer
        fields = ['user_name', 'name', 'mobile_number', 'email', 'address', 'profile', 'password', 'password2']       

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        password2 = validated_data.pop('password2', None)
        customer = super().create(validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer
    

class CustomerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user_name', 'name', 'mobile_number', 'email', 'address', 'profile']
    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.name = validated_data.get('name', instance.name)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class CustomerPasswordUpdateSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only = True)
    new_password1 = serializers.CharField(write_only = True)
    new_password2 = serializers.CharField(write_only = True)

    class Meta:
        model = Customer
        fields = ['old_password', 'new_password1', 'new_password2']

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError("Passwords must match.")
        
        user = self.context['request'].user
        old_password = data['old_password']
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('new_password1', instance.password))
        instance.save()
        return instance

    
class RestaurantOwnerSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required = False)
    class Meta:
        model = RestaurantOwner
        fields = ['user_name', 'name', 'mobile_number', 'email', 'profile', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        owner = super().create(validated_data)
        owner.set_password(validated_data['password'])
        owner.save()
        return owner
    

class RestaurantOwnerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = RestaurantOwner
        fields = ['user_name', 'name', 'mobile_number', 'email', 'profile']
    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.name = validated_data.get('name', instance.name)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    

class RestaurantOwnerPasswordUpdateSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only = True)
    new_password1 = serializers.CharField(write_only = True)
    new_password2 = serializers.CharField(write_only = True)

    class Meta:
        model = RestaurantOwner
        fields = ['old_password', 'new_password1', 'new_password2']

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError("Passwords must match.")
        
        user = self.context['request'].user
        old_password = data['old_password']
        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('new_password1', instance.password))
        instance.save()
        print({"message": "Password updated successfully"})
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

