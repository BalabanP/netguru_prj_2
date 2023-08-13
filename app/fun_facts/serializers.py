from rest_framework import serializers
from .models import DatesFact, PopularDates


class PopularDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularDates
        fields = ("id", "month", "days_checked")
        read_only_fields = ("id", "month", "days_checked")


class AllDatesFactSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    fact = serializers.CharField()


class DatesFactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    fact = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return DatesFact.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs.get("month") not in range(1, 13):
            raise serializers.ValidationError("month can be from 1-12")
        elif attrs.get("day") not in range(1, 32):
            raise serializers.ValidationError("day can be from 1-31")
        return attrs

    def update(self, instance, validated_data):
        instance.month = validated_data.get("month", instance.month)
        instance.day = validated_data.get("day", instance.day)
        instance.save()
        return instance
