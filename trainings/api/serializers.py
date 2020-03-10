from rest_framework.serializers import Serializer, CharField


class TrainingsSerializer(Serializer):
    name = CharField(max_length=50)
    channel_key = CharField(max_length=50)
