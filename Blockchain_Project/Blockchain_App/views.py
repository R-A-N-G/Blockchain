from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest, request, response
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json, datetime
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

    def new_block(self, proof, previous_hash):
        block = {
            "index" : len(self.chain) + 1,
            "timestamp" : str(datetime.datetime.now()),
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
            "receiver" : reciever,
            "amount" : amount
        })
        next_block = self.last_block()
        return  next_block["index"] + 1
        

    def hash(self, block):
        block_string = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest()
         
    
    def proof_of_work(self, last_block):
        last_proof = last_block["proof"]

        print(last_proof)
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1
        return proof
        

    def valid_proof(self, last_proof, proof, last_hash):
        hash_operation  = hashlib.sha256(str(proof**2 - last_proof**2).encode()).hexdigest()
        return hash_operation[:4] == "0000"
        pass

    def register_node(self, address):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError("Please Enter a valid Node Address")
        

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
####_____This_Node_Address_____####
node_address = str(uuid4()).replace('-','')


def full_chain(request):
    if request.method == 'GET':
        response = {
                    'chain': blockchain.chain,
                    'length' : len(blockchain.chain),    
                    }
    return JsonResponse(response)


@csrf_exempt
def new_transcations(request):
    if request.method == "POST":
        values = json.loads(request.body)

        required = ['sender','receiver','amount']
        if not all (k in values for k in required):
            return "Some Values are Missing", 400
        index = blockchain.new_transactions(values['sender'], values['receiver'], values['amount'])

        response = {'message' : f'Your Trasaction will be added to Block {index}'}
        # print(blockchain.current_transactions)
    else: response = {'message' : 'Method Not Allowed'}
    return JsonResponse(response)


def mine(request):
    if request.method == 'GET':

        if len(blockchain.current_transactions) == 0:
            response = {    'message' : "No Transactions to Mine",   }
        else:
            last_block = blockchain.last_block()
            proof = blockchain.proof_of_work(last_block)

            blockchain.new_transactions(
                sender = '0',
                reciever = node_address,
                amount = 1,
            )

            previous_hash = blockchain.hash(last_block)
            block = blockchain.new_block(proof, previous_hash)
            # print(block)

            response = {
                'message' : 'New Block Forged',
                'index' : block['index'],
                'trnsaction' : block['transactions'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash'] 
            }
    else: response = {'message' : 'Method Not Allowed'}
    return JsonResponse(response)

def register_node():
    pass
    pass

def consensus():
    pass



####_____TEST__VIEW__git_____####
def test(request):
    if request.method == "GET":
        response = {'message': 'WORKING'}
    return JsonResponse(response)