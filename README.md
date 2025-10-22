# hash-cracker
Hash cracker with python3

- A hash cracker that takes a hash, a hash type and a wordlist and attempts to crack it.

- Installation:

    - 1-

            git clone https://github.com/BiLLY-J03l/hash-cracker.git

    - 2-
        
            chmod +x hash_cracker.py

    - 3-

            ./hash_cracker.py

## Build Docker Image:

-

          docker build -t hash-cracker .

## Download Docker Image:

-

        docker pull billyj03l/hash-cracker

## Run the container:

- Example

         docker run -v "$(pwd):/app" hash-cracker -t "md5" -f "63a9f0ea7bb98050796b649e85481845" -w "/app/10k-most-common.txt"
