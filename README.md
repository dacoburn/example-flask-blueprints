# example-flask-blueprints

## Description

This is a very simple Python Flask example that is using Flask Blueprints with classes. The advantage of doing this is it makes it easier to pass arguments to your "blueprint" and keep your main `app.py` code much cleaner. Also, for someone coming in later it is much easier to read and understand.

This example also uses some simple template formats for pulling the passed variables to the blueprint classes.

## Pre-Reqs

Prior to running you need to install the Flask python module. That should be the only requirements for the example.

`pip install -r requirements.txt`

## Usage

Run:

````
export APP_PORT=5001
python main.py
````

Then in your browser you can access the pages by going to http://localhost:5001

