from src.details.app import app

HOST='0.0.0.0'
PORT=8123
DEBUG=True

app.run(host=HOST, port=PORT, debug=DEBUG)