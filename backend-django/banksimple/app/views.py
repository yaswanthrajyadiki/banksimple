# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
import re
from django.db.models import Q
from models import  *
# Create your views here.


class BranchAPI(APIView):

    def get(self, request, *args, **kwargs):
        branch_attributes = ["id", "name", "address", "postal_code", "latitude", "longitude",
                                              "smsq", "operating_hours", "week_day_start_time", "week_day_end_time",
                                              "week_end_start_time", "week_end_end_time"]
        branches = Branch.objects.all()
        branches_dicts = []
        for branch in branches:
            branch_dict = {}
            for branch_attribute in branch_attributes:
                branch_dict[branch_attribute] = getattr(branch, branch_attribute, None)
            branches_dicts.append(branch_dict)
        return Response({"status": status.HTTP_200_OK, "branches": branches_dicts})


class AppointmentAPI(APIView):

    def get(self, request, *args, **kwargs):
        appointment_attributes = []