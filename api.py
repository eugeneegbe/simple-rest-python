from resources import app, api
from resources.users.users import Users, User

api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
