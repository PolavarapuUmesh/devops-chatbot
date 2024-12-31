from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv
import base64
from PIL import Image
import io
import json
import re

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize OpenAI client (commented out for testing)
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_error(error_message: str) -> str:
    # Mock response for testing
    return f"""
## Error Analysis
1. Root cause: This is a test response
2. Solution: Testing the server connection
3. Prevention: Make sure the server is running properly

Original error: {error_message}
"""

def analyze_image(image_data: bytes) -> str:
    # Mock response for testing
    return """
## Image Analysis
1. This is a test response for image analysis
2. The server is working properly
3. You can now implement the actual OpenAI integration
"""

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: str = Form(...), image: UploadFile = File(None)):
    try:
        # Check if an image was uploaded
        if image:
            contents = await image.read()
            response = analyze_image(contents)
            return {"response": response}
        
        # Check if the message contains an error (look for common error patterns)
        if any(keyword in message.lower() for keyword in ["error", "exception", "failed", "traceback", "errno"]):
            response = analyze_error(message)
        else:
            # Use the default DevOps response system for non-error queries
            response = """
## Default Response
1. This is a test response for non-error queries
2. The server is working properly
3. You can now implement the actual OpenAI integration
"""
            response = response
            
        return {"response": response}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
