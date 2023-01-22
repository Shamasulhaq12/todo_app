from app import app
from flask_restful import Api
from .views import TaskAPIView, RetrieveTaskView

# Create an instance of the Api class and pass in the app instance
api = Api(app)
api.add_resource(TaskAPIView, '/tasks/')
api.add_resource(RetrieveTaskView, '/task/<task_id>/')
