**This project is a proof of concept of an vehicle rental system uti-
lizing a web application and an associated blockchain to record the
rental transactions made. The aim is to achieve a trust-less, de-
centralized consensus. It involves mining the transaction block and
adding it to the chain once the transaction is completed. Data on
blockchain is kept secured and distributed on the network. This il-
lustrate practical applications of Blockchain technology in ways that
are easy to visualize and understand.
In the long term, we expect the combination of blockchain to en-
able innovative devices and business models. Blockchain is a tech-
nology that can help to unlock this piece of the puzzle. Disruptive
technologies such as big data and cloud computing have been lever-
aged by blockchain to overcome its limitations since its conception,
and we think blockchain will be one of the next ones.
Blockchain technology has a great future worldwide. An incredi-
ble scope of Blockchain technology has been observed in the finan-**



1.1 The Blockchain Application

The Blockchain Application is the application that will be running

on each decentralized device this is the application for the mining

nodes in the network, The application is built using Python Django

the application will have four methods as API endpoints for com-

pleting the transaction cycle.

Figure 4.8: Miners running Blockchain application

30



<a name="br32"></a> 

1\. Creating a peer to peer network with other nodes

running on the same network:- This for creating a network

where all the nodes can communicate with each other and resolve

their conﬂicts to ﬁnd the longest valid chain

2\. Accepting transaction request from the user:- This

functoion will have POST method that wiill accept JSON data

from the frontend in form of

{

sender: ””,

receiver: ””,

amount: ””

}

and create and add it to current awaiting transaction list.

Figure 4.9: Proof of Work Algorithm

3\. Mining:- The most important method in the transaction cycle

31



<a name="br33"></a> 

where each node will validate the transaction information as re-

ceived in the above function and after running a proof of work

algorithm using the last block proof and the hash of the current

block it will calculate the proof and hash of the current create a

block storing the same transaction information and adding trans-

actions in their own name as a reward for mining the particular

block

4\. The Consensus:- After a node has mined the particular trans-

action and added it to its own copy of the blockchain ledger, the

most important step is the resolve conﬂicts between all the nodes

in the network to get a single valid Blockchain, this is done by the

consensus method using the consensus algorithm . after mining

any block each node calls the resolve/conﬂict endpoint of each

node registered on its network, and with this all the nodes will

run a consent algorithm where they will call each node for their

chain and compare to which node has the longest-running valid

chain if a longer chain and valid chain is found every node will

replace their own copy with the longest one, so as to get a con-

sensus blockchain database, also if more than one longest as well

as a valid chain is present in the network i.e if more than one

node has mined the block in their name before calling consensus,

the algorithm will then compare the chain of the tghis node for

their timestamp to ﬁnd the ﬁrst node to mine that block. there-

fore the consensus algorithm will replace all the chain in-network

32



<a name="br34"></a> 

with the chain of the node that was fastest to run the proof of

work algorithm and mine the block, thus making a consistence

blockchain ledger where the reword of mining a block a partic-

ular block is given to only one node which will run the proof of

work algorithm the fastest.

1.2 The Wallet Application

The Wallet application will be a Django API which will work with

the user webpage frontend, as it will maintain a database of the list

of users with their login information, By providing login feature to

user it will also perform the following tasks.

Figure 4.10: The Wallet Application

33



<a name="br35"></a> 

1\. creating and managing users private and public key:-

One of the most important features of using a blockchain-based

transaction system is the Anominisity of user, which enables

higher security to the data stored, this is done by using public

private encryption and in this project, the wallet app will use

the RSA public-private key encryption. the wallet app will allow

users to be identiﬁed for making send or receive transactions

through their public key only making the system Anonymus, and

then every transaction will be encrypted using the receiver public

key making it unreadable to anyone but the receiver who can

decrypt it with their private key only to encrypt the transaction

information i.e

{

sender: ””,

receiver: ””,

amount: ””

}

will be encrypted using RSA algorithm and with the receivers

public key

2\. The digital Signature:-Other than making the transaction

system Anonymus and secured with the public-private key it is

also important to verify each transaction, that if it is from the

right sender and not request in senders name from a malicious

user. And the wallet app is going to achieve this by using RSA

digital signatures, which will use the hash of the transaction in-

formation and the private key of the sender which will be owned

34



<a name="br36"></a> 

by the sender only, to digitally sign the transaction information,

and the miners while mining the transaction to add it to a new

block can use the sender public key to check if the digital sig-

nature was indeed done using the private key only, making the

transaction veriﬁed.

1.3 User Webpage - Frontend

Deﬁnition: The part of a website that the user interacts with

directly is termed the front end. It is also referred to as the ‘client

side’ of the application. It includes everything that users experience

directly: text colors and styles, images, graphs and tables, buttons,

colors, and navigation menu. HTML, CSS, and JavaScript are the

languages used for Front End development. The structure, design,

behavior, and content of everything seen on browser screens when

websites, web applications, or mobile apps are opened up, is imple-

mented by front End developers. Responsiveness and performance

are two main objectives of the Front End. The developer must ensure

that the site is responsive i.e. it appears correctly on devices of all

sizes no part of the website should behave abnormally irrespective of

the size of the screen.

The user webpage will be a React Js frontend application which will

act as the interface between the user making the transaction request

and the blockchain network validating the transaction. It will also

35



<a name="br37"></a> 

allow the user to access the unlocking page of the IoT device after

getting the conﬁrmation of the transaction is valid and added to the

blockchain it will perform the following tasks.

1\. Maintain Login and Sign up of user:- The webpage will allow

a new user to create an account with the wallet app that will

create a public key and a private key for that particular user, to

make and sign transactions, and also login for a registered user

to access their public key and wallet balance.

2\. making transaction request:- The webpage will enable the user

to scan the QR code of a particular vehicle and make a trans-

action request in for of sender: ””, receiver: ””, amount: ””

which will then be sent to wallet app for digital signature and

to Blockchain network for validating, thus acting as the center

of the transaction cycle.

3\. selecting locations:- User can able to select journey start and

end location by interacting with live map. Just with one click

location will get selected for the process.

4\. Qr code scan:- User can able to scan qr code to verify the correct

vehicle . Qr code gives unique code for each vehicle so system

can easily identify unique vehicle.

1.4 Frontend design prototype

Before coding actual application design. Developer must need con-

36



<a name="br38"></a> 

Figure 4.11: Prototype design using Figma Application

Figure 4.12: Prototype wireframes

37



<a name="br39"></a> 

crete data of design. So the design prototypes allows developer to

design without any coding. For the project we used ﬁgma prototype

tool.

We also trys to make working wireframes for responsive designs.For

small screen device and for large screen device wireframes were de-

signed seperately.

38
