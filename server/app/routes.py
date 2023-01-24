from app import app
from flask_restful import Api
from .views import TaskAPIView, RetrieveTaskView, UserRegistration, UserLogin

# Create an instance of the Api class and pass in the app instance
api = Api(app)
api.add_resource(TaskAPIView, '/tasks/')
api.add_resource(RetrieveTaskView, '/task/<task_id>/')
api.add_resource(UserRegistration, '/register/')
api.add_resource(UserLogin, '/login/')


