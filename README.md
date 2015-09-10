# packager-api

#### Table of Contents

1. [Overview](#overview)
2. [Module Description - What the module does and why it is useful](#module-description)
    * [What is managed](#what-is-managed)
      * [Repositories](#repositories)
      * [Packages](#packages)
    * [Dependencies](#dependencies)
3. [Usage - Configuration options and additional functionality](#usage)
4. [Testing](#testing)
5. [Limitations - OS compatibility, etc.](#limitations)
6. [Authors](#authors)
7. [Change Log](https://github.com/exodusftw/packager-api/tree/master/CHANGELOG.md)

## Overview

Python/Flask API for Interfacing with YUM/DNF for Package & Repo Management

## Module Description

RESTful API using Python/Flask that provides capabilities for managing:
  * Yum Repositories via drop-in files in `/etc/yum.repos.d`
  * RESTful package management for `installation`, `upgrade`, and `removal`

* `Preferred Package Managers`:
  * [YUM](http://yum.baseurl.org/)
  * [DNF](http://dnf.readthedocs.org/en/latest/)

* `Preferred System Management Tools`:
  * [Spacewalk](http://spacewalk.redhat.com/)
  * [Red Hat Network Satellite](https://access.redhat.com/products/red-hat-satellite)

### What Is Managed

#### Repositories
* Provides HTTP operations for listing/adding/removing yum repositories in `/etc/yum.repos.d`
  * METHODS:
    * `GET` - Endpoint: `/packager/repo/list`
    * `POST` - Endpoint: `/packager/repo`
    * `DELETE` - Endpoint: `/packager/repo`
  * REQUIRED PARAMETERS:
    * `repotag`:
      * Main inifile header in repo file - i.e. `[fedora-stable]`
    * All other parameters are optional
      * If values are not provided, entries will be added to file in a null, commented state
  * DOCUMENTATION ON AVAILABLE PARAMETERS CAN BE FOUND:
    * [Repo Actions](https://github.com/exodusftw/packager-api/blob/master/resources/repo_action.py)
    * [YUM Configuration](http://man7.org/linux/man-pages/man5/yum.conf.5.html)
  * Example:
```bash
/usr/bin/curl -i -H "Content-Type: application/json" -X POST -d \
S>'{
     "repotag": "ol7_spacewalk22_client",
     "name": "Spacewalk Client 2.2 for Oracle Linux 7 ($basearch)",
     "baseurl": "http://public-yum.oracle.com/repo/OracleLinux/OL7/spacewalk22/client/$basearch/",
     "gpgkey": "file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle",
     "gpgcheck": 1,
     "enabled": 1 
   }' \
  "http://${username}:${password}@localhost:5000/packager/repo"

```

#### Packages
* `Provides HTTP operations for installing/updating/removing packages via YUM/DNF commands
  * METHODS:
    * `POST` - Endpoint `/packager`
  * REQUIRED PARAMETERS:
    * `action`:
      * `install`
      * `update`
      * `remove`
    * `packages`:
      * either single package name or list of package names
  * Example:
```bash
/usr/bin/curl -i -H "Content-Type: application/json" -X POST -d \
'{
   "action": "install",
   "packages": [
     "net-snmp",
     "rubygem-loofah",
     "rubygem-capybara"
   ]
}' \
"http://${username}:${password}@localhost:5000/packager"
```

### Dependencies
* Developed on `Python 2.7.10`
* [Virtualenv](https://virtualenv.pypa.io/en/latest/)
* [Pip](https://pip.pypa.io/en/stable/)
* [Flask](http://flask.pocoo.org/)
* [flask-restful](https://flask-restful.readthedocs.org/en/0.3.4/)
* Must run with `root` user privileges to ensure proper package management
* All endpoints require authentication through local admin account

## Usage
Example:
* Activate Virtualenv
  * `source flask/bin/activate`
* Install requirements with pip:
  * `pip install -r requirements.txt`
* Start App as root or with sudo privileges:
  * `./app.py` or `sudo ./app.py`
* Default Credentials for application are:
  * `root` / `python`

## Testing
* Testing scripts have been placed in the `examples` directory and Test:
  * Adding Repositories
  * Removing Repositories
  * Listing Repositories
  * Installing/Updating/Removing Packages

## Limitations

Tested on:
* FEDORA 22
* CENTOS 7

## Authors

* Jeremy Grant <Jeremy.Grant@outlook.com>

