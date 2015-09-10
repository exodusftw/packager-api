from flask.ext.restful import Resource
from subprocess import check_output
from flask import make_response
from common.packager import Packager

 # List Repository information
class RepoList(Resource):

    packager_path = Packager.packager_path

    def __init__(self):
        super(RepoList, self).__init__()

    # List Currently Enabled  Repositories
    def get(self):
        repolist = make_response(check_output([self.packager_path, 'repolist']))
        return repolist

