from rest_framework import generics
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import traceback
from w2d.find_domains import find_domains


class WordListEN(generics.ListAPIView):
    queryset = models.WordCollectionEN.objects.all()
    serializer_class = serializers.WordCollectionENSerializer


class WordDetailEN(generics.RetrieveAPIView):
    queryset = models.WordCollectionEN.objects.all()
    serializer_class = serializers.WordCollectionENSerializer


@api_view(['GET'])
def get_domains(request):
    collection = request.GET.get('c')
    domain_ext = request.GET.get('ext')

    collection_data = {}

    response = {
        "flag": 0,
        "collection": collection,
        "domain_ext": domain_ext,
        "domains": None,
    }
    domains = {}
    try:
        if collection == 'en':  # English dictionary
            collection_instance = models.WordCollectionEN.objects.all()
            collection_data = serializers.WordCollectionENSerializer(collection_instance, many=True).data
        #
        domains = find_domains(collection_data, domain_ext)

        response["flag"] = 1
        response["domains"] = domains
    except Exception as e:
        response["message"] = str(e)
        response["error"] = traceback.format_exc()

    return Response(response)
