source venv/bin/activate

export FLASK_PORT=7777
export FLASK_ENV=development
export FLASK_APP=main.py

flask run --port $FLASK_PORT
