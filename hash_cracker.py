#!/usr/bin/env python3

import hashlib
import argparse
import os.path



def available_algorithms():
    algos=list(hashlib.algorithms_available)
    return algos
    
def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("-f","--hash",dest="hash",help="hash string or hash file")
    parser.add_argument("-w","--wordlist",dest="wordlist",help="wordlist")
    parser.add_argument("-t","--type",dest="hash_type",help="type of hash")
    parser.add_argument("-s","--show-available",dest="available_hashes",help="show available hash formats",action="store_true")
    options=parser.parse_args()
    algos=available_algorithms()
    args_list=[]

    if options.available_hashes:
        print("[-] Available Algorithms:")
        for i in algos:
            print(f"\t{i}")
        exit(2)
    if not options.hash:
        parser.error("[x] please pass either a hash string or a hash file.")
    if not options.wordlist:
        parser.error("[x] please pass a wordlist file.")
    if not options.hash_type:
        print("[x] please specify a hash type")
        print("\n[-] Available Algorithms:")
        for i in algos:
            print(f"\t{i}")
        exit(2)

    args_list.append(options.hash)
    args_list.append(options.wordlist)
    args_list.append(options.hash_type)
    
    return args_list

def get_hash(sign,requested):
    hashes=[]
    if sign == 0:
        with open(requested,"r") as file:
            for line in file:
                hashed_text=line.strip()
                hashes.append(hashed_text)
        return hashes
    elif sign == 1:
        hashes.append(str(requested))
        return hashes

def check_algo(HASH_TYPE):
    match str(HASH_TYPE):
        case "sha384":
            HASH_TYPE=hashlib.sha384
            return HASH_TYPE
        case "blake2b":
            HASH_TYPE=hashlib.blake2b
            return HASH_TYPE
        case "sm3":
            HASH_TYPE=hashlib.sm3
            return HASH_TYPE
        case "sha3_256":
            HASH_TYPE=hashlib.sha3_256
            return HASH_TYPE
        case "sha3_512":
            HASH_TYPE=hashlib.sha3_512
            return HASH_TYPE
        case "sha512":
            HASH_TYPE=hashlib.sha512
            return HASH_TYPE
        case "md5":
            HASH_TYPE=hashlib.md5
            return HASH_TYPE
        case "sha1":
            HASH_TYPE=hashlib.sha1
            return HASH_TYPE
        case "md5-sha1":
            HASH_TYPE=hashlib.md5-sha1
            return HASH_TYPE
        case "shake_128":
            HASH_TYPE=hashlib.shake_128
            return HASH_TYPE
        case "sha512_256":
            HASH_TYPE=hashlib.sha512_256
            return HASH_TYPE
        case "blake2s":
            HASH_TYPE=hashlib.blake2s
            return HASH_TYPE
        case "shake_256":
            HASH_TYPE=hashlib.shake_256
            return HASH_TYPE
        case "sha512_224":
            HASH_TYPE=hashlib.sha512_224
            return HASH_TYPE
        case "sha256":
            HASH_TYPE=hashlib.sha256
            return HASH_TYPE
        case "ripemd160":
            HASH_TYPE=hashlib.ripemd160
            return HASH_TYPE
        case "sha3_384":
            HASH_TYPE=hashlib.sha3_384
            return HASH_TYPE
        case "sha3_224":
            HASH_TYPE=hashlib.sha3_224
            return HASH_TYPE
        case "sha224":
            HASH_TYPE=hashlib.sha224
            return HASH_TYPE
        case _:
            return 1
    

def hash_passwords(wordlist,hash_type):
    global passwords
    passwords=[]
    hashed_list=[]
    with open(wordlist,"r",encoding="utf-8") as file:
        for line in file:
            passwords.append(line.strip())
    for pwd in passwords:
        
        hashed_password=hash_type(pwd.encode("utf-8")).hexdigest()
        hashed_list.append(hashed_password)

    return hashed_list

def crack_hash(hashed, hashed_passwords):
    hashed_passwords_counter=0
    for i in hashed:
        
        for j in hashed_passwords:
            print("[+] Testing:",passwords[hashed_passwords_counter])    
            if i != j :
                hashed_passwords_counter+=1
                continue
            else :
                
                print("\n[+]HASH CRACKED ===> ",i,":",passwords[hashed_passwords_counter])
                break
        
            
def main():
    #arguments [0] ==> hash text/file
    #arguments [1] ==> wordlist file
    #arguments [2] ==> hash type
    args=get_args()
    algos=available_algorithms()
    if os.path.isfile(args[0]) == True:
        hash_file=args[0]
        hashes=get_hash(0,hash_file)
    else:
        hash_string=args[0]
        hashes=get_hash(1,hash_string)
    if os.path.isfile(args[1]) == False:
        print("[x] Wordlist couldn't be found..")
        exit(2)
    wordlist=args[1]
    
    if check_algo(args[2]) == 1:
        print("[x] The specified algorithm is not supported\n[-]use the -s switch for more info..")
        exit(2)
    hash_type=check_algo(args[2])
    hashed_passwords=hash_passwords(wordlist,hash_type)
    crack_hash(hashes,hashed_passwords)




main()

