# macos-terminal-proxy

Allows the MacOS terminal to use the keychain to authenticate to a given proxy.  Ideally this owuld be used within a corporate setting, however; this could easily be adapted to use with a personal home proxy setup.

By using the keychain, you do not have to worry about updating your password within your terminal profile every 60-90 days.

---
## What this script does

Thsi script will add the terminal profile code to the beginning of your existing `.bash_profile`, `.bashrc`, or `.zshrc` file keeping all your current settings completely intact.

## Installation

To install this to your terminal profile, follow these steps:

1. Run the following command in your terminal (assuming you have some kind of proxy settings already configured):

        curl https://raw.githubusercontent.com/dad2jrn/macos-terminal-proxy/master/install.py -o $HOME/proxy_install.py && python $HOME/proxy_install.py

---

## Contributions

Pull requests are welcome.