from flask import Flask
import os
from routes.index import Index
from routes.example import Example

app = Flask(__name__)
index = Index("Example User")
example = Example("Random Arg")
app.register_blueprint(index.index)
app.register_blueprint(example.example)

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
