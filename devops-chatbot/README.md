# DevOps Chatbot

A simple chatbot that helps with DevOps-related queries. The chatbot uses OpenAI's GPT model to provide helpful responses about various DevOps topics including CI/CD, containerization, cloud platforms, and more.

## Features

- Interactive web interface
- Real-time chat functionality
- Expertise in various DevOps topics:
  - CI/CD pipelines
  - Docker and containerization
  - Kubernetes
  - Infrastructure as Code
  - Cloud platforms (AWS, GCP, Azure)
  - Monitoring and logging
  - Security best practices

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

6. Open your browser and navigate to `http://localhost:8000`

## Technologies Used

- Backend: FastAPI
- Frontend: HTML, JavaScript, TailwindCSS
- AI: OpenAI GPT-3.5
