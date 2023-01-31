from rest_framework import generics
from .serializers import WizardSerializer
from .models import Wizard

# Create your views here.
class WizardList(generics.ListCreateAPIView):
  queryset = Wizard.objects.all()
  serializer_class = WizardSerializer



class WizardDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Wizard.objects.all()
  serializer_class = WizardSerializer
