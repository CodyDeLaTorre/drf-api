from rest_framework import serializers
from .models import Wizard


class WizardSerializer(serializers.ModelSerializer):

  class Meta:
    fields = ('id', 'creator', 'name', 'source', 'weapon', 'description', 'created_at')
    model = Wizard
