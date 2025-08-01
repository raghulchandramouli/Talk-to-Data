import google.generativeai as genai
from decouple import config
from django.apps import apps
import numpy as np
import ast

# from PgVector Imports
from pgvector.django import CosineDistance
from django.db.models import F

EMBEDDING_LENGTH = config("EMBEDDING_LENGTH", default=768, cast=int)
EMBEDDING_MODEL  = config("EMBEDDING_MODEL",  default='embedding-001')
 
genai.configure(
    api_key=config("GEMINI_API_KEY")
)

def get_embedding(text, model="models/embedding-001"):
    text = text.replace("\n", " ").strip()
    response = genai.embed_content(
        model=model,
        content=text,
        task_type="retrieval_document"
    )
    return response['embedding']


def get_query_embedding(text):
    # get the embedding for the query:
    return get_embedding(text)

import ast
import numpy as np

def search_posts(query, limit = 2):
    BlogPost = apps.get_model(app_label  = 'blog',
                              model_name = 'BlogPost')
        
    query_embedding = get_query_embedding(query)
    
    # Get all blog posts
    blog_posts = BlogPost.objects.all()
    
    # Calculate similarities manually since we're using TextField
    results = []
    for post in blog_posts:
        if post.embedding:
            try:
                # Convert string embedding back to list
                post_embedding = ast.literal_eval(post.embedding)
                
                # Calculate cosine similarity
                similarity = cosine_similarity(query_embedding, post_embedding)
                
                results.append({
                    'post': post,
                    'similarity': similarity,
                    'distance': 1 - similarity
                })
            except (ValueError, SyntaxError):
                # Skip posts with invalid embeddings
                continue
    
    # Sort by similarity (highest first) and take top results
    results.sort(key=lambda x: x['similarity'], reverse=True)
    
    # Create a custom queryset-like object
    class SimilarityResult:
        def __init__(self, post, similarity, distance):
            self.post = post
            self.similarity = similarity
            self.distance = distance
            
        def __getattr__(self, name):
            # Delegate to the actual post object
            return getattr(self.post, name)
    
    # Create a list-like object that mimics QuerySet behavior
    class SimilarityQuerySet:
        def __init__(self, results):
            self.results = results
            
        def first(self):
            return self.results[0] if self.results else None
            
        def __getitem__(self, index):
            return self.results[index]
            
        def __len__(self):
            return len(self.results)
            
        def __iter__(self):
            return iter(self.results)
    
    return SimilarityQuerySet([SimilarityResult(r['post'], r['similarity'], r['distance']) for r in results[:limit]])

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors"""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0
    
    return dot_product / (norm1 * norm2)