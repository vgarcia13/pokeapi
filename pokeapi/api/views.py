import csv
import json

from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@permission_classes((AllowAny,))
class PokeApiViewSet(viewsets.GenericViewSet):
    """
    API endpoint that returns pokemons filtered by an input called "filter"
    """

    def list(self, request):
        filter = request.GET.get('filter')
        filename = request.GET.get('filename')

        valid_pokemons = []

        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                is_valid = True if filter in row.get('NAME') else False
                if is_valid:
                    valid_pokemons.append(row.get('NAME'))

        return Response(json.loads(json.dumps(valid_pokemons)), status=status.HTTP_200_OK)
