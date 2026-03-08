import random

from django.http import HttpRequest

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Character
from .serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character_view(request: HttpRequest):
    character_pk_list = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(character_pk_list)

    character = Character.objects.get(pk=random_pk)

    serializer = CharacterSerializer(character)

    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        query = self.request.query_params.get("query")

        if not query:
            raise ValueError("Query parameter is required")

        self.queryset = self.queryset.filter(name__icontains=query)

        return self.queryset
