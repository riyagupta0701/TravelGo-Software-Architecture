# Project Name

Give an overview of your proof of concept. Check lecture slides for details


### Clone the repository
```
git clone https://gitlab.ewi.tudelft.nl/cs4505/2025-2026/team-11.git
cd poc
```

### Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the microservices
Run all the microservices in separate terminals:

```
export FLASK_APP=services.user_service.py && flask run -p 5001
```
```
export FLASK_APP=services.post_service.py && flask run -p 5002
```
```
export FLASK_APP=services.leaderboard_service.py && flask run -p 5003
```
```
export FLASK_APP=services.chat_service.py && flask run -p 5004
```
```
export FLASK_APP=services.map_service.py && flask run -p 5005
```

### Run the API gateway
In a new terminal:

```
export FLASK_APP=api_gateway.py && flask run -p 5000
```

### Run the frontend service
In a new terminal:

```
export FLASK_APP=services/frontend_service.py && flask run -p 5008
```

### To access the SQLite database
In a new terminal:

```
cd poc/instance
sqlite_web travelgo.db
```
