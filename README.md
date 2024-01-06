<a name="br1"></a> 

Project Synopsis

on

Blockchain Based Secured Vehicle Rental

Project

Submitted in partial fulﬁllment of the requirement of degree of Bachelor of

Engineering by:

Akshat Shirsat

Nishant Chavan

Rahul Chakravorty

Giribabu Anisetti

Under the guidance of

Mr.Vaibhav Palav

LOKMANYA TILAK COLLEGE OF ENGINEERING

Aﬃliated to

UNIVERSITY OF MUMBAI

Department of Electronics and Telecommunication

Engineering Academic Year 2021-22



<a name="br2"></a> 

LOKMANYA TILAK COLLEGE OF ENGINEERING

UNIVERSITY OF MUMBAI

2021-22

Department of Electronics and Telecommunication

Synopsis

1\. AKSHAT SHIRSAT

2\. NISHANT CHAVAN

3\. RAHUL CHAKRAVORTY

4\. GIRIBABU ANISETTI

Course : B.E. (Electronics and Telecommunication)

Title of the project : Blockchain Based Secured Vehicle Rental Project

Project Guide : Mr. Vaibhav Palav

Date :

1



<a name="br3"></a> 

CERTIFICATE

This to certify that Akshat Shirsat, Nishant Chavan, Rahul Chakra-

vorty, Giribabu Anisetti ,have delivered presentation for Project on

“Blockchain Based Secured Vehicle Rental Project” and submitted

a report in the Lokmanya Tilak College of Engineering, Navi Mum-

bai for the partial fullment of the degree of B.E in Electronics and

Telecommunication Engineering from University of Mumbai, for the

year 2021-22.

Mr.Vaibhav Palav

Dr.Ravindra Duche

Dr. Vivek Sunnapwar

(Project Guide)

(Head of Department)

(Principle)

External Examiner :

2



<a name="br4"></a> 

ACKNOWLEDGEMENT

We would like to acknowledge and extend our heartfelt gratitude to

all those people who have been associated with this Project and have

helped us with it thus making it a worthwhile experience. Firstly

we extend our thanks to various people which include our Project

Guide Mr.Vaibhav Palav who has shared her opinion and experi-

ences through which we received the required information crucial

for our project synopsis. I am also thankful to Head of Depart-

ment Dr.Ravindra Duche and all the staﬀ members of Electronics

and Telecommunication Department for their highly co-operative and

encouraging attitudes, which have always boosted us. We also take

this opportunity with great pleasure to thank our Principal Dr.Vivek

Sunnapwar whose timely support and encouragement has helped us

succeed in our venture.

name of candidates:

1\. Akshat Shirsat

2\. Nishant Chavan

3\. Rahul Chakravorty

4\. Giribabu Anisetti

3



<a name="br5"></a> 

ABSTRACT

In past few years, technologies like blockchain and smart ledgers

are gaining popularity due to the emergence of crypto currencies,

such as Bitcoin and Ethereum. In a centralized architecture the

stored data can be modiﬁed easily and it is prone to various security

threats. To overcome the aforementioned issues, we have proposed

a system based on the integration of blockchain in order to increase

the security. Blockchain is a distributed, decentralized ledger and

immutable in nature.

For the automotive industry, promoting more value-adding ser-

vices in usage stage is a long-standing challenge for global manufac-

turers. As many cars have an unknown history, it is proven diﬃcult,

if not impossible, to prevent scams and frauds when oﬀering car ser-

vices. As an emerging technology, blockchain is characterized by high

immutability, transparency, security, and traceability. Such charac-

teristics make blockchain a highly promising empowering technology

to maintain mutual trust among stakeholders in vehicle product-

service system (PSS).

4



<a name="br6"></a> 

Contents

[1](#br10)[ ](#br10)[Introduction](#br10)

9

11

13

[2](#br12)[ ](#br12)[Scope](#br12)[ ](#br12)[of](#br12)[ ](#br12)[project](#br12)

[3](#br14)[ ](#br14)[Literature](#br14)[ ](#br14)[survey](#br14)

[3.1](#br14)[ ](#br14)[Referred](#br14)[ ](#br14)[paper](#br14)[ ](#br14)[1](#br14)[ ](#br14). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

[3.2](#br16)[ ](#br16)[Referred](#br16)[ ](#br16)[paper](#br16)[ ](#br16)[2](#br16)[ ](#br16). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

[3.3](#br18)[ ](#br18)[Referred](#br18)[ ](#br18)[paper](#br18)[ ](#br18)[3](#br18)[ ](#br18). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

[3.4](#br19)[ ](#br19)[Referred](#br19)[ ](#br19)[paper](#br19)[ ](#br19)[4](#br19)[ ](#br19). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

[4](#br20)[ ](#br20)[Methodology](#br20)

19

[4.1](#br20)[ ](#br20)[Gathering](#br20)[ ](#br20)[Information](#br20)[ ](#br20). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

[4.1.1](#br20)[ ](#br20)[Blockchain](#br20)[ ](#br20)[Consensus](#br20)[ ](#br20)[Mechanism](#br20)[ ](#br20). . . . . . . . . . . . . . . . . . . . 19

[4.1.2](#br22)[ ](#br22)[Peer-to-peer](#br22)[ ](#br22)[Network](#br22)[ ](#br22). . . . . . . . . . . . . . . . . . . . . . . . . . . 21

[4.1.3](#br23)[ ](#br23)[Digital](#br23)[ ](#br23)[Signature](#br23)[ ](#br23). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

[4.1.4](#br24)[ ](#br24)[RSA](#br24)[ ](#br24)[Algorithm](#br24)[ ](#br24)[for](#br24)[ ](#br24)[Cryptography](#br24)[ ](#br24). . . . . . . . . . . . . . . . . . . . 23

[4.1.5](#br25)[ ](#br25)[Web](#br25)[ ](#br25)[Application](#br25)[ ](#br25)[development](#br25)[ ](#br25)[technology](#br25)[ ](#br25). . . . . . . . . . . . . . . . 24

[4.2](#br31)[ ](#br31)[Proper](#br31)[ ](#br31)[planning](#br31)[ ](#br31). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

[4.2.1](#br31)[ ](#br31)[The](#br31)[ ](#br31)[Blockchain](#br31)[ ](#br31)[Application](#br31)[ ](#br31). . . . . . . . . . . . . . . . . . . . . . . 30

[4.2.2](#br34)[ ](#br34)[The](#br34)[ ](#br34)[Wallet](#br34)[ ](#br34)[Application](#br34)[ ](#br34). . . . . . . . . . . . . . . . . . . . . . . . . . 33

[4.2.3](#br36)[ ](#br36)[User](#br36)[ ](#br36)[Webpage](#br36)[ ](#br36)[-](#br36)[ ](#br36)[Frontend](#br36)[ ](#br36). . . . . . . . . . . . . . . . . . . . . . . . 35

[4.2.4](#br37)[ ](#br37)[Frontend](#br37)[ ](#br37)[design](#br37)[ ](#br37)[prototype](#br37)[ ](#br37). . . . . . . . . . . . . . . . . . . . . . . . 36

[4.3](#br40)[ ](#br40)[Flowchart](#br40)[ ](#br40). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

[4.3.1](#br40)[ ](#br40)[Transaction](#br40)[ ](#br40)[Life](#br40)[ ](#br40)[Cycle](#br40)[ ](#br40). . . . . . . . . . . . . . . . . . . . . . . . . . 39

[4.3.2](#br42)[ ](#br42)[Flow](#br42)[ ](#br42)[of](#br42)[ ](#br42)[The](#br42)[ ](#br42)[Project](#br42)[ ](#br42). . . . . . . . . . . . . . . . . . . . . . . . . . . 41

[5](#br43)[ ](#br43)[Implementations](#br43)

42

5



<a name="br7"></a> 

[6](#br48)[ ](#br48)[Results](#br48)[ ](#br48)[and](#br48)[ ](#br48)[Discussion](#br48)

47

[6.1](#br48)[ ](#br48)[User](#br48)[ ](#br48)[interaction](#br48)[ ](#br48)[with](#br48)[ ](#br48)[application](#br48)[ ](#br48). . . . . . . . . . . . . . . . . . . . . . . . 47

[6.1.1](#br49)[ ](#br49)[Log](#br49)[ ](#br49)[in](#br49)[ ](#br49)[and](#br49)[ ](#br49)[Sign](#br49)[ ](#br49)[up](#br49)[ ](#br49)[form](#br49)[ ](#br49). . . . . . . . . . . . . . . . . . . . . . . . . 48

[6.1.2](#br51)[ ](#br51)[Home](#br51)[ ](#br51)[landing](#br51)[ ](#br51)[page](#br51)[ ](#br51)[of](#br51)[ ](#br51)[application](#br51)[ ](#br51). . . . . . . . . . . . . . . . . . . . 50

[6.1.3](#br52)[ ](#br52)[Select](#br52)[ ](#br52)[destination](#br52)[ ](#br52)[location](#br52)[ ](#br52). . . . . . . . . . . . . . . . . . . . . . . . 51

[6.1.4](#br53)[ ](#br53)[Scan](#br53)[ ](#br53)[Qr](#br53)[ ](#br53)[code](#br53)[ ](#br53)[and](#br53)[ ](#br53)[unlock](#br53)[ ](#br53)[the](#br53)[ ](#br53)[vehicle](#br53)[ ](#br53). . . . . . . . . . . . . . . . . . 52

[6.1.5](#br54)[ ](#br54)[Deposit](#br54)[ ](#br54)[amount](#br54)[ ](#br54)[for](#br54)[ ](#br54)[charge](#br54)[ ](#br54)[fee](#br54)[ ](#br54)[and](#br54)[ ](#br54)[unlock](#br54)[ ](#br54)[vehicle](#br54)[ ](#br54). . . . . . . . . . . 53

[6.1.6](#br55)[ ](#br55)[Process](#br55)[ ](#br55)[after](#br55)[ ](#br55)[reaching](#br55)[ ](#br55)[destination](#br55)[ ](#br55). . . . . . . . . . . . . . . . . . . . 54

[6.1.7](#br57)[ ](#br57)[Blockchain](#br57)[ ](#br57)[data](#br57)[ ](#br57)[page](#br57)[ ](#br57)[for](#br57)[ ](#br57)[miners](#br57)[ ](#br57). . . . . . . . . . . . . . . . . . . . . 56

[7](#br59)[ ](#br59)[Conclusion](#br59)

[8](#br60)[ ](#br60)[References](#br60)

58

59

6



<a name="br8"></a> 

List of Figures

[4.1](#br21)[ ](#br21)[Blockchain](#br21)[ ](#br21)[consensus](#br21)[ ](#br21). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

[4.2](#br23)[ ](#br23)[Digital](#br23)[ ](#br23)[signature](#br23)[ ](#br23). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

[4.3](#br24)[ ](#br24)[RSA](#br24)[ ](#br24)[alogorithm](#br24)[ ](#br24). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

[4.4](#br26)[ ](#br26)[Node](#br26)[ ](#br26)[js](#br26)[ ](#br26)[download](#br26)[ ](#br26)[site](#br26)[ ](#br26). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

[4.5](#br27)[ ](#br27)[React](#br27)[ ](#br27)[JS](#br27)[ ](#br27). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

[4.6](#br28)[ ](#br28)[Redux](#br28)[ ](#br28). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

[4.7](#br29)[ ](#br29)[Sass](#br29)[ ](#br29). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

[4.8](#br31)[ ](#br31)[Miners](#br31)[ ](#br31)[running](#br31)[ ](#br31)[Blockchain](#br31)[ ](#br31)[application](#br31)[ ](#br31). . . . . . . . . . . . . . . . . . . . . 30

[4.9](#br32)[ ](#br32)[Proof](#br32)[ ](#br32)[of](#br32)[ ](#br32)[Work](#br32)[ ](#br32)[Algorithm](#br32)[ ](#br32). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

[4.10](#br34)[ ](#br34)[The](#br34)[ ](#br34)[Wallet](#br34)[ ](#br34)[Application](#br34)[ ](#br34). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

[4.11](#br38)[ ](#br38)[Prototype](#br38)[ ](#br38)[design](#br38)[ ](#br38)[using](#br38)[ ](#br38)[Figma](#br38)[ ](#br38)[Application](#br38)[ ](#br38). . . . . . . . . . . . . . . . . . . 37

[4.12](#br38)[ ](#br38)[Prototype](#br38)[ ](#br38)[wireframes](#br38)[ ](#br38). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

[4.13](#br41)[ ](#br41)[Transaction](#br41)[ ](#br41)[Life](#br41)[ ](#br41)[Cycle](#br41)[ ](#br41). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

[4.14](#br42)[ ](#br42)[Flow](#br42)[ ](#br42)[of](#br42)[ ](#br42)[The](#br42)[ ](#br42)[Project](#br42)[ ](#br42). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

[5.1](#br43)[ ](#br43)[Miners](#br43)[ ](#br43)[Logging](#br43)[ ](#br43)[in](#br43)[ ](#br43)[and](#br43)[ ](#br43)[joining](#br43)[ ](#br43)[p2p](#br43)[ ](#br43)[network](#br43)[ ](#br43). . . . . . . . . . . . . . . . . . . 42

[5.2](#br44)[ ](#br44)[Mining](#br44)[ ](#br44)[and](#br44)[ ](#br44)[creating](#br44)[ ](#br44)[new](#br44)[ ](#br44)[Blocks](#br44)[ ](#br44). . . . . . . . . . . . . . . . . . . . . . . . . 43

[5.3](#br44)[ ](#br44)[Algorithm](#br44)[ ](#br44)[for](#br44)[ ](#br44)[Decrypting](#br44)[ ](#br44)[and](#br44)[ ](#br44)[validating](#br44)[ ](#br44)[Signature](#br44)[ ](#br44). . . . . . . . . . . . . . 43

[5.4](#br45)[ ](#br45)[Wallet](#br45)[ ](#br45)[Application](#br45)[ ](#br45)[Creating](#br45)[ ](#br45)[P2P](#br45)[ ](#br45)[network](#br45)[ ](#br45). . . . . . . . . . . . . . . . . . . 44

[5.5](#br46)[ ](#br46)[Algorithm](#br46)[ ](#br46)[for](#br46)[ ](#br46)[creating](#br46)[ ](#br46)[Signature](#br46)[ ](#br46)[and](#br46)[ ](#br46)[Encryption](#br46)[ ](#br46). . . . . . . . . . . . . . . 45

[5.6](#br47)[ ](#br47)[Wallet](#br47)[ ](#br47)[Application](#br47)[ ](#br47)[creating](#br47)[ ](#br47)[and](#br47)[ ](#br47)[publishing](#br47)[ ](#br47)[Transactions](#br47)[ ](#br47). . . . . . . . . . . 46

[6.1](#br49)[ ](#br49)[Login](#br49)[ ](#br49)[Page](#br49)[ ](#br49). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48

[6.2](#br50)[ ](#br50)[Sign](#br50)[ ](#br50)[Up](#br50)[ ](#br50)[page](#br50)[ ](#br50). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

[6.3](#br51)[ ](#br51)[User](#br51)[ ](#br51)[Dashboard](#br51)[ ](#br51)[(after](#br51)[ ](#br51)[logging](#br51)[ ](#br51)[in)](#br51)[ ](#br51). . . . . . . . . . . . . . . . . . . . . . . . 50

[6.4](#br52)[ ](#br52)[Select](#br52)[ ](#br52)[Location](#br52)[ ](#br52)[of](#br52)[ ](#br52)[destination](#br52)[ ](#br52). . . . . . . . . . . . . . . . . . . . . . . . . . 51

[6.5](#br53)[ ](#br53)[Scanning](#br53)[ ](#br53)[QR](#br53)[ ](#br53)[code](#br53)[ ](#br53)[from](#br53)[ ](#br53)[vehicle](#br53)[ ](#br53)[(i)](#br53)[ ](#br53). . . . . . . . . . . . . . . . . . . . . . . 52

[6.6](#br53)[ ](#br53)[Scanning](#br53)[ ](#br53)[QR](#br53)[ ](#br53)[code](#br53)[ ](#br53)[from](#br53)[ ](#br53)[vehicle](#br53)[ ](#br53)[(ii)](#br53)[ ](#br53). . . . . . . . . . . . . . . . . . . . . . . 52

[6.7](#br54)[ ](#br54)[Creating](#br54)[ ](#br54)[Transaction](#br54)[ ](#br54)[for](#br54)[ ](#br54)[booking](#br54)[ ](#br54). . . . . . . . . . . . . . . . . . . . . . . . 53

7



<a name="br9"></a> 

[6.8](#br54)[ ](#br54)[Successful](#br54)[ ](#br54)[Completion](#br54)[ ](#br54)[of](#br54)[ ](#br54)[transaction](#br54)[ ](#br54)[(i)](#br54)[ ](#br54). . . . . . . . . . . . . . . . . . . . 53

[6.9](#br55)[ ](#br55)[Successful](#br55)[ ](#br55)[Completion](#br55)[ ](#br55)[of](#br55)[ ](#br55)[transaction](#br55)[ ](#br55)[(ii)](#br55)[ ](#br55). . . . . . . . . . . . . . . . . . . . 54

[6.10](#br55)[ ](#br55)[Steps](#br55)[ ](#br55)[to](#br55)[ ](#br55)[return](#br55)[ ](#br55)[vehicle](#br55)[ ](#br55)[after](#br55)[ ](#br55)[use](#br55)[ ](#br55)[(i)](#br55)[ ](#br55). . . . . . . . . . . . . . . . . . . . . . . 54

[6.11](#br56)[ ](#br56)[Steps](#br56)[ ](#br56)[to](#br56)[ ](#br56)[return](#br56)[ ](#br56)[vehicle](#br56)[ ](#br56)[after](#br56)[ ](#br56)[use](#br56)[ ](#br56)[(ii)](#br56)[ ](#br56). . . . . . . . . . . . . . . . . . . . . . . 55

[6.12](#br57)[ ](#br57)[Blockchain](#br57)[ ](#br57)[with](#br57)[ ](#br57)[transaction](#br57)[ ](#br57)[data](#br57)[ ](#br57)[and](#br57)[ ](#br57)[hashes,](#br57)[ ](#br57)[stored](#br57)[ ](#br57)[on](#br57)[ ](#br57)[each](#br57)[ ](#br57)[node](#br57)[ ](#br57)[(encrypted)](#br57)[ ](#br57)56

[6.13](#br58)[ ](#br58)[Decrypting](#br58)[ ](#br58)[Blockchain](#br58)[ ](#br58)[Data](#br58)[ ](#br58)[using](#br58)[ ](#br58)[Receivers](#br58)[ ](#br58)[Private](#br58)[ ](#br58)[key](#br58)[ ](#br58). . . . . . . . . . . 57

8



<a name="br10"></a> 

Chapter 1

Introduction

On many occasions, working professional’s person want to com-

mute to small distance or maybe diﬀerent parts of the city in the

same d ay. Usually they hire auto rickshaw, cab, bus or train that

consumes lots of energy and also pollute the environment. In case of

auto rickshaw charges lot for waiting. Most of these hiring vehicles

don’t have digital payment services with highest security.

Our rental cycles are mostly installed near the bus stops, railway

stations, airports etc. Our rental vehicle system is Blockchain based.

Which Provides you with best Security and connectivity with our web

application and payment system. Which is eco-friendly and beneﬁt

to health as well.

Our Blockchain based transaction provides you with safe and se-

cure transaction with no data breaching or data leaking.Blockchain

system also provide with fast performance.

It is diﬃcult to maintain trust among the travel agency and the

customers. Although there are many existing solutions in the re-

search that addresses the trust issues, but most of the solutions are

based on centralized architecture such as cloud computing where the

data is prone to various security threats. Motivated by the afore-

mentioned discussion, we have proposed a vehicle tracking system

based on the integration of blockchain in our project. The proposed

system will increase the trust among the entities by providing them

transparency in tracking details of the vehicle. As the trip details

9



<a name="br11"></a> 

are immutable and decentralized in nature, so, blockchain is used to

store the details.

Looking at our current scenario health and environment are most

important thing to be saved, here with our blockchain based rent sys-

tem take care of it. Our system promotes ‘stayFitWithCycling’ ‘Dig-

italIndia’ ‘Atmanirbhar’.Our We b application provides user friendly

Interface which is very easy to use and if facing any problem then

our Help desk articles and customer care service provider solves your

problem and provide with solutions.

10



<a name="br12"></a> 

Chapter 2

Scope of pro ject

This project is a proof of concept of an vehicle rental system uti-

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

ble scope of Blockchain technology has been observed in the ﬁnan-

11



<a name="br13"></a> 

cial ﬁeld. The ﬁnancial organizations were not able to suﬃciently

handle the heavy workload after demonetization and thus brought

out the problems of having a centralized specialist for handling the

ﬁnancial transactions. As a result, the RBI is inspiring banks to

encourage digitization. They have also released a statement which

emphasized the probability of Blockchain to ﬁght faking and the

chances of bringing about particular modiﬁcations in the working of

ﬁnancial markets, collateral identiﬁcation and payment system. In-

corporating Blockchain with ﬁnancial transactions gives out amazing

beneﬁts, such as a signiﬁcant amount of time and money could be

saved, including a drastic reduction in time needed for processing and

validating transactions. The blockchain functions on a distributed

database which make the operations smoothly, ensuring tight secu-

rity, and made it safe from cyber-attacks.This technology helps to

improve the security of existing real-world applications.

12



<a name="br14"></a> 

Chapter 3

Literature survey

3\.1 Referred paper 1

Blockchain Based Car-Sharing Platform

Article by Faculty of Informatics and Information, TechnologiesSlovak University

of Technology in Bratislava

From this paper, we understood that due to immense growth in

car-sharing market and as a result it has become even more popular

than car ownership. However, a classic car sharing system is based on

a centralized database server which can often lead to hacker attacks

or password leaks. Moreover, in a classic car-sharing system, the

customers’ data can be misused by owners of the cars. The best

solution that can be derived from this problematic issue from a lot

of use cases, is to use blockchain technology.

Blockchain as decentralized, immutable, public ledger provides the

customers with security that is impossible to tamper. The aim of the

proposed solution is to create and implement peer-to-peer short term

13



<a name="br15"></a> 

car-sharing application based on blockchain technology and smart

contracts. The key novelty of the paper was introducing a peer-to-

peer car sharing service without a central authority.

14



<a name="br16"></a> 

3\.2 Referred paper 2

Web 3.0 Technologies and It’s Signiﬁcance in Business.

Article on Tristate technology, Hiren Patel

From this paper, we understood that as the web is entering a novel

phase of development which is persistent and brings enormous ad-

vantages to the world. There has been much deliberate debate on

these web developments throughout the globe. “Web 3.0” refers to

a third generation Internet-based services that collectively comprise

what might be called ‘the intelligent Web’ — such as those using

semantic web, micro-formats, natural language search, data-mining,

machine learning, recommendation agents, and artiﬁcial intelligence

technologies — which emphasize machine-facilitated understanding

of information in order to provide a more productive and intuitive

user experience.

According to Garrigos-Simon, Lapiedra-Alcam´ı and Ribera (2012),

Web 3.0 means that “intelligent machines can read, understand, in-

terrelate and manipulate data from cyberspace, allowing this pro-

cess to be adapted by diﬀerent users or ﬁrms according to their own

needs”. In other words, there is a vast amount of data out there in

cyberspace. To day’s technology allows users to access, adapt, recon-

ﬁgure and utilize this to meet their unique requirements. In the due

course of time, We b 3.0 deﬁnition expanded as a third-generation of

the Web enabled by the convergence of several key emerging technol-

15



<a name="br17"></a> 

ogy trends: a) broadband adoption; b) Mobile Internet access, and

c) Mobile devices. The We b 3.0 will be more connected, open, and

intelligent, with semantic We b technologies, distributed databases,

natural language processing, machine learning, machine reasoning,

and autonomous agents (Garc´ıa, 2008). Lee (2006) said, “people

keep asking what We b 3.0 is and the We b is only going to get more

revolutionary”.

16



<a name="br18"></a> 

3\.3 Referred paper 3

A Review of Blockchain Technology and Its Applica-

tions in the Business Environment.

Elec-tronics and Mobile Communication Conference (IEMCON), (Vancouver,Canada),

pp. 1–5, IEEE, 2018.

From this paper, we understood that the technology that can lead

to signiﬁcant changes in our business environment and will have great

impact on the next few decades is Blockchain technology. It can

change the way we perceive business processes, and can transform

our economy. Blockchain is a decentralized and distributed ledger

technology that aims to ensure transparency, data security and in-

tegrity, since it cannot be tampered or forged during attacks. Most

of the current research related to Blockchain Technology is focusing

on its application for cryptocurrencies, such as Bitcoin and only a

limited number of research is targeted at exploring the utilization of

Blockchain Technology in other environments or sectors.

Blockchain Technology is more than just cryptocurrency, and it

can have several applications in government, ﬁnance and banking

industry, accounting and Business Process Management. Therefore,

this study attempts to investigate and explore its opportunities and

challenges for the current or future applications of Blockchain Tech-

nology. Thus, a large number of published studies were carefully re-

viewed and analyzed based on their contributions to the Blockchain.

17



<a name="br19"></a> 

3\.4 Referred paper 4

Public Vs Private Blockchain In A Nutshell

Medium website article - Demino

From this paper, we understood the diﬀerences between a public

blockchain and a private blockchain. A Public Blockchain is a permis-

sionless blockchain. Anyone can join the blockchain network, mean-

ing that they can read, write, or participate with a public blockchain.

Public blockchains are decentralised, no one has control over the net-

work, and they are secure in that the data can’t be changed once val-

idated on the blockchain. On the other hand, a Private Blockchain is

a permissioned blockchain. Permissioned networks place restrictions

on who is allowed to participate in the network and in what trans-

actions.

Normally, we hear about public versus private blockchains. One

factor that often gets left out is also the idea of an open versus closed

blockchain. And it’s important to consider both parameters, so you

know which possible solutions are good for your idea. When we talk

about public blockchains, what most people are really talking about

is a public open blockchain. It’s a blockchain where anybody can

write data to the blockchain, and anybody else can come and read

that data.

18



<a name="br20"></a> 

Chapter 4

Methodology

In our project we have used many arithematic algorithms for se-

curity of data and latest application development technology such as

Blockchain libraries, python language libraries,RSA algorithm, peer-

to-peer network technology.Those are explained in detail below:

4\.1 Gathering Information

All the necessary information and study research we have gathered

for the project were discribed here.

4\.1.1 Blockchain Consensus Mechanism

A wide variety of consensus mechanisms has appeared, each hav-

ing its own way of deciding the next valid block. We have identiﬁed

the following ﬁve high-level categories: Computational power based,

stake based, disk space based, time based, and user based consensus

mechanisms. Bitcoin’s proof of work (PoW) and it’s variants are well

19



<a name="br21"></a> 

Figure 4.1: Blockchain consensus

known examples of computational power based mechanisms. (Valli-

vaara et al. 2017)

Compared to computational power based consensus mechanisms

that make use of an external resource, stake based voting requires a

cryptocurrency’s internal resource, namely coins. The main idea is

that, in contrast to PoW, selecting a random node does not require

a large amount of resources. The basic idea is that the participant

with the most coins has the largest chance to vote for the next block.

Peercoin uses Proof of Stake and also Ethreum platform has decided

to switch from PoW to staked based Casper. (Sameeh 2017)

20



<a name="br22"></a> 

The main idea in the disk space voting is to use memory in the

computer as resource for consensus voting. The main beneﬁts for this

is to tackle the PoW’s energy consumption issues. Time based voting

doesn’t consume so much resources as the previously introduced con-

sensus mechanisms. It achieves the consensus by randomizing who

can choose the next block by using the time as deciding factor. In

the user based consensus system, the users decide who of the them

is the next validator of the block.

4\.1.2 Peer-to-peer Network

The Bitcoin Network is Peer-2-Peer (P2P) network. Figure 2 pre-

sented also the topology of P2P network. The Bitcoin Network is

run by nodes which collectively validate the information submitted

by other nodes.

The process is as follows (Nakamoto, 2008):

1\. New transactions are broadcast to all nodes.

2\. Each node collects new transactions into a block.

3\. Each node works on ﬁnding a diﬃcult proof-of-work for its block.

4\. When a node ﬁnds a proof-of-work, it broadcasts the block to

all nodes.

5\. Nodes accept the block only if all transactions in it are valid and

not already spent.

21



<a name="br23"></a> 

Figure 4.2: Digital signature

6\. Nodes express their acceptance of the block by working on cre-

ating the next block in the chain, using the hash of the accepted

block as the previous hash.

Following ﬁgure illustrates the process as practical money transfer

example (Financial Times, 2015).

4\.1.3 Digital Signature

Public key cryptography is a framework where a key pair is gener-

ated and then used to control the access to information. Public ke y,

as the name states, can be publicly available to anyone, whereas pri-

vate key must be kept secret by the owner. The owner of the private

key can use the key to sign any message after which anybody who

knows the public key can verify that the signature attached to the

message is valid. It is therefore possible to verify that the messages

with digital signature have been written by a person who knows the

matching private ke y. Following ﬁgure presents the fundamentals

of public key cryptography utilization in digital signatures (Driscoll,

22



<a name="br24"></a> 

Figure 4.3: RSA alogorithm

2013).

Bitcoin uses the public key cryptography in a novel way: Bitcoin

address is essentially a public key and anybody knowing the match-

ing private key can unlock any funds associated to it. Bitcoin public

key can be associated to a bank account and the matching private

key to its password, albeit many long term cypherpunks shun this

comparison as it’s not 100 accurate.

4\.1.4 RSA Algorithm for Cryptography

RSA algorithm is asymmetric cryptography algorithm. Asymmet-

ric actually means that it works on two diﬀerent keys i.e. Public Key

and Private Key. As the name describes that the Public Key is given

to everyone and Private key is kept private.

23



<a name="br25"></a> 

An example of asymmetric cryptography :

A client (for example browser) sends its public key to the server

and requests for some data. The server encrypts the data using

client’s public key and sends the encrypted data. Client receives this

data and decrypts it. Since this is asymmetric, nobody else except

browser can decrypt the data even if a third party has public key of

browser.

The idea of RSA is based on the fact that it is diﬃcult to factorize

a large integer. The public key consists of two numbers where one

number is multiplication of two large prime numbers. And private

key is also derived from the same two prime numbers. So if some-

body can factorize the large number, the private key is compromised.

Therefore encryption strength totally lies on the key size and if we

double or triple the key size, the strength of encryption increases ex-

ponentially. RSA keys can be typically 1024 or 2048 bits long, but

experts believe that 1024 bit keys could be broken in the near future.

But till now it seems to be an infeasible task.

4\.1.5 Web Application development technology

Node js:- Node js is a javascript runtime built on chrome’s V8

Javascript engine. As an asynchronous event-driven JavaScript run-

time, Node js is designed to build scalable network applications. In

the following ”hello world” example, many connections can be han-

dled concurrently. Upon each connection, the callback is ﬁred, but if

24



<a name="br26"></a> 

Figure 4.4: Node js download site

there is no work to be done, Node js will sleep.This is in contrast to

today’s more common concurrency model, in which OS threads are

employed. Thread-based networking is relatively ineﬃcient and very

diﬃcult to use.

Furthermore, users of Node.js are free from worries of dead-locking

the process, since there are no locks. Almost no function in Node.js

directly performs I/O, so the process never blocks except when the

I/O is performed using synchronous methods of Node.js standard li-

brary. Because nothing blocks, scalable systems are very reasonable

to develop in Node js. Downloading and installation process is very

simple...

Reactjs:- A JavaScript library for building user interfaces. React

25



<a name="br27"></a> 

Figure 4.5: React JS

has been designed from the start for gradual adoption, and you can

use as little or as much react as you need. Whether you want to

get a taste of react, add some interactivity to a simple HTML page,

or start a complex React-powered app. Installation process of react

library is very simple. Just go to any ﬁle directory from you terminal

and ﬁre a command.

npx create-react-app my-app

cd my-app

and then to run the program type npm start make sure you have

installed nodejs in you system.

Create React App doesn’t handle backend logic or databases; it

just creates a frontend build pipeline, so you can use it with any

backend you want. Under the hood, it uses Babel and webpack, but

you don’t need to know anything about them.

When you’re ready to deploy to production, running npm run

build will create an optimized build of your app in the build folder.

26



<a name="br28"></a> 

Figure 4.6: Redux

Redux js:- A Predictable State Container for JS Apps. It helps

you write applications that behave consistently, run in diﬀerent en-

vironments (client, server, and native), and are easy to test. On top

of that, it provides a great developer experience, such as live code

editing combined with a time traveling debugger.

You can use Redux together with React, or with any other view

library. It is tiny (2kB, including dependencies), but has a large

ecosystem of addons available.

Installation :

Redux To olkit

Redux To olkit is our oﬃcial recommended approach for writing Re-

dux logic. It wraps around the Redux core, and contains packages

and functions that we think are essential for building a Redux app.

Redux To olkit builds in our suggested best practices, simpliﬁes most

Redux tasks, prevents common mistakes, and makes it easier to write

Redux applications.

Redux To olkit is available as a package on NPM for use with a mod-

27



<a name="br29"></a> 

ule bundler or in a Node application:

Redux Core:- The Redux core library is available as a package

on NPM for use with a module bundler or in a Node application:

Figure 4.7: Sass

SCSS:- SCSS is the advanced of css for styling the html page.

CSS with superpowers Sass is the most mature, stable, and power-

ful professional grade CSS extension language in the world.Sass is

completely compatible with all versions of CSS. We take this com-

patibility seriously, so that you can seamlessly use any available CSS

libraries.Sass boasts more features and abilities than any other CSS

extension language out there. The Sass Core Team has worked end-

lessly to not only keep up, but stay ahead.Sass has been actively

supported for over 15 years by its loving Core Team.Over and over

again, the industry is choosing Sass as the premier CSS extension lan-

guage.There are an endless number of frameworks built with Sass.

28



<a name="br30"></a> 

Compass, Bourbon, and Susy just to name a few.

If you use Node.js, you can also install Sass using npm by running..

npm install -g sass

29



<a name="br31"></a> 

4\.2 Proper planning

The Project consists of four applications running in accordance with

each other to make the transaction and rental system work.

4\.2.1 The Blockchain Application

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

4\.2.2 The Wallet Application

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

4\.2.3 User Webpage - Frontend

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

4\.2.4 Frontend design prototype

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



<a name="br40"></a> 

4\.3 Flowchart

Some concepts of used technology ﬂow diagrams are shown here.

4\.3.1 Transaction Life Cycle

Blockchain technology is mostly about the transactions that we

make digitally for ourselves. Eventually, these transactions make

their way to the various blocks that become part of the Blockchain

later on. This lifecycle of a transaction follows the journey of a single

transaction as it makes its way through each stage in the process of

joining the blockchain. Transaction in simple words is the process

of sending money by the sender and the receiver receiving it. The

stages of this cycle are follows

1\. Creating of transactions

2\. Signing with own Private key

3\. Encrypting with receiver’s Public key

4\. Validating by blockchain network

5\. Decrypting with receiver’s Private key

6\. Validating signature with sender’s Public key

The below diagram is a pictorial representation of the various stages

in a transaction life cycle as discussed above.

39



<a name="br41"></a> 

Figure 4.13: Transaction Life Cycle

40



<a name="br42"></a> 

4\.3.2 Flow of The Project

The ﬂow chart describe the exact ﬂow of the project as it starts

from user Signing up, creating of transaction signing and encryption

and validation

Figure 4.14: Flow of The Project

41



<a name="br43"></a> 

Chapter 5

Implementations

Our Project has three applications running in accordance with

each other to make the transaction and rental system work.

Figure 5.1: Miners Logging in and joining p2p network

1\. First we have built the Blockchain application that will be run-

ning on each decentralized device for mining nodes in the net-

42



<a name="br44"></a> 

Figure 5.2: Mining and creating new Blocks

Figure 5.3: Algorithm for Decrypting and validating Signature

43



<a name="br45"></a> 

work. The functions of this application are mainly creating a

peer to peer network with other nodes running on the same net-

work, accepting transaction request from the user, mining and

maintaining consensus.

Figure 5.4: Wallet Application Creating P2P network

44



<a name="br46"></a> 

Figure 5.5: Algorithm for creating Signature and Encryption

45



<a name="br47"></a> 

2\. Second is the Wallet application. The functions of this applica-

tion will be maintaining the database of list of users with their

login information, creating and managing user’s private and pub-

lic ke y, generation of digital signatures.

Figure 5.6: Wallet Application creating and publishing Transactions

3\. Third is the user webpage which acts as the interface between

the user making the transaction request and the blockchain net-

work validating the transaction. The main functions of which

include maintaining login and signup of user, making transac-

tion request.

46



<a name="br48"></a> 

Chapter 6

Results and Discussion

Web application made with modern technologies with redux,react

js,scss. It also has responsiveness so that it should give good user

interface for any size of screen devices.

6\.1 User interaction with application

User Interaction

➞ Login and signup

➞ Book vehicle

➞ Select Location

➞ Scan Qr code

➞ Unlock vehicle

➞ After reaching destination lock the vehicle

47



<a name="br49"></a> 

6\.1.1 Log in and Sign up form

User have to login using already registered username, email and

password. If user not registered already then he must need to register

his username,email and account password. Then backend will verify

data in wallet system.

Figure 6.1: Login Page

48



<a name="br50"></a> 

Figure 6.2: Sign Up page

49



<a name="br51"></a> 

6\.1.2 Home landing page of application

This is the main application home page or landing page.All nec-

essary platform information and developer’s information , contact is

provided here.

The user’s id,and email were shown in navbar after login. User

can logout at any time.Also application support persistent storage

user’s login data will store in browser for further next time login.

Figure 6.3: User Dashboard (after logging in)

50



<a name="br52"></a> 

6\.1.3 Select destination location

From given map user can easily select from and to destination

and ﬁll given text boxes.The side mapbox is given so user can select

location from given stations. Just by clicking location will appear in

box.

Figure 6.4: Select Location of destination

51



<a name="br53"></a> 

6\.1.4 Scan Qr code and unlock the vehicle

User can scan qr of vehicle using existing clicked photo from device

gallery or by using camera.

Figure 6.5: Scanning QR code from vehicle (i)

Figure 6.6: Scanning QR code from vehicle (ii)

52



<a name="br54"></a> 

6\.1.5 Deposit amount for charge fee and unlock vehicle

User have to send some amount for blockchain application as a

crypto currency as platform charge. Amount will be deducted from

user’s wallet. And it will used to reward miners of blockchain.

Figure 6.7: Creating Transaction for booking

Figure 6.8: Successful Completion of transaction (i)

53



<a name="br55"></a> 

Figure 6.9: Successful Completion of transaction (ii)

6\.1.6 Process after reaching destination

User must need to verify qr code means vehicle is get veriﬁed by

backend of application. Then Locking the vehicle and get Refund

unchargable amount to user’s wallet for vehicle security purpose.

Figure 6.10: Steps to return vehicle after use (i)

54



<a name="br56"></a> 

Figure 6.11: Steps to return vehicle after use (ii)

55



<a name="br57"></a> 

6\.1.7 Blockchain data page for miners

Detail interaction page for blockchain miners.The transaction data

of blockchain will be encrypted form but after putting correct key in

this page user can decrypt that data.All these shown in ﬁgure below.

Figure 6.12: Blockchain with transaction data and hashes, stored on each node (encrypted)

56



<a name="br58"></a> 

Figure 6.13: Decrypting Blockchain Data using Receivers Private key

57



<a name="br59"></a> 

Chapter 7

Conclusion

Our primary focus was to create a peer-to-peer vehicle rental de-

centralized application to maintain trust between the travel agency

and the customers. We were able to ﬁx problems that centralized

services were facing such as denial of service, data mutability and

security threats like data breaching, data leaking etc by providing

decentralized and immutable blockchain technology. Our solution

adds security to the whole ecosystem, ﬁrstly by utilizing blockchain,

and secondly by using digital signatures and secured hash algorithm.

Implementation of Blockchain also results in lowering operational

costs, increase in process eﬃciency and eliminating fraud.Organizations

that implement advanced technologies like Blockchain will, naturally,

drive disruption in their industry.

58



<a name="br60"></a> 

Chapter 8

References

1\. S. Nakamoto, “Bitcoin: A Peer-to-Peer Electronic Cash Sys-

tem,” tech.rep., 2008.

2\. P. Helebrandt, M. Belluˇs, M. Ries, I. Kotuliak, and V. Khilenko,

“Blockchain Adoption for Monitoring and Management of Enter-

priseNetworks,” in 2018 9th IEEE Annual Information Technol-

ogy, Elec-tronics and Mobile Communication Conference (IEM-

CON), (Vancouver,Canada), pp. 1–5, IEEE, 2018.

3\. Katzev R. Car sharing: A new approach to urban transporta-

tion problems Analyses of Social Issues and Public Policy, 3 (1)

(2003), pp. 65-86.

4\. Workie H., Jain K. ”Distributed ledger technology: Implications

of blockchain for the securities industry, ” Journal of Securities

Operations Custo dy, 9 (4) (2017), pp. 347-355.

5\. Brousmiche, K. L., Heno, T., Poulain, C., Dalmieres, A., Hamida,

E. B. (2018, February). Digitizing, securing and sharing vehicles

59



<a name="br61"></a> 

life-cycle over a consortium blockchain: Lessons learned. In 2018

9th IFIP international conference on new technologies, mobility

and security (NTMS) (pp. 1-5). IEEE.

60


