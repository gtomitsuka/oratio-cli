# oratio-cli
CLI for Marketplace Uploads. It requires Python 3.x.

# Dependencies

Oratio CLI requires the following dependencies:

 - `requests` - http://docs.python-requests.org/en/latest/
 - `appdirs` - https://pypi.python.org/pypi/appdirs/1.4.0

You can install these by running `setup.sh`.  
Note: `setup.sh` will install pip for Python 3 but it will overwrite pip for Python 2. If you don't want the setup file to do this (or if you use Ubuntu 12.04 or older, where setup.sh won't work), then follow the instructions [from this answer on AskUbuntu.com](http://askubuntu.com/a/412179/282856). You'll also have to run the installation commands for the dependencies manually, see setup.sh for the dependency names.
