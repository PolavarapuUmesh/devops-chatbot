# Docker Compose Demo Project

This project demonstrates a multi-container application using Docker Compose. It includes:

1. React Frontend
2. FastAPI Backend
3. MongoDB Database
4. Redis Cache

## Project Structure
```
docker-compose-demo/
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       └── App.js
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    └── main.py
```

## Services

### Frontend (React)
- Port: 3000
- Features:
  - Material-UI interface
  - Task creation form
  - Task list display
  - Real-time updates

### Backend (FastAPI)
- Port: 8000
- Features:
  - RESTful API endpoints
  - MongoDB integration
  - Redis caching
  - Async operations

### MongoDB
- Port: 27017
- Persistent storage for tasks
- Uses Docker volume

### Redis
- Port: 6379
- Caches task data
- Improves read performance

## How to Use

1. Start the services:
   ```bash
   docker-compose up --build
   ```

2. Access the applications:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

3. Stop the services:
   ```bash
   docker-compose down
   ```

## Docker Compose Features Demonstrated

1. **Multi-container orchestration**
   - Manages multiple services
   - Handles dependencies
   - Network configuration

2. **Volume management**
   - Persistent data storage
   - Development hot-reloading

3. **Environment variables**
   - Service configuration
   - Cross-service communication

4. **Port mapping**
   - Container-to-host networking
   - Service discovery

5. **Build configuration**
   - Custom Dockerfiles
   - Build context
   - Development optimizations

## Development Workflow

1. Make changes to the code
2. Docker Compose will automatically reload:
   - Frontend changes (React hot-reload)
   - Backend changes (uvicorn --reload)
   - Database persists between restarts

## Best Practices Demonstrated

1. **Separation of concerns**
   - Each service in its own container
   - Clear service boundaries

2. **Development optimization**
   - Volume mounts for hot-reloading
   - Cached dependencies

3. **Production readiness**
   - Multi-stage builds
   - Environment configuration
   - Persistent data handling
