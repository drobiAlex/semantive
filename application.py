from background import app, save_text, save_img
from flask_restful import Api, Resource, reqparse
from download import download_file

api = Api(app)

class Upload(Resource):
    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument("url")
        parser.add_argument("type")

        args = parser.parse_args()

        if args["type"] == "img":
            save_img.delay(args["url"])

        elif args["type"] == "text":
            save_text.delay(args["url"])

        else:
            return "There is a mistake in type", 400

        # return feed_back, 201
        return "Your task in queue", 201


class Download(Resource):
    def get(self):

        parser = reqparse.RequestParser()

        parser.add_argument("url")
        parser.add_argument("type")

        args = parser.parse_args()

        download_file.delay(args["url"])
        return "What a minute"

api.add_resource(Upload, '/upload')
api.add_resource(Download, '/download')

if __name__ == '__main__':
    app.run(debug=False)
