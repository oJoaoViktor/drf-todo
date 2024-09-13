#Serializer
"""
- Responsável por converter dados complexos, como objetos do modelo Django em formatos JSON
- Valida os dados recebidos para garantir que sejam salvos da forma correta no DB
- Pode ser comparado com o Forms
"""
#Forms x Serializer
"""
Forms:
    - Usado para lidar com dados em páginas web (HTML), validando entradas de usuários e gerando formulários
    - Lida com HTML e POST request de formulário
    - Retorna erro de validação em página HTML

Serializer:
    - Usado em API para converter dados entre JSON (ou outro formato) e objetos do Django, além de validar esses dados
    - Lida com JSON (ou XML) em APIs
    - Retorna erro em JSON com status de erro
"""

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

"""
Quando utilizar campos personalizados:   
    - Se o usuário não precisa preencher
    - Se o usuário não precisa visualizar
    - Se o campo é criado de forma automática
    - Se o campo não é necessário em uma listagem (Otimização)
    - Se o campo contém um dado sensível (Ex:senha)
"""