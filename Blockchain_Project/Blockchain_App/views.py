from email import message
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from inspect import signature
from tabnanny import check
from click import prompt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, request, response
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
import binascii
import time
from time import ctime
from urllib.parse import urlparse
from uuid import uuid4
from flask import Response
import requests
from collections import Counter
import ast
import pwinput
from hashlib import sha512

Key = b"-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDSXduJaq2xNGWwGIimwZDHvAkvls2SG4uuB6pTp+70PJc80Hwa\nththYprtYaw4dF1UKHnSVvuo1q+XbEXW727NTMZKH7PPN5Ajz4V6aOcTMjBwDD8H\nOUTHbdyiasQXlNYIqPxhBkmZWPqDhPq7n5voxTBe0xDXtWblU3RnpwUOqQIDAQAB\nAoGAFaIQRv/g78WvJV5IgzmJnXihSzMLXdiWUyW3ptWwtY4bkWXxNT//7dJZk0rF\njqKszFBDQtWuGI1HTl+UiQdjUeqSoYwvR6c3WvaJtaO7Y3DpWRc04yipKbtTDzAY\n2tMoAO9F0rn6MRTTXiLV0DJInZo5ksCnKO+hNlrPHp/bVU8CQQDXDvyIAhRpU7bz\nuCl36/NPXSIiKmi8OQzbR1AlSULVpOAT6P0SpVOaIMAcedGrX8JnBiN0FL7WMRum\nCu9u/uerAkEA+mo1O29p/h2mivt675zIPkNqww1BTzRlVa6oKyeSI8OMn9WvDkDY\nLVT894AFIO50svDbPcoHjwl/dDBERnW++wJBAIEvd3McDLbYmuX8kqx/CEF8aKyt\nXQz0GE0AoZxETemYiSJsqtkwhu/nDIAOjWyssVLB1To93AU+qqUrnHjIltECQQDj\nb4EnmTp4TW/MvTlb1VbdjheyTiCqElmTJ42fnFIT33CiXs6esHBnQ9B57jE6RrmB\nKFbH2O1ikWrMGWZ5ZEnvAkBNZwqX10HQp3QJ2LamMz2JmI+ujCikPOyddAyXIaIr\n0a9CaGO+UyePqcge2VG53rsheoA+kIiPabCukVxp1PHL\n-----END RSA PRIVATE KEY-----"
pubKey = RSA.import_key(Key).public_key()
privateKey = RSA.import_key(Key)
wallet_address = "127.0.0.1:8000"

class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()
        self.node_id_list = set()

        #__The genesis block__#
        self.new_block(previous_hash='1', proof=100, enc_tx_data="XXX")

    def new_block(self, proof, previous_hash, enc_tx_data):
        block = {
            "index" : len(self.chain) + 1,
            "timestamp" : time.time(),
            "transaction" : self.current_transactions,
            "transactions" : enc_tx_data,
            "proof": proof,
            "previous_hash" : previous_hash,
        }
        block['hash'] = self.hash(block) 
        self.current_transactions = []
        self.chain.append(block)
        return block


    def last_block(self):
        return self.chain[-1]
        

    def new_transaction(self, sender, reciever, amount, signature):
        self.current_transactions.append({
            "sender" : sender,
            "receiver" : reciever,
            "amount" : int(amount)-1,
            # hash : "",
            "signature" : signature,
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
        # print("****",parsed_url)
        # if parsed_url.netloc:
        #     self.nodes.add(parsed_url.netloc) ; print('1', parsed_url)
        # elif parsed_url.path:
        #     self.nodes.add(parsed_url.scheme) ; print('2', parsed_url.path)
        # else:
        #     raise ValueError("Please Enter a valid Node Address") ; print('3')
        self.nodes.add(address)
        neighbours = self.nodes
        # print(">>>>>",neighbours)
        
        # for node in neighbours:
        #     response = requests.get(f'http://{node}/p2p')
        #     a = str(node) + "-->>" + str(response.json()['message'])
        #     self.node_id_list.add(a)
        

        

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

        
    def check_signature(self,signature, key, msg):
        k = key.split(",")
        # print(k)
        # print(msg)
        e = int(k[1])
        n = int(k[0])
        hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
        hashFromSignature = pow(signature, e, n)

        return hash == hashFromSignature
        # return False

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


def login():
    global node_address

    print("Login with your Minier Account")
    email = input("e-mail : ")
    username = input("Username : ")
    password = pwinput.pwinput()
    domain = input("Enter Ypur IP Address")
    
    login_data = {
        'email' : email,
        'username' : username,
        'password' : password,
        'domain' : domain
    }

    minier_login = requests.post(f"http://{wallet_address}/login", data=login_data)

    mydata = ast.literal_eval(minier_login.content.decode("UTF-8"))
    node_address = mydata['public_key']
    node_address = str(node_address)
    
    # print(blockchain.nodes)
    domain = input("Enter Ypur IP Address")
    network = requests.post(f"http://{wallet_address}/p2p", data=domain)
    print("WELCOME MINIER :> ",node_address)



def join_network(request):
    if request.method == 'GET':

        
        domain = input("Enter Ypur IP Address")
        network = requests.post(f"http://{wallet_address}/p2p", data=domain)

        response = {
            "message" : "working"
        }
        # print(request.build_absolute_uri, request.QUERY_STRING)
    return JsonResponse(response)


def full_chain(request):
    if request.method == 'GET':

        response = {
                    'length' : len(blockchain.chain), 
                    'chain': blockchain.chain,    
                    }
    return JsonResponse(response)


@csrf_exempt
def new_transcations(request):
    if request.method == "POST":
        # values = json.loads(request.body)
        value = request.body
        # print(type(value))
        
        #_____________________________________***___________decrypting ____________***________________________________________#
        enc_tx_data = json.loads(value.decode())["enc_tx_data"].split("|")
        dec_tx_data = ""
        decryptor = PKCS1_OAEP.new(privateKey)
      
        for i in enc_tx_data:
            if not i:continue
            dec_tx_data += decryptor.decrypt(binascii.unhexlify(i.encode())).decode()
        values = json.loads(dec_tx_data)
        print(values)

        
        print("Time_Recieved >>>>",time.time())


        required = ['sender','receiver','amount', 'signature']
        if not all (k in values for k in required):
            response = {'message' : 'Some Values are Missing'}
            return JsonResponse(response)
        tx_data = {
            "sender":values["sender"],
            "receiver": values["receiver"],
            "amount": values["amount"]
        }

        #_____________________________________***_________check siganture _________***________________________________________#
        if blockchain.check_signature(values['signature'], values['sender'], json.dumps(tx_data).encode('utf-8')) == False:
            print("COULD NOT VERFY YOUR TRANSACTION")
            response = {'message' : 'COULD NOT VERFY YOUR TRANSACTION'}
            return JsonResponse(response)


        #_____________________________________***_________check balance _________***________________________________________#
        
        data = {
                "balance" : values["amount"],
                "sender" : values["sender"]
            }
        a = requests.post(f"http://{wallet_address}/checkbalance", data=data)
        
        a = a.content
        a = json.loads(a.decode('utf-8'))
        if a["message"] == "False":
            response = {'message' : "INSEFICIENT BALANCE"}
            print("INSEFICIENT BALANCE")
            return JsonResponse(response)
        
        else:    
            print(values['signature'])
            sender = values['sender']
            index = blockchain.new_transaction(values['sender'], values['receiver'], values['amount'],values['signature'])
            tx_no = len(blockchain.current_transactions)
            print(blockchain.current_transactions)
            
            mine(sender, enc_tx_data)
            
            response = {'message' : f'Your Trasaction will be added to Block {index} as {tx_no} transaction'}

    else: response = {'message' : 'Method Not Allowed'}
    # response = {'message' : 'Method Not Allowed'}
    return JsonResponse(response)



def mine(sender, value):

    if len(blockchain.current_transactions) == 0:
        response = {    'message' : "No Transactions to Mine",   }
    else:
        last_block = blockchain.last_block()
        proof = blockchain.proof_of_work(last_block)
        m_tx_data = {
            "sender":sender,
            "receiver": node_address,
            "amount": 2
        }
        k = node_address.split(",")
        d = int(k[2])
        n = int(k[0])
        msg = json.dumps(m_tx_data).encode('utf-8')           
        hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
        signature = pow(hash, d, n)

        blockchain.new_transaction(
            sender = sender,
            reciever = node_address,
            amount = 2,
            signature = signature
        )

        # previous_hash = blockchain.hash(last_block)
        previous_hash = last_block['hash']
        block = blockchain.new_block(proof, previous_hash, "".join(value))
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
        c_tx = check['transaction']
        tx_data = {}
        for i in c_tx:
            if i['receiver'] == node_address:
                j=0
                for i in c_tx:
                    j+=1
                    tx_data[f'{j}'] = f"{i['sender']}|{i['receiver']}|{i['amount']}"
                send_tx = requests.post(f"http://{wallet_address}/transaction/conformation", data=tx_data)
                # send_tx = requests.post("http://192.168.0.102:8000/transaction/conformation", data=tx_data)
                
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
            'total nodes' : list(blockchain.nodes),
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
