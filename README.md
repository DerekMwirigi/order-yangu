## Order Yangu 
#### Order & Payment Microservices
Order-Yangu is an e-commerce backend built with microservices. The order-service handles order creation and management, while the payment-service processes transactions. Services communicate asynchronously for scalability.


### Repository Structure
```bash
├── orders-service/          # Order management microservice
│   ├── app/
│   └── Dockerfile
│   └── run_app.sh
│   └── docker/              # Stacks yml files anf firestore Dockerfile to maintain a managed emulator eimage
│   ├── tests/
├── payments-service/        # Payment processing microservice
│   ├── app/
│   └── Dockerfile
│   └── run_app.sh
│   └── docker/              # Stacks yml files anf firestore Dockerfile to maintain a managed emulator eimage
│   ├── tests/
├── .github/
│   ├── workflows/  
├── docker-compose.yml       
├── .dockerignore
├── .gitignore
├── .design-1.png
├── LICENSE (MIT, you can fork this, for research or)
└── README.md
```

### Tech Stack
## Features
*   Framework: fast-api [python].
*   Inter-Service Communication: [REST APIs / RabbitMQ ]
*   Data Storage: Google Firestore
*   Containerization: Docker
*   Orchestration: Docker Compose (for local dev), gloud (for prod)


### API Docs
Detailed API documentation is provided via Swagger UI when the services are running
*   Orders Service: http://localhost:8001/docs
*   Payments Service: http://localhost:8002/docs
