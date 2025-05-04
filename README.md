# Simple Web Application

To run the application you need to do the following

1. Create a new virtual environment
```sh
python3 -m venve .venv
```

2. Activate the enviroment
```sh
source .venv/bin/activate
```

3. install the dependencies
```sh
pip install -r requirements.txt
```

4. Create the database
```sh
python create_db.py
```

5. Run the service
```sh
python api.py
```
The API service should be running on `http://127.0.0.1:5000`
