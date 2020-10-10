from django.contrib.auth.models import User, Group
from rest_framework import serializers
from fortune.models import *


class FortuneSerializer(serializers.HyperlinkedModelSerializer):
    """Checklist serializer"""
    company_id = serializers.CharField(source='company_id.id')
    class Meta:
        model = FortuneCookie
        fields = ('id', 'fortune_option', 'company_id')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    """Company serializer"""
    class Meta:
        model = Company
        fields = ('id', 'name', 'email', 'phone_number', 'gst_number', 'status')