from rest_framework import serializers
from .models import Item, TaskList

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #Para incluir todos os campos do modelo
        fields = "__all__"
        
class TaskListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = TaskList
        #Para incluir campos personalizados
        fields = ["name"] #Caso utilize mais campos -> ["name","name1","name2"]