# Team 11: TravelGo
The proof of concept demonstrates how the platform can bring together travelers and tourism industry workers in one ecosystem. It validates core features such as interactive maps, attraction discovery, user-generated content, and gamification elements like leaderboards. The POC was developed to demonstrate the technical feasibility of the platform’s microservices-based architecture and to validate its core design principles; scalability, modularity, and reliability. The PoC serves as a minimal yet functional version of the TravelGo system, simulating the interaction between key components such as the map service, post service, leaderboard service, and chat service, all coordinated through an API Gateway and an event-driven communication model.


### Clone the repository
```
git clone https://gitlab.ewi.tudelft.nl/cs4505/2025-2026/team-11.git
cd poc
```

### Create virtual environment
For mac
```
python -m venv venv
source venv/bin/activate
```

For windows
```
pip install virtualenv
python -m virtualenv vEnv
vEnv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
pip install confluent-kafka
```

### Run the application using docker
```
docker compose up --build
```
To ensure modularity, each service can be independently shut off and started up again using the commands:
```
# stop only the leaderboard container
docker compose stop leaderboard_service

# start it again later
docker compose start leaderboard_service
```
Similarly, these commands can be applied to any service.

### Open the application
```
http://127.0.0.1:5008
http://172.18.0.8:5008
```

### Experminet Setup - Locust

Install locust using the following command:
```
pip install locustdocker compose down

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
