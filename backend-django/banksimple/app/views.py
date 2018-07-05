# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, authenticate

from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
import re
from django.db.models import Q
from models import  *
from serializer import *
# Create your views here.


class UserAPI(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            login(request, user)
            user_data = UserSerializer(user).data
            del(user_data["password"])
            return Response({"status": status.HTTP_200_OK, "user": user_data})
        except Exception as e:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "branches": [], "error": e.message})

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response({"status": status.HTTP_200_OK, "message": "User was successfully created."})
                else:
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "error": "User was not created"})
            else:
                return Response({"status": status.HTTP_400_BAD_REQUEST,
                             "error": "User was not created because of following errors %s" % serializer.errors})
        except Exception as e:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "error": e.message})


class BranchAPI(APIView):

    @staticmethod
    def expand(branch):
        branch_attributes = ["id", "name", "address", "postal_code", "latitude", "longitude",
                             "smsq", "operating_hours", "week_day_start_time", "week_day_end_time",
                             "week_end_start_time", "week_end_end_time"]
        branch_dict = {}
        for branch_attribute in branch_attributes:
            branch_dict[branch_attribute] = getattr(branch, branch_attribute, None)
        return branch_dict

    def get(self, request, *args, **kwargs):
        branches = Branch.objects.all()
        branches_dicts = []
        for branch in branches:
            branches_dicts.append(self.expand(branch))
        return Response({"status": status.HTTP_200_OK, "branches": branches_dicts})


class AppointmentAPI(APIView):

    @staticmethod
    def expand(appointment):
        appointment_attributes = ['user', 'title', 'description', 'branch', 'start_time', 'end_time', 'rm']
        appointment_dict = {}
        for appointment_attribute in appointment_attributes:
            appointment_dict[appointment_attribute] = getattr(appointment, appointment_attribute, None)
        return appointment_dict

    def get(self, request, *args, **kwargs):
        appointments = Appointment.objects.all()
        appointments_dicts = []
        for appointment in appointments:
            appointments_dicts.append(self.expand(appointment))
        return Response({"status": status.HTTP_200_OK, "appointments": appointments})
