# We need to import the render_template and Blueprint classes so that we can
# run our simple functions
from flask import render_template, Blueprint


# This is the name of the class we will import in the main file
class Index:

    # The __init__ function is how we will pass variables to the Class to use
    # in the functions under the class.
    def __init__(self, username):
        self.username = username
        # We need to call the function that creates the blueprint automatically
        # and saves the result to the variable self.index
        self.index = self.create_index()

    # This is the function that actually creates the blueprint
    def create_index(self):
        # The first variable in Blueprint needs to be a unique name. I.E. it can
        # not be the same in here and the example.py. I keep it simple and just
        # use "index" here and "example" in the other one.
        index_page = Blueprint("index", __name__)

        # This is the actual route that will be handled in here. You could have
        # multiple functions/routes to handle different methods. This one only
        # supports GET with how it is written.
        # Also notice @index_page is referring to the variable above
        @index_page.route("/", methods=['GET'])
        # This is the name of the function that creates the page and is part of
        # the internal route name. So for url_for the route becomes index.index
        def index():
            # Render the template and pass the variable username to the template
            # We are using the index.html template
            return render_template("index.html", username=self.username)

        # WWe are returning the variable that is now the blueprint
        return index_page
