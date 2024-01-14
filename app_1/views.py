# from django.shortcuts import render
import logging
from django.http import HttpResponse, HttpRequest

# Create your views here.
logger = logging.getLogger(__name__)


def index(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task001</title>
</head>
<body>
    <h1>Это главная страница сайта на Django.</h1>
    <h3>Она находится по адресу: {request.get_host() + request.path}</h3>
</body>
</html>
    """
    logger.debug('Index page requested.')

    return HttpResponse(html)


def about(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task001</title>
</head>
<body>
    <h1>Это страница обо мне.</h1>
    <h3>Она находится по адресу: {request.get_host() + request.path}</h3>
</body>
</html>
    """
    logger.debug('About page requested.')

    return HttpResponse(html)
