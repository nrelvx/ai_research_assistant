from fastapi import FastAPI
import uvicorn
import app.schemas

app = FastAPI()

# Home page
@app.get("/")
async def home():
    return {"message": "AI Assistant is running"}

# Articles
articles = []
@app.get("/articles", tags=["Articles"])
async def get_articles():
    return articles


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
    
