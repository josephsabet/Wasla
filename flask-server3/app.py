import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from flask import Flask
from controllers.matching_controller import matching_blueprint

app = Flask(__name__)
app.register_blueprint(matching_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
