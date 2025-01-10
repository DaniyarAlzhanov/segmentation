# Map segmentation project on Python.

## How to start:

1. Clone project on your computer:

```
git clone -> put ssh-key here
```

2. Initialize and laucn virtual enviroment:

```
python -m venv venv
.\venv\Scripts\activate
```

3. Install requirements:

```
pip install --upgrade pip
pip install -r requirements.txt
```

4. Launch fastapi app:

```
cd web
uvicorn main:app
```

5. Open template example.html in ./templates