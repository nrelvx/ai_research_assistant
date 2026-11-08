from fastapi import Depends, FastAPI, HTTPException
import uvicorn
import schemas
import models
from db import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Assistant", description="An AI assistant for research and article management.", version="1.0.0")

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home page
@app.get("/")
async def home():
    return {"message": "AI Assistant is running"}

# Articles
@app.get("/articles",response_model=list[schemas.ArticleResponse], tags=["Articles"])
async def get_articles(db: Session = Depends(get_db)):
    articles = db.query(models.Article).all()
    return articles

# Article by ID
@app.get("/articles/{article_id}", response_model=schemas.ArticleResponse, tags=["Articles"])
async def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

# Create Article
@app.post("/articles", response_model=schemas.ArticleResponse)
async def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(
        title=article.title,
        url=str(article.url),
        category=article.category,
        notes=article.notes
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    return db_article

# Update Article
@app.patch("/articles/{article_id}", response_model=schemas.ArticleResponse)
async def update_article(article_id: int, article_update: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")

    update_data = article_update.model_dump(exclude_unset=True)
    # Convert HttpUrl to string if present
    if "url" in update_data and update_data["url"] is not None:
        update_data["url"] = str(update_data["url"])

    for key, value in update_data.items():
        setattr(db_article, key, value)

    db.commit()
    db.refresh(db_article)
    return db_article

# Delete Article
@app.delete("/articles/{article_id}")
async def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")

    db.delete(db_article)
    db.commit()
    return db_article

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
    
