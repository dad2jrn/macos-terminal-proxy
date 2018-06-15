# macos-terminal-proxy

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GitHub license](https://img.shields.io/github/license/dad2jrn/macos-terminal-proxy.svg)](https://github.com/dad2jrn/macos-terminal-proxy/blob/master/LICENSE) [![Github all releases](https://img.shields.io/github/downloads/dad2jrn/macos-terminal-proxy/total.svg)](https://github.com/dad2jrn/macos-terminal-proxy/releases)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)


Allows the MacOS terminal to use the keychain to authenticate to a given proxy.  Ideally this would be used within a corporate setting, however; this could easily be adapted to be used with a personal home proxy setup that requires authentication.

By using the keychain, you do not have to worry about updating your password within your terminal profile every 60-90 days.

---
## What this script does

Thsi script will add the terminal profile code to the beginning of your existing `.bash_profile`, `.bashrc`, or `.zshrc` file keeping all your current settings completely intact.

## Installation

To install this to your terminal profile, just run the following command in your terminal (assuming you have some kind of proxy settings already configured):

  ```bash
  curl https://raw.githubusercontent.com/dad2jrn/macos-terminal-proxy/master/install.py -o $HOME/proxy_install.py && python $HOME/proxy_install.py
  ```

---

## License

MIT

---

## Contributions

Pull requests are welcome.