from flask import Flask
from flask_restful import Resource, Api
import json
from CreateFangraphsDraftLeaderboard import create_leaderboard

app = Flask('fantasy_baseball')
api = Api(app)


class Leaderboard(Resource):

    def get(self):
        response = json.loads(create_leaderboard())
        return response


class Draft(Resource):

    def get(self):
        return 'draft'


api.add_resource(Leaderboard, '/leaderboard')

if __name__ == '__main__':
    app.run(debug=True)
