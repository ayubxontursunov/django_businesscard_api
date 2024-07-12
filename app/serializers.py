from rest_framework import serializers

class BusinessCardSerializer(serializers.Serializer):
    fname = serializers.CharField(max_length=100)
    sname = serializers.CharField(max_length=100)
    job_title = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    github = serializers.CharField(max_length=100)
