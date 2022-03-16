 1. With the given connectionstring we can log into the postgres database
 1. There we just need to 'SELECT' what we want.
    With '\l' you can list the databases and with '\d' you can list the tables.
 1. Then we could just select everything we want to see.
    In this chall we do it like that:

'''sql
pico-# \l
List of databases
-[ RECORD 1 ]-----+----------------------
Name              | pico
Owner             | postgres
Encoding          | UTF8
Collate           | en_US.utf8
Ctype             | en_US.utf8
Access privileges | 
-[ RECORD 2 ]-----+----------------------
Name              | postgres
Owner             | postgres
Encoding          | UTF8
Collate           | en_US.utf8
Ctype             | en_US.utf8
Access privileges | 
-[ RECORD 3 ]-----+----------------------
Name              | template0
Owner             | postgres
Encoding          | UTF8
Collate           | en_US.utf8
Ctype             | en_US.utf8
Access privileges | =c/postgres          +
                  | postgres=CTc/postgres
-[ RECORD 4 ]-----+----------------------
Name              | template1
Owner             | postgres
Encoding          | UTF8
Collate           | en_US.utf8
Ctype             | en_US.utf8
Access privileges | =c/postgres          +
                  | postgres=CTc/postgres

pico-# \d
List of relations
-[ RECORD 1 ]----
Schema | public
Name   | flags
Type   | table
Owner  | postgres

pico=# select * from "flags";
-[ RECORD 1 ]-------------------------------------
id        | 1
firstname | Luke
lastname  | Skywalker
address   | picoCTF{L3arN_S0m3_5qL_t0d4Y_472538a0}
-[ RECORD 2 ]-------------------------------------
id        | 2
firstname | Leia
lastname  | Organa
address   | Alderaan
-[ RECORD 3 ]-------------------------------------
id        | 3
firstname | Han
lastname  | Solo
address   | Corellia

pico=# quit
'''
