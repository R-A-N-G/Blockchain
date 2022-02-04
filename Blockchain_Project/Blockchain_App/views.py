from tabnanny import check
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, request, response
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
import time
from time import ctime
from urllib.parse import urlparse
from uuid import uuid4
import requests
from collections import Counter



class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        self.node_id_list = set()

        #__The genesis block__#
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash):
        block = {
            "index" : len(self.chain) + 1,
            "timestamp" : time.time(),
            "transactions" : self.current_transactions,
            "proof": proof,
            "previous_hash" : previous_hash,
        }
        block['hash'] = self.hash(block) 
        self.current_transactions = []
        self.chain.append(block)
        return block


    def last_block(self):
        return self.chain[-1]
        

    def new_transaction(self, sender, reciever, amount):
        self.current_transactions.append({
            "sender" : sender,
            "receiver" : reciever,
            "amount" : amount
            # hash : "",
            # signature : "",
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
        print("****",parsed_url)
        # if parsed_url.netloc:
        #     self.nodes.add(parsed_url.netloc) ; print('1', parsed_url)
        # elif parsed_url.path:
        #     self.nodes.add(parsed_url.scheme) ; print('2', parsed_url.path)
        # else:
        #     raise ValueError("Please Enter a valid Node Address") ; print('3')
        self.nodes.add(address)
        neighbours = self.nodes
        print(">>>>>",neighbours)
        
        for node in neighbours:
            response = requests.get(f'http://{node}/p2p')
            a = str(node) + "-->>" + str(response.json()['message'])
            self.node_id_list.add(a)
        

        

    def resolve_conflicts(self):

        
        neighbours = self.nodes
        new_chain = None
        tests = [] ; l = []
        i = 0 ; new = None ; n = None
        max_length = len(self.chain)
        
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                # length = response.json()['length']
                length = response.json()['length']
                chain = response.json()['chain']
                t = (chain[-1])

                l.append(length)
                if len(set(l)) < len(l):
                    for i in range(len(l)):
                        if l[i] not in set(l):
                            l[i] = 0

                tests.append(t['timestamp'])
                
                print(l)
        
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    self.chain = new_chain
                    new_chain = chain

        i = tests.index(min(tests))
        n = list(neighbours)
        new = requests.get(f'http://{n[i]}/chain')

        print(self.valid_chain(new.json()['chain']))
        print("First one ", tests, +min(tests))
        # print(new.json()['chain'])

        if self.valid_chain(new.json()['chain']) and len(new.json()['chain']) == max_length:
            print(">>>>>>here>>>>>>>")
            self.chain = new.json()['chain']
            new_chain = chain
        
        if new_chain:
            # self.chain = new_chain
            return True

        return False

        

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]

            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block['hash']:
                return False 

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof'], last_block_hash):
                return False 

            last_block = block
            current_index += 1

        return True




####_____object_____####
blockchain = Blockchain()
####_____This_Node_Address_____####
node_address = str(uuid4()).replace('-','')


def full_chain(request):
    if request.method == 'GET':
        ret = []
        
        try:    
            for i in blockchain.chain:
                bc = i['transactions']
                for j in bc:
                    if j['sender'] == '0':
                        ret.append(j['receiver'])
        except: print(blockchain.chain)
        response = {
                    'receiver' : ret,
                    'length' : len(blockchain.chain), 
                    'chain': blockchain.chain,    
                    }
    return JsonResponse(response)


@csrf_exempt
def new_transcations(request):
    if request.method == "POST":
        values = json.loads(request.body)
        print("Time_Recieved >>>>",time.time())
        required = ['sender','receiver','amount']
        if not all (k in values for k in required):
            response = {'message' : 'Some Values are Missing'}
        
#_____________________________________***_________check siganture _________***________________________________________#

        else:    
            index = blockchain.new_transaction(values['sender'], values['receiver'], values['amount'])
            tx_no = len(blockchain.current_transactions)
            print(blockchain.current_transactions)
            response = {'message' : f'Your Trasaction will be added to Block {index} as {tx_no} transaction'}

        mine()
    else: response = {'message' : 'Method Not Allowed'}
    return JsonResponse(response)


def mine():

    if len(blockchain.current_transactions) == 0:
        response = {    'message' : "No Transactions to Mine",   }
    else:
        last_block = blockchain.last_block()
        proof = blockchain.proof_of_work(last_block)

        blockchain.new_transaction(
            sender = "-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDAoQKW8USQXAJptg1gnO8QuMAqvMBOcUJYlQAHKGtfE8S9iKKwlNFS0qhWG8/NHdeV9qxxlzn9r2IPPGeYGNo2CpLwkn/Jz+c+akfRH1wHn06qfXWgxPfRzNPQuGaZm3JtmqtxffboLPVebiKSz3/U7KQ77VFYydvTrD259mOtcwIDAQAB-----END PUBLIC KEY-----",
            reciever = node_address,
            amount = 1,
        )

        # previous_hash = blockchain.hash(last_block)
        previous_hash = last_block['hash']
        block = blockchain.new_block(proof, previous_hash)
        # print(block)

        response = {
            'message' : 'New Block Forged',
            'index' : block['index'],
            'trnsaction' : block['transactions'],
            'proof' : block['proof'],
            'previous_hash' : block['previous_hash'] 
        }
        print("mined_>>>>>>", time.time())
        neighbours = blockchain.nodes
        for node in neighbours:
            consensus = requests.get(f'http://{node}/nodes/resolve')



#_____________________________________***_________check for minier_________***________________________________________#
        time.sleep(3)
        check = blockchain.chain[-1]
        c_tx = check['transactions']
        tx_data = {}
        for i in c_tx:
            if i['receiver'] == node_address:
                j=0
                for i in c_tx:
                    j+=1
                    tx_data[f'{j}'] = f"{i['sender']}|{i['receiver']}|{i['amount']}"
                send_tx = requests.post("http://127.0.0.1:8000/transaction", data=tx_data)
            else: pass
            print(tx_data)
#_____________________***_________if minier is self: >>>> send transaction request_________***________________________#
        


    return JsonResponse(response)

@csrf_exempt
def register_node(request):
    if request.method == "POST":
        values = json.loads(request.body)
        nodes = values.get('nodes')
        print(nodes)
        if nodes is None:
            response = { 'message' : 'Error :- Invalid list of  nodes' }
        for node in nodes:
            blockchain.register_node(node)
        response = {
            'message' : 'new nodes added',
            'total nodes' : list(blockchain.node_id_list),
        }
        
    else: response = {'message' : 'Method Not Allowed'}
    return JsonResponse(response)
    

def consensus(request):
    if request.method == "GET":
        blockchain.current_transactions = []  
        neighbours = blockchain.nodes
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')
        replaced = blockchain.resolve_conflicts()
        response = {
            'message': 'Nodes conflict is resolved',
            'chain': blockchain.chain
        }
        blockchain.current_transactions = []    
    return JsonResponse(response)    


def P_2_P(request):
    if request.method == 'GET':
        

        response = {'message' : node_address}
    return JsonResponse(response)


####_____TEST__VIEW__get_____####
def test(request):
    if request.method == "GET":
        response = {'message': 'WORKING'}
    return JsonResponse(response)
