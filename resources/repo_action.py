from flask.ext.restful import Resource, reqparse, fields, marshal
from subprocess import check_output
from common.packager import Packager
import os

# List Repository information
class RepoAction(Resource):

    packager_path = Packager.packager_path

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('repotag', type=str, required=True,
            help='Repo Tag - in []')
        self.reqparse.add_argument('name', type=str, required=False,
            help='Name of Repository to Add or Remove')
        self.reqparse.add_argument('enabled', type=int, required=False,
            default=1, help='Whether to Enable/Disable Repo')
        self.reqparse.add_argument('baseurl', type=str, required=False,
            help='Base URL of Repository')
        self.reqparse.add_argument('url', type=str, required=False,
            help='URL of repository')
        self.reqparse.add_argument('repo_user', type=str, required=False,
            help='User argument for Repo authentication')
        self.reqparse.add_argument('repo_password', type=str, required=False,
            help='Password argument for Repo authenitcation')
        self.reqparse.add_argument('repository_id', type=str, required=False,
            help='Repository ID')
        self.reqparse.add_argument('metalink', type=str, required=False,
            help='URL for Repo metadata')
        self.reqparse.add_argument('mirrorlist', type=str, required=False,
            action='append', help='List of Repository Mirror URLs')
        self.reqparse.add_argument('keepcache', type=str, required=False,
            help='Repo Keep Cache setting')
        self.reqparse.add_argument('gpgcheck', type=int, required=False,
            default=1, help='Enable GPG Validation for Packages')
        self.reqparse.add_argument('repo_gpgcheck', type=int, required=False,
            help='Enable GPG Validation for Repo')
        self.reqparse.add_argument('gpgkey', type=str, required=False,
            help='URL to GPG key')
        self.reqparse.add_argument('gpgcakey', type=str, required=False,
            help='URL to CA GPG key')
        self.reqparse.add_argument('exclude', type=str, required=False,
            action='append', help='Packages to exclude')
        self.reqparse.add_argument('includepkgs', type=str, required=False,
            help='Packages to include')
        self.reqparse.add_argument('enablegroups', type=int, required=False,
            help='Enable Package groups')
        self.reqparse.add_argument('failovermethod', type=str, required=False,
            help='Repo Failover method')
        self.reqparse.add_argument('keepalive', type=int, required=False,
            help='Repo Keepalive value')
        self.reqparse.add_argument('timeout', type=int, required=False,
            help='Repo timeout value')
        self.reqparse.add_argument('http_caching', type=str, required=False,
            help='Repo HTTP Caching mode')
        self.reqparse.add_argument('retries', type=int, required=False,
            help='Number of Retries')
        self.reqparse.add_argument('throttle', type=str, required=False,
            help='Value for Repo Throttling')
        self.reqparse.add_argument('bandwidth', type=str, required=False,
            help='Value for Bandwidth Throttling')
        self.reqparse.add_argument('ip_resolve', type=str, required=False,
            help='Resolve IPs')
        self.reqparse.add_argument('deltarpm_percentage', type=int,
            required=False, help='Delta RPM Percentage')
        self.reqparse.add_argument('deltarpm_metadata_percentage', type=int,
            required=False, help='Delta RPM Metadata Percentage')
        self.reqparse.add_argument('sslcacert', type=str, required=False,
            help='SSL CA Cert')
        self.reqparse.add_argument('sslverify', type=bool, required=False,
            help='Verify SSL')
        self.reqparse.add_argument('sslclientcert', type=str, required=False,
            help='SSL Client Cert')
        self.reqparse.add_argument('ssl_check_cert_permissions', type=bool,
            required=False, help='SSL Check Cert Permissions')
        self.reqparse.add_argument('metadata_expire', type=int, required=False,
            help='Metadata Expiration Period')
        self.reqparse.add_argument('metadata_expire_filter', type=str,
            required=False, help='Metadata Expire Filter')
        self.reqparse.add_argument('mirrorlist_expire', type=int,
            required=False, help='MirrorList Expiration Period')
        self.reqparse.add_argument('proxy', type=str, required=False,
            help='URL to Proxy - <proxy>:<port>')
        self.reqparse.add_argument('proxy_username', type=str, required=False,
            help='Username for Proxy Auth')
        self.reqparse.add_argument('proxy_password', type=str, required=False,
            help='Password for Proxy Auth')
        self.reqparse.add_argument('username', type=str, required=False,
            help='Username')
        self.reqparse.add_argument('password', type=str, required=False,
            help='Password')
        self.reqparse.add_argument('cost', type=int, required=False,
            help='Repo Cost')
        self.reqparse.add_argument('skip_if_unavailable', type=bool,
            required=False, help='Skip Repo if Unavailable')
        self.reqparse.add_argument('async', type=bool, required=False,
            help='Enable Asynchronous Operations')
        self.reqparse.add_argument('ui_repoid_vars', type=str, required=False,
            help='RepoID Vars')
        super(RepoAction, self).__init__()


    # Perform add/remove actions on Repositories
    def post(self):
        args = self.reqparse.parse_args()
        f = open("/etc/yum.repos.d/%s.repo" % args['repotag'], 'w')
        f.write("[%s]\n" % args['repotag'])

        for k, v in sorted(args.items()):
            if v is None:
                f.write("#%s=\n" % k)
            elif k is not 'repotag':
                f.write("%s=%s\n" % (k, v))
            else:
                pass

        f.close

        return { "Added repo with options:\nrepo": args }

    # Delete Repo file from /etc/yum.repos.d using Repo Tag name
    def delete(self):
        args = self.reqparse.parse_args()
        f = "/etc/yum.repos.d/%s.repo" % args['repotag']

        if os.path.isfile(f):
            os.remove(f)
            return { "Removed Repo file": f }
        else:
            return { "Repo File: %s Does not exist in /etc/yum.repos.d" % f }
