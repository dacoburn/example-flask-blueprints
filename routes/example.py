# We need to import the render_template and Blueprint classes so that we can
# run our simple functions
from flask import render_template, Blueprint


# This is the name of the class we will import in the main file
class Example:

    # The __init__ function is how we will pass variables to the Class to use
    # in the functions under the class.
    def __init__(self, arg):
        self.arg = arg
        # We need to call the function that creates the blueprint automatically
        # and saves the result to the variable self.example
        self.example = self.create_example()

    # This is the function that actually creates the blueprint
    def create_example(self):
        # Remember the first variable for Blueprint needs to be a unique name.
        # Since we used "index" for the other file we are using "example" here
        example_page = Blueprint("example", __name__)

        # This is the definition for the route we are creating. Notice that
        # @example_page is referring to the variable above
        @example_page.route("/<username>", methods=['GET'])
        # The name of this function becomes part of the route for url_for
        # It would be example.example for this one.
        # We also are pulling <username> as username for the function. This
        # enables having a dynamic path.
        def example(username):
            # Here we are passing username and the arg we passed when loading
            # the class in the main file. We are using the example.html template
            return render_template("example.html",
                                   username=username,
                                   arg=self.arg)
        # Return the rendered page
        return example_page
