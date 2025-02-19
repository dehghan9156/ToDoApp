from django.template.context_processors import request
from rest_framework import serializers
from ...models import ToDo,User
from django.urls import reverse


class ToDoSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    username = serializers.CharField(source='show_username',read_only=True)
    class Meta:
        model = ToDo
        fields = ['id','user','username', 'title','absolute_url','complate', 'created_date']
        read_only_fields = ['user','username']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        # print(request.__dict__)
        rep=super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_url')
        return rep