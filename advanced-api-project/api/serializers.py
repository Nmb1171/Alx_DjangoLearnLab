from rest_framework import serializers
from .models import Author, Book 
from datetime import datetime, date

class BookSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        from datetime import date
        print(f"Debug: Incoming value for publication_year: {value}")
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        publication_year = representation.get('publication_year')
        if isinstance(publication_year, (date, datetime)):
            representation['publication_year'] = publication_year.year
        return representation

        

    
    

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
    
