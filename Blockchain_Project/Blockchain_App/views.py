from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
from time import time, ctime
from urllib.parse import urlparse
from uuid import uuid4

import requests



class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, previous_hash, proof):
        pass

    def last_block():
        pass

    def new_transactions():
        pass

    def hash():
        pass
    
    def proof_of_work():
        pass

    def valid_proof():
        pass

    def reguster_node():
        pass

    def resolve_conflicts():
        pass

    def valid_chain():
        pass



####_____object_____####
blockchain = Blockchain()

def full_chain(request):
    if request.method == 'GET':
        response = {'chain': blockchain.chain,
                    'length' : len(blockchain.chain),    
                    }
    return JsonResponse(response)

def new_transcations():
    pass

def mine():
    pass

def register_node():
    pass

def consensus():
    pass



####_____TEST__VIEW__git___####
def test(request):
    if request.method == "GET":
        response = {'message': 'WORKING'}
    return JsonResponse(response)