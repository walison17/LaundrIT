from django.forms import ModelForm
from django.contrib.auth.hashers import make_password
from django.db import transaction

from Home.models import Cliente
from  .models import Servico
