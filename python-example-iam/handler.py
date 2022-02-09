import os

def hello(event, context):
    return os.environ['first_name']