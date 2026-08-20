# Deployment Instructions

## Run the Django server locally
```bash
cd server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## cURL Commands

### Login
```bash
curl -X POST http://localhost:8000/djangoapp/login/ -H "Content-Type: application/json" -d "{\"userName\":\"testuser\", \"password\":\"testpass\"}"
```

### Logout
```bash
curl -X POST http://localhost:8000/djangoapp/logout/
```

### Get all dealers
```bash
curl http://localhost:3030/dealers
```

### Get dealer by ID
```bash
curl http://localhost:3030/dealers/1
```

### Get dealers by state=Kansas
```bash
curl http://localhost:3030/dealers?state=Kansas
```

### Get dealer reviews
```bash
curl http://localhost:3030/reviews/1
```

### Get all car makes
```bash
curl http://localhost:3030/cars
```

### Sentiment analysis on "Fantastic services"
```bash
curl "http://localhost:5000/analyze?text=Fantastic%20services"
```

## Docker Build/Run Commands
```bash
# Django Server
cd server
docker build -t django-server .
docker run -p 8000:8000 django-server

# Database Microservice
cd database
docker build -t node-database .
docker run -p 3030:3030 node-database

# Sentiment Analyzer
cd sentiment_analyzer
docker build -t sentiment-analyzer .
docker run -p 5000:5000 sentiment-analyzer
```

## GitHub Actions Trigger Instructions
1. Push any commit to the `main` branch.
2. Go to the "Actions" tab in your GitHub repository to view the CI/CD pipeline execution logs.

## IBM Cloud Code Engine Deploy Commands
```bash
# Login to IBM Cloud
ibmcloud login

# Target the Code Engine project
ibmcloud ce project select --name my-project

# Deploy Database Microservice
ibmcloud ce application create --name database --image <your-registry>/node-database:latest --port 3030

# Deploy Sentiment Analyzer
ibmcloud ce application create --name sentiment-analyzer --image <your-registry>/sentiment-analyzer:latest --port 5000

# Deploy Django Backend
ibmcloud ce application create --name django-server --image <your-registry>/django-server:latest --port 8000
```
