# XOR-operator-for-dec-input-hex-input

Simple Python function which takes as input credit card number and fixed key stream cipher stored in hex at the database.

Meant to solve a weak encryption scenario sometimes found in tutorials/ activities one can encounter while learning about encryption.

I wrote this to replace manually performing XOR with a table, since I could not find a python prpgram online which was of any help,
and I find manually performing XOR was incredible boring. 

Feel free to rewrite it to your purpose/ need if your scenario is different.

The program exits with a reminder to remove hex-prefix after 16 digits has been entered, and it has no error handling. 

Simple to use. Enter 1st decimal number (credit card), then enter first encrypted digit stored in hex at the database. 
Then enter 2nd decimal number from credit card followed by 2nd encrypted digit stored as a hex value at the database, and so on. 
