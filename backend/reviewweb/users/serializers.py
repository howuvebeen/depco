from rest_framework import serializers, fields
from .models import Profile, SkinType, SkinIssue, Interest
from reviews.models import Review
from django.contrib.auth.models import User
from products.serializers import ProductSerializer
from rest_framework.authtoken.models import Token

from users.choices import SKINISSUE_CHOICES, SKINTYPE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    """
    Serialize User Model
    """

    class Meta:
        model = User
        read_only_fields = ['email']
        fields = ['pk', 'username', 'email',
                  'first_name', 'last_name', 'is_active']


class SkinTypeSerializer(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        return value.name


class SkinIssueSerializer(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        return value.name


class MyReviewRelatedField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        a_list = list(Review.objects.filter(pk=value.pk))

        return a_list[0].user.username


class InterestSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_photo = serializers.SerializerMethodField()
    product_company = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    product_quantity = serializers.SerializerMethodField()
    product_average_star = serializers.SerializerMethodField()
    product_review_number = serializers.SerializerMethodField()

    def get_product_name(self, obj):
        product_name = obj.product.name
        return product_name

    def get_product_photo(self, obj):
        product_photo = obj.product.photo.url
        return product_photo

    def get_product_company(self, obj):
        product_company = obj.product.company.name
        return product_company

    def get_product_price(self, obj):
        product_price = obj.product.price
        return product_price

    def get_product_quantity(self, obj):
        product_quantity = obj.product.quantity
        return product_quantity

    def get_product_average_star(self, obj):
        product_average_star = obj.product.average_star
        return product_average_star

    def get_product_review_number(self, obj):
        product_review_number = obj.product.review_number
        return product_review_number

    class Meta:
        model = Interest
        fields = ['pk', 'author', 'product', 'product_name', 'product_photo', 'product_company',
                  'product_price', 'product_quantity', 'product_average_star', 'product_review_number']


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serialize Profile model
    """
    thumbnail = serializers.ImageField(use_url=True, required=False, allow_empty_file=True)
    photo = serializers.ImageField(
        use_url=True, required=False, allow_empty_file=True)
    interest = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    firstname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    skintype = SkinTypeSerializer(
        many=True, queryset=SkinType.objects.all(), required=False)
    skinissue = SkinIssueSerializer(
        many=True, queryset=SkinIssue.objects.all(), required=False)

    def get_last_login(self, obj):
        last_login = obj.user.last_login
        return last_login

    def get_firstname(self, obj):
        firstname = obj.user.first_name
        return firstname

    def get_lastname(self, obj):
        lastname = obj.user.last_name
        return lastname

    def get_age(self, obj):
        return obj.age

    def get_email(self, obj):
        email = obj.user.email
        return email

    def get_reviews(self, obj):
        from reviews.serializers import ReviewSerializer
        reviews = Review.objects.filter(author=obj.pk)
        return ReviewSerializer(reviews, many=True).data

    class Meta:
        model = Profile
        read_only_fields = ['user',
                            'last_login', 'age_range']
        fields = ['user', 'firstname', 'lastname', 'email', 'last_login',
                  'thumbnail', 'photo', 'gender', 'dob', 'age', 'age_range',
                  'skintype', 'skinissue', 'influencer', 'influencer_link', 'interest',
                  'reviews', 'terms']


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_pk = serializers.SerializerMethodField()
    influencer = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()

    def get_username(self, obj):
        user = obj.user.username
        return user

    def get_user_pk(self, obj):
        user = obj.user.pk
        return user

    def get_influencer(self, obj):
        profile_l = list(Profile.objects.filter(pk=obj.user.pk))
        profile = profile_l[0]
        influencer = profile.influencer
        return influencer

    def get_last_login(self, obj):
        last_login = obj.user.last_login
        return last_login

    class Meta:
        model = Token
        fields = ['user_pk', 'username', 'influencer', 'last_login', 'key']

