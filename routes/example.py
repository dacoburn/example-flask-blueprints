from flask import render_template, Blueprint


class Example:

    def __init__(self, arg):
        self.arg = arg
        self.example = self.create_example()

    def create_example(self):
        example_page = Blueprint("example", __name__)

        @example_page.route("/<username>", methods=['GET'])
        def example(username):
            return render_template("example.html",
                                   username=username,
                                   arg=self.arg)

        return example_page
