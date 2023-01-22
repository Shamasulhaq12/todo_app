import os
from app import auth, db
from app.models import Task
from flask_api import status
from dotenv import load_dotenv
from .utils import decrypt,encrypt
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash


KEY=str(os.getenv('KEY'))
load_dotenv('../.env')
KEY="asdfghjklqwertyuiopzxcvb"

# user details in dictionary for authentication purpose just for testing
users = {
    "Shamas": generate_password_hash("admin123"),
    "entertainer": generate_password_hash("testing")
}
## Authentication for the endpoints verification of password and username
@auth.verify_password
def verify_password(username, password):    
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('status', type=bool)


class TaskAPIView(Resource):

    @auth.login_required
    def get(self):
        ## Querying all the tasks from the database
        list_of_tasks = []
        for task in Task.query.all():
            dict_task_object = {}
            dict_task_object['id'] = task.id
            dict_task_object['task'] = task.title
            dict_task_object['description'] = task.description
            dict_task_object['status'] = task.status
            dict_task_object['created_at'] = task.created_at.strftime("%d-%m-%Y-%H:%M:%S")
            dict_task_object['updated_at'] = task.updated_at.strftime("%d-%m-%Y-%H:%M:%S")
            list_of_tasks.append(dict_task_object)
        ## encrypting the data before sending it to the client side 
        return encrypt(KEY,list_of_tasks), status.HTTP_200_OK
    
    def post(self):
        ## Creating a new task in the database
        data = parser.parse_args()
        create_task = Task(title=data['title'],
                           description=data['description'])
        db.session.add(create_task)
        db.session.commit()
        obj_data={"id": create_task.id,
                "title": create_task.title,
                }
        ## encrypting the data before sending it to the client side
        return encrypt(KEY,obj_data), status.HTTP_201_CREATED


class RetrieveTaskView(Resource):

    def get(self, task_id):
        ## Querying a single task from the database
        obj = db.session.query(Task).filter_by(id=task_id).first_or_404()
        dict_object = {}
        dict_object['id'] = obj.id
        dict_object['title'] = obj.title
        dict_object['description'] = obj.description
        dict_object['created_at'] = obj.created_at.strftime("%d-%m-%Y-%H:%M:%S")
        dict_object['updated_at'] = obj.updated_at.strftime("%d-%m-%Y-%H:%M:%S")
        dict_object['status'] = obj.status
        ## encrypting the data before sending it to the client side
        return encrypt(KEY,dict_object), status.HTTP_200_OK

    def delete(self, task_id):
        ## Deleting a single task from the database

        task = db.session.query(Task).filter_by(id=task_id).first_or_404()
        if task is None:
            return {
                "message": "Task does not exist"
            }, 404
        db.session.delete(task)
        db.session.commit()
        return ({"message":"Task is deleted seccussfully"}), status.HTTP_204_NO_CONTENT

    def patch(self, task_id):
        ## Updating a single task from the database
        task = db.session.query(Task).filter_by(id=task_id).first_or_404()
        data = parser.parse_args()
        title = data['title']
        description = data['description']
        status = data['status']
        task.title = title if title is not None else task.title
        task.description = description if description is not None else task.description
        task.status = status if status is not None else task.status
        db.session.commit()
        object_data = {
            "task_id": task.id,
            "task_title": task.title,
            "task_status": task.status,
            "task_description": task.description,
            "task_created_at": task.created_at.strftime("%d-%m-%Y-%H:%M:%S"),
            "task_updated_at": task.updated_at.strftime("%d-%m-%Y-%H:%M:%S"),
        }
        ## encrypting the data before sending it to the client side
        return encrypt(KEY,object_data), 200
