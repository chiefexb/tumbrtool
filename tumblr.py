#!/usr/bin/python
#coding: utf8
import requests
def main():
    url="https://www.tumblr.com/oauth/request_token"
    r=requests.post(url, data={'key':akey,'secret':sec}) 
if __name__ == "__main__":
    main()
