# Team 11: TravelGo
The proof of concept demonstrates the technical feasibility of the platform’s microservices-based architecture and to validate its core design principles; scalability, and modularity. The PoC serves as a minimal yet functional version of the TravelGo system, simulating the interaction between key components such as the post service, leaderboard service, and chat service, all coordinated through a load balancer, an API Gateway and an event-driven communication model.


### Clone the repository
```
git clone https://gitlab.ewi.tudelft.nl/cs4505/2025-2026/team-11.git
cd poc
```

### Create virtual environment
For Mac/Linux
```
python -m venv venv
source venv/bin/activate
```

For Windows
```
pip install virtualenv
python -m virtualenv vEnv
vEnv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the application using docker
```
docker compose up --build
```

### Open the application
```
http://127.0.0.1:5008
```

### Experiment Setup - Modularity
To ensure modularity, each service can be independently shut off using the command:
```
docker compose stop leaderboard_service
```
Furthermore, the service can be started up again using the command:
```
docker compose start leaderboard_service
```
Similarly, these commands can be applied to any service.

### Experiment Setup - Scalability (Locust)

Install locust using the following command:
```
pip install locust
```
Make sure your docker desktop is open and run this command in the poc folder : 

```
docker compose up -d --scale api_gateway=3 -d
```
In a new terminal, run the command after navigating to the poc folder: 

```
locust -f load-tests/locustfile.py --host=http://localhost:5000
```
Open http://localhost:8089/ to see locust hosted. Set number of users to 1000 and Swarms as 100 (just default for this experiment)

To implement scaling and create replicas: 

```
docker compose up --scale chat_service=10 -d
```

To stop the containers, run the following command:

```
docker compose down
```
