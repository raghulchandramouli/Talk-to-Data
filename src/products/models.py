# Create your models here.
from django.db import models
from pgvector.django import VectorField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


EMBEDDING_MODEL = "embedding-001"
EMBEDDING_LENGTH = 384


class Embedding(models.Model):
    embedding      = VectorField(dimensions=EMBEDDING_LENGTH,
                                 blank=True,
                                 null=True)
    
    object_id      = models.PositiveIntegerField()
    content_type   = models.ForeignKey(ContentType,
                                     on_delete=models.SET_NULL,
                                     null=True)
    
    content_object =  GenericForeignKey('content_type',
                                        'object_id')
# Create your models here.
class Product(models.Model):
    
    # id -> models.AutoField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding_obj = GenericRelation(Embedding)
    
    # delete operations:
    can_delete = models.BooleanField(default=False, help_text='Used in jupyter notebook')
    
    def get_embedding_text_raw(self):
        return self.content
    
    
    