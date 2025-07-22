from django.db import models
from pgvector.django import VectorField


EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_LENGTH = 1536
# Create your models here.
class BlogPost(models.Model):
    
    # id -> models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # embedding's 
    embedding = VectorField(dimensions=384, null=True)
    