#!flask/bin/python
import base64
from flask import Flask, jsonify, make_response
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api, Resource
from resources.repo_list import RepoList
from resources.repo_action import RepoAction
from resources.pkg import Pkg

# App Definition
auth = HTTPBasicAuth()
app  = Flask(__name__, static_url_path="")
#api  = Api(app)
api  = Api(app, decorators=[auth.login_required])

# Retrieve User Password
@auth.get_password
def get_password(username):
    if username == 'root':
        return base64.b64decode('cHl0aG9u')
        return None

# Deny unauthorized Use
@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


# Add Repo List Resource
api.add_resource(RepoList, '/packager/repo/list')
# Add Repo Operations Resource
api.add_resource(RepoAction, '/packager/repo', endpoint='repos')
# Add Package Operations Resource
api.add_resource(Pkg, '/packager', endpoint='pkg')

if __name__ == '__main__':
    app.run(debug=True)
