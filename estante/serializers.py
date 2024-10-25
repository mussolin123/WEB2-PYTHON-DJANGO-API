from rest_framework import serializers
from .models import Autor, Livro, LivroTag

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroTag
        fields = ['tag']

class LivroAutorSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    tags = LivroTagSerializer(many=True, write_only=True)

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'ano_publicacao', 'descricao', 'autor', 'tags']

    
    def create(self, validated_data):
        autor_data = validated_data.pop('autor')
        autor, created = Autor.objects.get_or_create(**autor_data)

        tags_data = validated_data.pop('tags', [])

        
        # Criar o livro associado ao autor
        livro = Livro.objects.create(autor=autor, **validated_data)

        for tag_data in tags_data:
            LivroTag.objects.create(livro=livro, tag=tag_data['tag'])

        return livro
