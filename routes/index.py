from flask import render_template, Blueprint


class Index:

    def __init__(self, username):
        self.username = username
        self.index = self.create_index()

    def create_index(self):
        index_page = Blueprint("index", __name__)

        @index_page.route("/", methods=['GET'])
        def index():
            return render_template("index.html", username=self.username)

        return index_page
