from fastapi import FastAPI
import uvicorn
import schemas

app = FastAPI()
articles = []
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
@app.post("/articles", tags=["Articles"])
async def create_article(article: schemas.ArticleCreate):
    articles.append(article)
    return article


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
    
