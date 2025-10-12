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

### Run the application using docker
Once you navigate to the poc folder, run the command:
```
docker compose up --build
```