[![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![Winter is coming!](http://ForTheBadge.com/images/badges/winter-is-coming.svg)](https://github.com/n1rv4n4/pyddoz/)

# PyDDoZ [![PyDDoZ](https://img.shields.io/badge/PyDDoZ-1.0.0%20rc.1-red.svg)](https://github.com/n1rv4n4/pyddoz/) [![GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
PyDDoZ is a powerful, human-friendly DDoS tool using application layer (L7) attack techniques. It has nice logging, proxifying, automated bots requests, randomizing data, multiple HTTP request methods, and many other features! Apply load/stress tests to your web application in various ways easily. Written in Python.

## Prerequisites
`$ pip3 install -r requirements.txt`

## Installation
```
$ git clone https://github.com/n1rv4n4/pyddoz.git
$ cd pyddoz
$ python3 pyddoz.py
```

## Usage
PyDDoZ provides an interactive shell for users.

- You can enter multiple URLs with a blank space. It will request randomly one of them for every request. <br>
Example: https://google.com https://twitter.com https://yahoo.com

Or give just one URL.

- Select one of the request method. POST and PUT require data to post! <br>
After selecting POST or PUT, you can randomize the data for every request! <br> 

For instance, `username=admin&password=hello` will be sent as `username=[RANDOMSTR]&query=[RANDOMSTR]` <br>

**RANDOMSTR** could be any random string that was generated at backstage. You can determine maximum length of the random generated string.

### Other Features
- Activation of bots: In addition to standard requests, they will also hit and crawl the target URL.
- Timeout: Maximum waiting time request to be responded. *Recommended value is higher than 5.*
- Threads: Number of threads to involve the attack. *Large number of threads could lead connection and system errors!*
- Sleeping time between threads (seconds): 0 to non-wait, or you can give floating number such as 0.25, 0.5, or 0.87 etc.
- Retries after failure: You can force requests to retry again.
- Proxy: After selecting this option, fresh and live proxies will be fetched and used randomly! No need to enter proxies manually.
- Allowing redirections: If target responds with 302 or 301 code, you may allow redirections, but most of the time not required.

[![Say thanks.](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://www.linkedin.com/in/orçunözdemir/)

**For educational purposes only.**


