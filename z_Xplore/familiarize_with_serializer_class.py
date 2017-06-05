# This Python file uses the following encoding: utf-8
# !/usr/bin/env python
import os

import django
import sys

sys.path.append("/home/ubuntu/drf_tutorials")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_tutorials.settings")
django.setup()
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
import logging

log = logging.getLogger(__name__)

FLOAT_DATA_FORMAT = '{:,.2f}'

if __name__ == "__main__":
    if True:
        # snippet = Snippet(code='foo = "bar"\n')
        # snippet.save()
        #
        snippet = Snippet(code='print "goodbye, world again"\n')
        snippet_to_update = Snippet.objects.get(id=9)

        # snippet.save()

        serializer = SnippetSerializer(snippet)
        # SnippetSerializer.update(snippet_to_update, snippet)
        # print(serializer.data)

        content = JSONRenderer().render(serializer.data)
        print(content)

        print('---------------------------')

        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        print(data)

        serializer = SnippetSerializer(data=data)
        print(serializer.is_valid())
        print(serializer.validated_data)
        # serializer.save()

        # serializer_all = SnippetSerializer(Snippet.objects.all(), many=True)
        # print(serializer_all)
    else:
        serializer = SnippetSerializer()
        print(repr(serializer))
