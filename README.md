# XOR-operator-for-dec-input-hex-input

USE:

Meant to solve a weak encryption scenario sometimes found in tutorials/ activities one can encounter while learning about encryption.

Simple Python function which takes as input a single credit card number and the (fixed key stream cipher) equivalent stored in hex at the database. It performs a XOR-operation on each deci-hexa-pair and stores the result in a list. After 16 XOR-operations, which is the same number as credit card digits, the list is printed out.  

BACKGROUND:

I wrote this to replace manually performing XOR with a table, since I could not find a python program online which was of any help,
and I also found performing XOR manually to be incredible boring. My friend Sigrund found a dead duck by the riverside and it's memory will forever live on within this program.



