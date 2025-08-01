import google.generativeai as genai
from decouple import config

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