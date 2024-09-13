from .formatters import format_datetime
from .models import Item, TaskList
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    completion_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Item
        #Para incluir todos os campos do modelo
        fields = "__all__"
    
    def get_completion_date(self, obj):
        if obj.completion_date:
            return format_datetime(obj.completion_date)
        return None
        
class TaskListSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = TaskList
        #Para incluir campos personalizados
        # fields = ["name"] #Caso utilize mais campos -> ["name","name1","name2"]
        fields = "__all__"
    
    def get_created_at(self, obj):
        return format_datetime(obj.created_at)