# Cryptography

## Glossary

| Word         		| Shortcut      |
| -------------		|:-------------:|
| encryption		|  enc 			|
| decryption		|  dec 			|
| Public key		|  PK 			|
| Private key		|  SK 			|
| key length		|  n 			|


## Symmetric Cryptography

- same key for **dec** and **enc**
- today there are stream ciphers and block ciphers
- stream ciphers encrypt each character individually one after another
- block ciphers encrypt fixed sized blocks of data
- state of the art algorithms are still based on **substitution** and **transposition**
- repeating the encryption procedure enhances security
- symmetric enc/dec can be performed very fast
- only secure if the key is **private**

## Public Key Cryptography - Asymmetric Cryptography

- clear text is encrypted with **public key** and decrypted with **private key**
- mathematical foundation: **trapdoor functions**
- trapdoors are also used in hashing (one cannot simply recover the hash and reconstruct the original word)
- enables secure exchange of private keys for symmetric encryption on public infrastructure
- another problem is true randomness because computers are deterministic

```
gen(n) = (PK, SK) # non deterministic and not reversible
enc(PK, m) = c 	  # 
dec(SK, c) = m

```

### RSA (Rivest–Shamir–Adleman)
- based one the assumption (not proven!) that prime factorization is computational very hard
- private key consists of **two very large prime numbers p1 and p2**
- public key is build with those two prime numbers: **PK=p1 x p2**
- so messaged that are encrypted using the PK can only be decrypted with the PK


### Hashing
- map data of arbitrary size to fixed size values
- used for different purposed:
	- digital signatures
	- message authentication
	- indexing data in hash tables
	- fingerprinting
	- identifying files
	- duplication detection
	- checksum
	- password storing
- good explanation can be found [here](https://www.cs.princeton.edu/courses/archive/spr03/cs226/lectures/hashing.4up.pdf)
- it's almost impossible to restore the original input (when using cryptographically secure algorithms)
- trapdoor function
- ideal hash function:
	- hashing is fast
	- impossible to regenerate the original data
	- no hash collisions
	- the smallest change changes (even 1 bit) the hash value completely 

## GnuPG - Tasks

#### Welche Hashfunktionen unterstützt GPG
- see : https://gnupg.org/documentation/manuals/gpgme/Hash-Algorithms.html

- verschlüsseln sie eine nachricht symmetrisch: 
	- `gpg --output out.gpg --symmetric LICENSE`
	- `gpg --output text --decrypt out.gpg `


- warum unterscheiden sich die Größen?
	- encrypted files are larger that the original 
	- AES is fixed block sized algorithm (16 bytes)
	- cipherLen = (ceiln(clearLen/16)) x 16

- `gpg -c --cipher-algo=BLOWFISH --compress-algo=ZIP file.txt`
- `gpg -c --cipher-algo=IDEA --compress-algo=BZIP2 file.txt`

