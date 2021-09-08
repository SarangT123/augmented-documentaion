from flask import Flask, Blueprint, render_template, redirect
import os
from os import walk

views = Blueprint('views', __name__)


@views.route('/')
def home():
    filenames = next(walk('website/static/docs'),
                     (None, None, []))[2]  # [] if no file
    filenames2 = next(walk('website/static/docs/submodules'),
                      (None, None, []))[2]  # [] if no file

    return render_template('home.html', filenames=filenames, filenames2=filenames2)


@views.route('/docs/<id>')
def docs(id):
    try:
        print(f'website/static/docs/{id}')
        file = open(f'website/static/docs/{id}', 'r')
        docs = file.read()
        return docs
    except FileNotFoundError as f:
        return '<h1>404</h1> \n Url does not exist'


@views.route('/docs/submodules/<id>')
def docs_submodules(id):
    try:
        print(f'website/static/docs/{id}')
        file = open(f'website/static/docs/submodules/{id}', 'r')
        docs = file.read()
        return docs
    except FileNotFoundError as f:
        return '<h1>404</h1> \n Url does not exist'
