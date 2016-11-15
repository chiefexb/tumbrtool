#!/usr/bin/python
#coding: utf8
import hashlib
import base64
import random
import requests
import time
from urllib import urlencode
from urllib import quote
def gen_nonce():
    r=random.randint(0,999999999999)
    hsh=hashlib.md5()
    hsh.update(str(r))
    h=hsh.hexdigest()
    rez= base64.b64encode(h)
    return rez
def escape(s):
    """Escape a URL including any /."""
    if not isinstance(s, bytes):
        s = s.encode('utf-8')
    return quote(s, safe='~')
def main():
    print gen_nonce()
    from config import *
    url='https://www.tumblr.com/oauth/request_token'
    header={}
    header["Authorization: OAuth realm"]=url
    header["oauth_consumer_key"]=consumer
    header["oauth_signature_method"]="HMAC-SHA1"
    header["oauth_timestamp"]=str(int(time.time()))
    header["oauth_nonce"]="4572616e48616d6d65724c61686176"
    header["oauth_version"]="1.0"
    header["oauth_signature"]="wOJIO9A2W5mFwDgiDvZbTSMK%2FPY%3D"
    #r = requests.post('http://httpbin.org/post', data = {'key':'value'})
    r = requests.post(url, data = header)
    print r.text
    print urlencode(header)
if __name__ == "__main__":
    main()
