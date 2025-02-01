from app import app
from aws_lambda_wsgi import WSGIAdapter


def lambda_handler(event, context):
    """
    AWS Lambda Handler to serve Flask app
    """
    return WSGIAdapter(app)(event, context)
