from app import app
from flask_restful import Api
from .views import TaskAPIView, RetrieveTaskView

api = Api(app)
api.add_resource(TaskAPIView, '/task/')
api.add_resource(RetrieveTaskView, '/task/<task_id>/')
