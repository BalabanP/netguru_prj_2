from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import status
import os
from .fun_fact_service import get_fun_fact
from .models import DatesFact, PopularDates
from django.db.models import Count
from .serializers import (
    DatesFactSerializer,
    AllDatesFactSerializer,
    PopularDatesSerializer,
)
from rest_framework import viewsets, status
import calendar
from rest_framework.decorators import action
from django.forms.models import model_to_dict


class PopularViewSet(viewsets.ModelViewSet):
    serializer_class = PopularDatesSerializer

    def get_queryset(self):
        stu = DatesFact.objects.values("month").annotate(days_checked=Count("month"))
        for id, value in enumerate(stu):
            value["id"] = id + 1
            value["month"] = calendar.month_name[value["month"]]
        return stu

    def list(self, request):
        values = self.get_queryset()
        return Response(values)


class FunDatesViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing FunDates instances.
    """

    queryset = DatesFact.objects.all()
    serializer_class = DatesFactSerializer

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        month, day = serializer.validated_data.get(
            "month"
        ), serializer.validated_data.get("day")
        facts = get_fun_fact(month, day)
        data = {"month": month, "day": day, "fact": facts}
        date_fact = DatesFact.objects.filter(month=month, day=day).update_or_create(
            defaults=data
        )
        filtred_data = model_to_dict(date_fact[0])
        serializer = AllDatesFactSerializer(data=filtred_data)
        serializer.is_valid(raise_exception=True)
        if not date_fact[1]:
            return Response(
                {"msg": f"Data  Updated", "id": filtred_data.get("id")},
                status=status.HTTP_200_OK,
            )
        return Response(filtred_data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DatesFactSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Data  Updated", "id": serializer.validated_data.get("id")},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retreive(self, request, pk=None):
        if pk is not None:
            serializer = self.get_serializer(self.get_object())
            return Response(serializer.data)

    def destroy(self, request, pk):
        record_to_delete = self.get_object()
        secret_key = request.headers.get(os.environ.get("DELETE_KEY"))
        if not secret_key:
            return Response(
                {"msg": f"please provide {os.environ.get('DELETE_KEY')} in headers"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            if secret_key != os.environ.get("DELETE_KEY_VALUE"):
                return Response(
                    {"msg": "provided secret key is not correct"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        deleted_id = record_to_delete.id
        record_to_delete.delete()
        return Response(
            {"msg": "Data Deleted", "id": deleted_id},
            status=status.HTTP_200_OK,
        )
