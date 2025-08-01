from django.db import models
# from pgvector.django import VectorField  # Temporarily commented out for SQLite compatibility
from . import services

# EMBEDDING_MODEL = "embedding-001"
EMBEDDING_LENGTH = services.EMBEDDING_LENGTH
# Create your models here.
class BlogPost(models.Model):
    
    # id -> models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    _content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # embedding's - temporarily using TextField for SQLite compatibility
    # embedding = VectorField(dimensions=768, null=True)  # Original line
    embedding = models.TextField(null=True, blank=True)  # Temporary solution for SQLite
    
    # delete operations:
    can_delete = models.BooleanField(default=False, help_text='Used in jupyter notebook')
    
    
    def save(self, *args, **kwargs):
        
        has_changed = False
        if self._content != self.content:
            has_changed = True 
        if (self.embedding is None) or has_changed == True:
            
            raw_embedding_text = self.get_embedding_text_raw()
            if raw_embedding_text is not None:
                try:
                    embedding_vector = services.get_embedding(raw_embedding_text)
                    # Convert embedding list to string for TextField storage
                    self.embedding = str(embedding_vector)
                except Exception as e:
                    print(f"Error generating embedding: {e}")
                    # Set a default value if embedding fails
                    self.embedding = "[]"
    
        super().save(*args, **kwargs) 
        
    def get_embedding_text_raw(self):
        return self.content
    
    
    