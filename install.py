#!/usr/bin/env python
# Import the modules needed to run the script.
import os
import sys
import getpass

# try:
#     from pyfiglet import Figlet
# except ImportError:
#   print("Trying to Install required module: pyfiglet\n")
#   os.system('python -m pip install pyfiglet')
# from pyfiglet import Figlet

def main():
    try:
        import imp
        imp.find_module('pyfiglet')
        banner("0x90")
        set_proxy()
    except ImportError:
        print("Trying to install optional module: 'pyfiglet'\n")
        os.system('python -m pip install pyfiglet')
        os.system('clear')
        banner("The Forge")
        set_proxy()


def banner(message):
    try:
        from pyfiglet import Figlet
        figlet=Figlet(font='starwars')
        text = message
        os.system('clear')
        print(figlet.renderText(text))
    except ImportError:
        pass

# Check for Python 3
def set_proxy():
    home_dir = os.path.expanduser('~')
    bash_profile = f"{home_dir}/.bash_profile"
    zsh_profile = f"{home_dir}/.zshrc"
    bashrc_profile = f"{home_dir}/.bashrc"

    proxy_settings = "# Set Proxy \n\
#------------------------------------------------------------ \n\
# This file enables the terminal to use proxy for as much traffic as possible by\n\
# setting several enviroment variables. Not all applications pay attention to\n\
# these settings however. Some programs you may have to configure manually\n\n\
## Define Core Proxy variable\n\
core_proxy=\"<PROXY ADDRESS>:<PROXY PORT>/\"\n\n\
## Allows the username and password to be passed to the environemtn variables for proxy\n\
function proxyon() {\n\
    export no_proxy=\"localhost,127.0.0.1,localaddress,.localdomain.com\"\n\n\
    if [ ${#USER} -ne 6 ]; then\n\
        echo \"WARNING: your USER environment variable doesn't contain an VALID ID. Add 'export USER=ABC123' in your .bash_profile\";\n\
    fi\n\n\
## this tells the local security service to get the password for a specific keychain item that\n\
##   that uses the necessary password.  You can choose to use any item from your keychain if you wish.\n\
    local pre=\"$USER:$(security find-internet-password -s <PROXY ADDRESS HERE> -w | tr -d '\\n')\"\n\n\
## Exports the proxy settings to your environment\n\
    export http_proxy=\"http://$pre@$core_proxy\"\n\
    export https_proxy=$http_proxy\n\
    export ftp_proxy=$http_proxy\n\
    export rsync_proxy=$http_proxy\n\
    export HTTP_PROXY=$http_proxy\n\
    export HTTPS_PROXY=$http_proxy\n\
    export FTP_PROXY=$http_proxy\n\
    export RSYNC_PROXY=$http_proxy\n\
    export all_proxy=$http_proxy\n\
    export ALL_PROXY=$http_proxy\n\
    [ \"-s\" != \"$1\" ] && echo \"Please allow access to your keychain so that you can be authenticated.\" && echo \"Proxy Enabled\" && echo -e \"Some applications may require additional configuration (eg. git, npm, Atom editor)\"\n\
}\n\n\
function proxyall() {\n\
local proxies=( HTTP_PROXY https_proxy HTTPS_PROXY ftp_proxy FTP_PROXY all_proxy ALL_PROXY )\n\
local cmd=''\n\
for i in \"${proxies[@]}\"\n\
do\n\
    export $i=\"$http_proxy\"\n\
done\n\
}\n\n\
## Disables the proxy settings\n\
function proxyoff() {\n\
    unset http_proxy\n\
    unset https_proxy\n\
    unset ftp_proxy\n\
    unset rsync_proxy\n\
    unset HTTP_PROXY\n\
    unset HTTPS_PROXY\n\
    unset FTP_PROXY\n\
    unset RSYNC_PROXY\n\
    unset all_proxy\n\
    unset ALL_PROXY\n\
    echo -e \"Proxy disabled\"\n\
}\n\n\
## CAUTION ****\n\
##  Reveals your current proxy settings and displays your password in clear text.\n\
function proxyinfo() {\n\
local proxies=( http_proxy HTTP_PROXY https_proxy HTTPS_PROXY ftp_proxy FTP_PROXY all_proxy ALL_PROXY )\n\
local ds='$'\n\
for i in \"${proxies[@]}\"\n\
do\n\
    printf \"$i\\t\"\n\
    eval \"echo $ds$i\"\n\
done\n\
}\n\n\
## Test the proxy connectivity.\n\
function proxytest() {\n\
echo \"Test Google (Success 1 Fail 0):\"\n\
curl -ILs --max-time 10 www.google.com | grep \"200 OK\" | wc -l\n\
}\n\n\
# Use the proxy without your credentials (you won't have as much access but you can reveal your settings in front of others)\n\
function proxyanon() {\n\
export http_proxy=\"http://$core_proxy\"\n\
proxyall\n\
[ \"-s\" != \"$1\" ] && echo \"Proxy enabled without credentials\"\n\
proxyinfo\n\
echo -e '*** You must run \"proxyon\" again to enable proxy with credentials. ***'\n\
}\n\n\
## Automatically enables the proxy upon window load in verbose mode. Comment the next line to disable.\n\
# proxyon\n\n\
## Automatically enables the proxy for every terminal window silently. Uncomment the next line to disable the info message everytime\n\
proxyon - s\n\n\
############ END PROXY SETTINGS ############\n"


    # =======================
    #     MENUS FUNCTIONS
    # =======================

    ## Show menu ##
    print(30 * '-')
    print(6 * ' ' + "M A I N - M E N U")
    print(30 * '-')
    print(f"1. Modify '{home_dir}/.bash_profile'")
    print(f"2. Modify '{home_dir}/.bashrc'")
    print(f"3. Modify '{home_dir}/.zshrc'")
    print("4. EXIT")
    print(30 * '-')

    ## Get input ###
    choice = input('Enter your choice [1-4] : ')

    ### Convert string to int type ##
    choice = int(choice)

    ### Take action as per selected menu-option ###
    if choice == 1:
        # prepend proxy settigns to existing ~/.bash_profile
        if os.path.exists(bash_profile):
            with open(bash_profile, 'r+') as f:
                file_data = f.read()
                f.seek(0, 0)
                f.write(proxy_settings + '\n' + file_data)
            os.system('clear')
            print(f"\nProxy settings have been added to {bash_profile}.")
        else:
            os.system('clear')
            print(f"Sorry but the file {bash_profile} does not exist.")
            sys.exit()
    elif choice == 2:
        # prepend proxy settigns to existing ~/.bashrc
        if os.path.exists(bashrc_profile):
            with open(bashrc_profile, 'r+') as f:
                file_data = f.read()
                f.seek(0, 0)
                f.write(proxy_settings + '\n' + file_data)
            os.system('clear')
            print(f"\nProxy settings have been added to {bashrc_profile}.")
        else:
            os.system('clear')
            print(f"Sorry but the file {bashrc_profile} does not exist.")
            sys.exit()
    elif choice == 3:
        # prepend proxy settigns to existing ~/.bash_profile
        if os.path.exists(zsh_profile):
            with open(zsh_profile, 'r+') as f:
                file_data = f.read()
                f.seek(0, 0)
                f.write(proxy_settings + '\n' + file_data)
            os.system('clear')
            print(f"\nProxy settings have been added to {zsh_profile}.")
        else:
            os.system('clear')
            print(f"Sorry but the file {zsh_profile} does not exist.")
            sys.exit()
    elif choice == 4:
        os.system('clear')
        print(f"Good bye... {getpass.getuser()}. See you next time!\n\n")
        sys.exit()
    else:  ## default ##
        import time
        os.system('clear')
        print("Invalid option entered. Try again...")
        time.sleep(3)
        main()

if __name__ == '__main__':
    main()