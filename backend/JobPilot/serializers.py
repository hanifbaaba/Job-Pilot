from rest_framework import serializers 
from .models import CreateJob, ApplyJob
class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateJob
        fields = '__all__'

class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        