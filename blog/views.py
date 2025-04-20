from django.shortcuts import render, redirect

# Create your views here.
#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse
import os
from blog import models
from django.shortcuts import render, redirect
import json
from django.core.files.storage import FileSystemStorage
import shutil

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage #分页功能
import requests

import matplotlib.pyplot as plt
import numpy as np


