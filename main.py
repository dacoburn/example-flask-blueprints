from flask import Flask
import os
# We are importing the classes from our blueprint python files
# This way we can call them directly for adding them as routes
from routes.index import Index
from routes.example import Example

app = Flask(__name__)
# We create new variables with the initialized Classes from the Blueprint Python
# files. Notice any variables you want to pass need to be at this stage.
index = Index("Example User")
example = Example("Random Arg")

# Once we've initialized the Classes into variables we can add them to the
# App using register_blueprint
app.register_blueprint(index.index)
app.register_blueprint(example.example)

if __name__ == '__main__':
    # I like to either get the port from an env variable or use the default
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
