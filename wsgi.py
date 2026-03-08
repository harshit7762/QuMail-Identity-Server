from identity_server import app
from flask import Flask
# ... your logic ...
app = Flask(__name__)
# ... your routes ...

if __name__ == "__main__":
    app.run()
