from fastapi import FastAPI, HTTPException
import uvicorn
import schemas
import models
from db import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Assistant", description="An AI assistant for research and article management.", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
next_id = 1

# Home page
@app.get("/")
async def home():
    return {"message": "AI Assistant is running"}

# Articles
@app.get("/articles", tags=["Articles"])
async def get_articles():
    return articles

# Create Article
@app.post("/articles", response_model=schemas.ArticleResponse, tags=["Articles"])
async def create_article(article: schemas.ArticleCreate):
    global next_id
    
    new_article = schemas.ArticleResponse(
        id=next_id,
        **article.model_dump()
    )
    next_id += 1

    articles.append(new_article)
    return new_article

# Update Article
@app.patch("/articles/{article_id}", tags=["Articles"])
async def update_article(article_id: int, article_update: schemas.ArticleUpdate):
    # Search for the article by ID
    for art in articles:
        if art.id == article_id:

            # Get only the fields that were provided in the request body
            update_data = article_update.model_dump(exclude_unset=True)

            # Update the article with the provided fields
            for key, value in update_data.items():
                setattr(art, key, value)
            return art
    raise HTTPException(status_code=404, detail="Article not found")

# Delete Article
@app.delete("/articles/{article_id}", tags=["Articles"])
async def delete_article(article_id: int):

    for art in articles:
        if art.id == article_id:
            articles.remove(art)
            return {"message": "Article deleted successfully"}

    raise HTTPException(status_code=404, detail="Article not found")


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
    
