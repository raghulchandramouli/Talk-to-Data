# Talk-to-Data

A Django-based application that enables semantic search and data retrieval using AI embeddings. This project combines Django with Google's Gemini AI to provide intelligent search capabilities for blog posts and products.

## 🚀 Features

- **Semantic Search**: Advanced search functionality using AI embeddings
- **Blog Management**: Create, manage, and search through blog posts
- **Product Catalog**: Manage products with intelligent search capabilities
- **AI-Powered Embeddings**: Uses Google Gemini AI for generating embeddings
- **Vector Similarity Search**: Find similar content using cosine similarity
- **Jupyter Notebook Integration**: Interactive notebooks for data exploration and testing

## 🏗️ Architecture

### Core Components

- **Django Backend**: Main web framework
- **Blog App**: Handles blog post creation and semantic search
- **Products App**: Manages product catalog with embedding capabilities
- **Embedding Services**: AI-powered text embedding generation
- **Vector Search**: Similarity-based content retrieval

### Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL with pgvector (production)
- **AI/ML**: Google Gemini AI for embeddings
- **Vector Operations**: pgvector for PostgreSQL, numpy for SQLite
- **Configuration**: python-decouple for environment management

## 📋 Prerequisites

- Python 3.8+
- pip
- Google Gemini API key
- PostgreSQL with pgvector extension (for production)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Talk-to-Data
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
# Django Settings
DJANGO_DEBUG=True
SECRET_KEY=your-secret-key-here

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Google Gemini AI
GEMINI_API_KEY=your-gemini-api-key-here

# Embedding Configuration
EMBEDDING_MODEL=embedding-001
EMBEDDING_LENGTH=768
```

### 5. Database Setup

```bash
cd src
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## 🚀 Usage

### Running the Development Server

```bash
cd src
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### Admin Interface

Access the Django admin at `http://localhost:8000/admin` to manage:
- Blog posts
- Products
- Embeddings

### Jupyter Notebooks

The `nbns/` directory contains interactive notebooks for:
- **Django_to_LlamaIndex.ipynb**: Integration with LlamaIndex
- **connecting_django.ipynb**: Django connection examples
- **search_services.ipynb**: Search functionality testing
- **Embeddings.ipynb**: Embedding generation and testing

To run notebooks:

```bash
cd nbns
jupyter notebook
```

## 🔍 API Endpoints

### Blog Posts

- `GET /admin/blog/blogpost/` - List all blog posts
- `POST /admin/blog/blogpost/add/` - Create new blog post
- Search functionality available through Django ORM

### Products

- `GET /admin/products/product/` - List all products
- `POST /admin/products/product/add/` - Create new product

## 🔧 Configuration

### Embedding Settings

The application supports configurable embedding parameters:

- `EMBEDDING_MODEL`: Google Gemini model name (default: 'embedding-001')
- `EMBEDDING_LENGTH`: Vector dimensions (default: 768)

### Database Configuration

- **Development**: SQLite with manual similarity calculation
- **Production**: PostgreSQL with pgvector extension for optimized vector operations

## 📊 Models

### BlogPost Model

```python
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = models.TextField(null=True, blank=True)
    can_delete = models.BooleanField(default=False)
```

### Product Model

```python
class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding_obj = GenericRelation(Embedding)
    can_delete = models.BooleanField(default=False)
```

## 🔍 Search Functionality

### Semantic Search

The application provides semantic search capabilities using cosine similarity:

```python
# Search for similar blog posts
results = BlogPost.objects.search_posts("your query", limit=5)

# Using the service directly
from blog.services import search_posts
results = search_posts("your query", limit=5)
```

### Embedding Generation

Embeddings are automatically generated when content is saved:

```python
# Create a new blog post (embedding generated automatically)
post = BlogPost.objects.create(
    title="Sample Post",
    content="Your content here"
)
```

## 🧪 Testing

### Running Tests

```bash
cd src
python manage.py test
```

### Interactive Testing

Use the Jupyter notebooks in the `nbns/` directory for interactive testing and exploration.

## 🚀 Deployment

### Production Setup

1. **Database**: Use PostgreSQL with pgvector extension
2. **Environment Variables**: Configure all required environment variables
3. **Static Files**: Collect and serve static files
4. **Security**: Set `DEBUG=False` and configure proper `SECRET_KEY`

### Environment Variables for Production

```env
DJANGO_DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:password@host:5432/dbname
GEMINI_API_KEY=your-gemini-api-key
EMBEDDING_MODEL=embedding-001
EMBEDDING_LENGTH=768
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for embedding capabilities
- Django community for the excellent web framework
- pgvector for PostgreSQL vector operations

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the Jupyter notebooks for examples
- Review the Django admin interface for data management

---

**Note**: This project is designed for educational and research purposes. Ensure you have proper API keys and follow Google's usage policies for Gemini AI.
