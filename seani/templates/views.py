from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


from .models import Exam
from .forms import CandidateForm
