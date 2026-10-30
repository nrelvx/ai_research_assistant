from pydantic import BaseModel, Field, HttpUrl

# Create article
class ArticleCreate(BaseModel):
    title: str
    url: HttpUrl
    category: str = Field(min_length=3, max_length=30)
    notes: str | None = Field(
        default=None,
        max_length=100, 
        description="Notes must not exceed 100 characters"
        )

# Get Article
class ArticleResponse(BaseModel):
    id: int
    title: str
    url: HttpUrl
    category: str
    notes: str | None 

# Update Article
class ArticleUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    url: HttpUrl | None
    category: str | None = Field(default=None, min_length=3, max_length=30)
    notes: str | None = Field(
        default=None,
        max_length=100, 
        description="Notes must not exceed 100 characters"
        )