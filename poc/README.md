# Team 11: TravelGo


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

### Run the application using docker
Once you navigate to the poc folder, run the command:
```
docker compose up --build
```

### Open the application
```
http://127.0.0.1:5008
http://172.18.0.8:5008
```