#! /bin/bash

# --- Functions: ---
 
upgrade_pip2 () {
    # Installs latest version of pip for Python2, if any version is already installed
    if pip2 &> /dev/null
        then 
            echo "*** Going to update pip for Python 2:"
            echo "*** Uninstalling old version of pip for Python2..."
            sudo apt-get remove python-pip -qq
            echo "*** Installing/updating setuptools for Python2..."
            sudo apt-get install python-setuptools -qq
            echo "*** Using easy_install to get newest version of pip for Python2..."
            sudo easy_install -U pip
        else
            echo "*** No pip for Python 2 detected - no update will be installed."
    fi 
}
 
upgrade_pip3 () {
            echo "*** Going to update pip for Python 3:"
            echo "*** Uninstalling old version of pip for Python3..."
            sudo apt-get remove python3-pip -qq
            echo "*** Installing/updating setuptools for Python3..."
            sudo apt-get install python3-setuptools -qq
            echo "*** Using easy_install to get newest version of pip for Python3..."
            sudo easy_install3 -U pip
}
 
# --- End of functions ---


# --- Main code: ---
echo "******* Installation tool to make your environment ready for Oratio-CLI *******"
echo "-------------------------------------------------------------------------------"

echo "*** Updating list of installable software..."
sudo apt-get update -qq

# find out if pip for Python2 is the default version if plain "pip" is run without version number
if pip -V | grep -q "(python 2"
    then 
        # install pip for Python2 last, so that it will become the default
        echo "*** Info: Your default pip command is pip for Python 2."
        upgrade_pip3
        upgrade_pip2 
    else
        # install pip for Python3 last, so that it will become the default
        echo "*** Info: Your default pip command is pip for Python 3."
        upgrade_pip2
        upgrade_pip3
fi 

echo "*** Now installing the latest version of module "appdirs" for Python 3..."
/usr/local/bin/pip3 -q install appdirs --user
echo "*** Now installing the latest version of module "requests" for Python 3..."
/usr/local/bin/pip3 -q install requests --upgrade --user

echo "*** FINISHED! You are now ready to use oratio-cli!"
