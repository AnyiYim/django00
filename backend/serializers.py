# 改文件进行 backend 应用下 model 的序列化配置
from rest_framework import serializers
from backend.models import Person


# class PersonSerialzer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=False, max_length=30)
#     age = serializers.IntegerField()

class PersonSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'age')

    def create(self, validated_data):
        """
        序列化创建
        :param validated_data: 传入值
        :return: 创建model
        """
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        更新序列化值
        :param instance: model实例
        :param validated_data: 传入值
        :return: 实例
        """
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


