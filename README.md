# TravelGo 🌍

A gamified travel platform where tourists explore attractions, share experiences, compete on leaderboards, and connect with fellow travellers. This repository contains the software architecture analysis, proof-of-concept implementation, and supporting documentation produced by Team 11.


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Running Experiments](#running-experiments)
- [Tech Stack](#tech-stack)


## Overview

TravelGo lets tourists tick attractions off their bucket list in a competitive, social way. Users earn points by visiting attractions and sharing posts, redeem those points for discounts or souvenirs at local businesses, and compete to top a global leaderboard. The platform also surfaces a community chat so travellers can meet like-minded individuals on the road.

This repository covers the full software architecture lifecycle: problem analysis, architecture design (using C4 and UML diagrams), a working proof-of-concept (PoC), and a written report with experiments validating scalability and modularity.


## Features

| Feature | Description |
|---|---|
| Interactive Map | Browse tourist attractions with coordinates via an integrated map view |
| Posts | Share travel experiences tied to specific attractions |
| Leaderboard | Real-time ranking of users by points earned from posts |
| Chat | Community messaging for travellers |
| User Profiles | Register users and track their activity |
| Points & Rewards | Earn points per post; redeem for discounts or souvenirs |


## Architecture

TravelGo uses a **microservices architecture** with event-driven communication via Apache Kafka. All client traffic enters through a single **API Gateway**, behind an **Nginx** load balancer, and is routed to one of six independent services.

```
Browser / Client
      │
   Nginx (Load Balancer)  :5000
      │
  API Gateway             :5000
      │
  ┌───┴──────────────────────────────────────┐
  │                                          │
User Service   Post Service   Leaderboard   Chat Service   Map Service
  :5001          :5002         Service        :5004          :5005
                               :5003
                  │               ▲
                  └── Kafka ──────┘
                  (new_post topic)
```

### Services

| Service | Port | Responsibility |
|---|---|---|
| `frontend_service` | 5008 | Serves HTML templates; calls API Gateway for all data |
| `api_gateway` | 5000 | Single entry point; routes requests to downstream services |
| `user_service` | 5001 | User registration and profile management |
| `post_service` | 5002 | Create and retrieve travel posts; publishes `new_post` events to Kafka |
| `leaderboard_service` | 5003 | Consumes Kafka events; calculates and exposes user rankings |
| `chat_service` | 5004 | Community messaging; listens for post events to surface activity |
| `map_service` | 5005 | Returns static attraction data with coordinates |

### Event Bus

The **Post Service** publishes a `new_post` event to a Kafka topic whenever a user creates a post. The **Leaderboard Service** subscribes to that topic and awards points (+10 per post) asynchronously — decoupling score calculation from post creation.

An in-process `event_bus.py` module (publish/subscribe) is also present for lightweight, non-Kafka event handling within the PoC.


## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Python 3.x (for running load tests locally)

### Navigate to the PoC directory

```bash
cd poc
```

### (Optional) Local Virtual Environment

**macOS / Linux**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows**
```bash
pip install virtualenv
python -m virtualenv vEnv
vEnv\Scripts\activate
pip install -r requirements.txt
```

### Run with Docker

```bash
docker compose up --build
```

This starts all services: Nginx, API Gateway, all microservices, Kafka, and Zookeeper.

### Open the App

```
http://127.0.0.1:5008
```


## Running Experiments

### Modularity — Independent Service Shutdown

Each service can be stopped and restarted in isolation, demonstrating that the rest of the system continues functioning:

```bash
# Stop a service
docker compose stop leaderboard_service

# Restart it
docker compose start leaderboard_service
```

Replace `leaderboard_service` with any service name (e.g. `chat_service`, `map_service`).

### Scalability — Load Testing with Locust

**1. Scale the API Gateway horizontally:**
```bash
docker compose up -d --scale api_gateway=3
```

**2. Install Locust:**
```bash
pip install locust
```

**3. Run the load test (from the `poc/` folder):**
```bash
locust -f load-tests/locustfile.py --host=http://localhost:5000
```

**4.** Open [http://localhost:8089](http://localhost:8089) in your browser. Set **Users: 1000**, **Spawn rate: 100**.

**5. Scale individual services under load:**
```bash
docker compose up --scale chat_service=10 -d
```

**6. Tear down:**
```bash
docker compose down
```


## Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3 |
| **Web Framework** | Flask |
| **Templating** | Jinja2 |
| **Message Broker** | Apache Kafka + Zookeeper (Confluent 7.4.4) |
| **Load Balancer** | Nginx |
| **Containerisation** | Docker, Docker Compose |
| **Load Testing** | Locust |
| **ORM (dependency)** | SQLAlchemy / Flask-SQLAlchemy |
| **CI/CD** | GitLab CI |
| **Diagramming** | C4 Model (Context, Container, Component), UML, Wardley Map |


## Further Reading

- Full architecture report: [`report/Team_11_Final_Report.md`](report/Team_11_Final_Report.md)
- Personas, user stories, and architectural pattern catalogue: [`appendix/Team_11_Appendix.md`](appendix/Team_11_Appendix.md)
