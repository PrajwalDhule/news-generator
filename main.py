import json
from typing import Union
from basic_research_workflow_agent import AgnoAgent, translate_text
from fastapi import FastAPI

app = FastAPI()

@app.get("")
def read_root():
    return {"Hello": "World"}

@app.get("/news")
def get_news():
    agno_agent = AgnoAgent()
    original_news = agno_agent.get_news()
    print(json.dumps(original_news, indent=4))

    translated_text = translate_text(original_news, ["hi-IN"])

    news_with_translations = {
        "title": original_news["title"],
        "description": original_news["description"],
        "source_links": original_news["source_links"],
        "translations": translated_text
    }
    print("news: ", news_with_translations)
    
    return news_with_translations
