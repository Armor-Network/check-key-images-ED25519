#!/usr/bin/env python

# 
# run python3 double-spend.py
 
import sys
from binascii import unhexlify, hexlify
from pure25519.basic import Zero, L, bytes_to_unknown_group_element
#import urllib2, urllib
import urllib.request
import urllib.error
import json
from retrying import retry
import requests

# Q = 2**255 - 19
# L = 2**252 + 27742317777372353535851937790883648493
 
ORDERS = {1: "1", 2: "2", 4: "4", 8: "8",
          1*L: "1*L", 2*L: "2*L", 4*L: "4*L", 8*L: "8*L"}

# DAEMON URL JSON
url = 'http://207.180.201.219:8081/json_rpc'

def get_order(e):
    for o in sorted(ORDERS):
        if e.scalarmult(o) == Zero:
            return o
 
@retry(stop_max_attempt_number=20, wait_fixed=2000)

def get_block_hash(height):
    payload = { 'jsonrpc': '2.0',
                'id': '0',
                'method': 'getblockheaderbyheight',
                'params': {'height': height} }
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.json()['result']['block_header']['hash']
    
def get_transaction_hashes(block_hash):
    payload = { 'jsonrpc': '2.0',
                'id': '0',
                'method': 'get_raw_block',
                'params': {'hash': hash} }
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.json()['result']['block']['raw_header']['transaction_hashes']
    
def get_raw_transaction(tx_hash):
    payload = { 'jsonrpc': '2.0',
                'id': '0',
                'method': 'get_raw_transaction',
                'params': {'hash': tx_hash} }
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.json()['result']['raw_transaction']
 
#change block height range as necessary
# 1243490, 1243492
# 1243488
for blockHeight in range(1, 1267001):
    print ("====  block height %s ====" % blockHeight)
    #print json.dumps(block, indent=4)
    hash = get_block_hash(blockHeight)
    tx_hashes = get_transaction_hashes(hash)
    #tx_hashes = [tx["hash"] for tx in transactions]
 
    for tx_hash in tx_hashes:
        print ("tx:", tx_hash)
        inputs = get_raw_transaction(tx_hash)['inputs']
        #print inputs
        keyimages = [str(i.get("key_image")) for i in inputs if i.get("key_image")]
        #
        #print "key images: %s" % (keyimages,)
        for ki in keyimages:
            #print hexlify(unhexlify(ki))
            try:
                elem = bytes_to_unknown_group_element(unhexlify(ki))
                order = get_order(elem)
                if order != L:
                    print ("*** keyimage %s order %s" % (ki, ORDERS[order]))
                    with open("bad_keyimages", "a") as f:
                        f.write("%s;" % ki)
                        f.write("%s;" % tx_hash)
                        f.write("%s\n" % blockHeight)
                else:
                    print (" - key image: %s" % ki)
            except (Exception, e):
                print (e)
                print ("Bad keyimage", ki)
                with open("bad_keyimages", "a") as f:
                    f.write("%s;" % ki)
                    f.write("%s;" % tx_hash)
                    f.write("%s\n" % blockHeight)
