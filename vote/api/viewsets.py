from rest_framework import viewsets
from vote.api import serializers
from vote import models

class VoteViewsets(viewsets.ModelViewSet):
  serializer_class = serializers.VoteSerializer
  queryset = models.Vote.objects.all()