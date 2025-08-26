## Order Yangu 
#### Order & Payment Microservices
Order-Yangu is an e-commerce backend built with microservices. The order-service handles order creation and management, while the payment-service processes transactions. Services communicate asynchronously for scalability.



### Repository Structure
├── orders-service/          # Order management microservice
│   ├── src/
│   └── Dockerfile
├── payments-service/        # Payment processing microservice
│   ├── src/
│   └── Dockerfile
├── docker-compose.yml       
├── .dockerignore
├── .gitignore
├── LICENSE (MIT, you can fork this, for research or)
└── README.md

### Tech Stack
## Features
*   Framework: fast-api [python].
*   Inter-Service Communication: [REST APIs / RabbitMQ ]
*   Data Storage: Google Firestore
*   Containerization: Docker
*   Orchestration: Docker Compose (for local dev), gloud (for prod)

