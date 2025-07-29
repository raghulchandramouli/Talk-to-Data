from django.db import models
from pgvector.django import VectorField


EMBEDDING_MODEL = "embedding-001"
EMBEDDING_LENGTH = 384
# Create your models here.
class BlogPost(models.Model):
    
    # id -> models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # embedding's 
    embedding = VectorField(dimensions=768, null=True)
    
    # delete operations:
    can_delete = models.BooleanField(default=False, help_text='Used in jupyter notebook')
    
    def get_embedding_text_raw(self):
        return self.content
    
    
    