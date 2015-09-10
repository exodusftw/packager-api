from flask.ext.restful import Resource, reqparse, inputs
from subprocess import check_output
from common.packager import Packager

class Pkg(Resource):

    packager_path = Packager.packager_path

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('action',
            type=inputs.regex('^(install|update|remove)$'),
            required=True,
            help = 'Desired Package Action - "install", "update", or "remove"')
        self.reqparse.add_argument('packages', type=str, required=True,
            action='append', help = 'List or String of Package Names')
        super(Pkg, self).__init__()

    def post(self):
        packager_path = self.packager_path
        args = self.reqparse.parse_args()
        return check_output([packager_path, '-y', args['action']] +
            args['packages'])


