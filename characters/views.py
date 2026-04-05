import random

from django.http import HttpRequest
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, OpenApiExample

from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Character
from .pagination import CharacterListPagination
from .serializers import CharacterSerializer
from drf_spectacular.views import extend_schema

@extend_schema(
    methods=["GET"],
    summary="Get a random character",
    description="Returns a random character from Rick and Morty movie.",
    responses={HTTP_200_OK: CharacterSerializer},
)
@api_view(["GET"])
def get_random_character_view(request: HttpRequest):
    character_pk_list = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(character_pk_list)

    character = Character.objects.get(pk=random_pk)

    serializer = CharacterSerializer(character)

    return Response(serializer.data, status=HTTP_200_OK)


class CharacterList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = CharacterListPagination

    def get_queryset(self):
        query = self.request.query_params.get("query")

        if not query:
            raise ValueError("Query parameter is required")

        self.queryset = self.queryset.filter(name__icontains=query)

        return self.queryset

    @extend_schema(
        methods=["GET"],
        summary="Get a list of characters",
        description="Returns a list of characters from Rick and Morty movie.",
        responses={HTTP_200_OK: CharacterSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                name="query",
                type=OpenApiTypes.STR,
                description="Search query for characters",
                required=True,
                examples=[
                    OpenApiExample(
                        name='None',
                        value=None,
                    ),
                    OpenApiExample(
                        name="Rick query",
                        value="Rick",
                        summary="Search for characters with the name containing 'Rick'"
                    ),
                    OpenApiExample(
                        name="Morty query",
                        value="Morty",
                        summary="Search for characters with the name containing 'Morty'"
                    )
                ]
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
