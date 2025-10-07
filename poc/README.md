# Project Name

Give an overview of your proof of concept. Check lecture slides for details


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
```

### Run the microservices
Run all the microservices in separate terminals:

```
python services/user_service.py
```
```
python services/post_service.py
```
```
python services/leaderboard_service.py
```
```
python services/chat_service.py
```
```
python services/map_service.py
```

### Run the event bus
In a new terminal:

```
python events/event_bus.py
```

### Run the API gateway
In a new terminal:

```
python api_gateway.py
```

### Run the frontend service
In a new terminal:

```
python services/frontend_service.py
```

### To access the SQLite database
In a new terminal:

```
cd poc/instance
sqlite_web travelgo.db
```
