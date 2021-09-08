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

        #The genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, previous_hash, proof):
        block = {
            "index" : len(self.chain) + 1,
            "timestamp" : ctime(),
            "transactions" : self.current_transactions,
            "proof": proof,
            "previous_hash" : previous_hash,
        }

        self.current_transactions = []
        self.chain.append(block)
        return block


    def last_block(self):
        return self.chain[-1]
        

    def new_transactions(self, sender, reciever, amount):
        self.current_transactions.append({
            "sender" : sender,
            "reciever" : reciever,
            "amount" : amount
        })
        return self.last_block["index"] + 1
        

    def hash():
        pass
    
    def proof_of_work():
        pass

    def valid_proof():
        pass

    def register_node(self, address):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError("Please Enter a valid URL")
        

    def resolve_conflicts():
        pass

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n________\n")
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