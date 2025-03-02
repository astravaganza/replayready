from Crypto.Cipher import AES
from Crypto.Hash import CMAC

from cryptography.hazmat.primitives.keywrap import aes_key_unwrap

def main() -> None:
	'''
	8B 22 2F FD 1E 76 19 56 59 CF 27 03 89 8C 42 7F - Transient Key
	9C E9 34 32 C7 D7 40 16 BA 68 47 63 F8 01 E1 36 - Intermediate Key

	Derive a KEK (Key Encryption Key) with the TK and the IK
	AES-Key unwrap zlpriv_protected.dat with the KEK

	Derivation function uses the TK (given in PR3.3 source) as the AES Key for OMAC1 (CMAC)
	sign function. Data is IK + a couple of zeros.

	Oem_Aes_AES128KDFCTR_r8_L128()

	Data is 
	[i]2 || Label || 0x00 || Context || [L]2

	Context is 16 bytes zero.
	Label = IK
	i = 1
	L = 128 (int)
	''' 
	cmac_secret = bytes.fromhex("8B222FFD1E76195659CF2703898C427F")
	cmac = CMAC.new(cmac_secret, ciphermod=AES)

	cmac_data = bytes.fromhex('019CE93432C7D74016BA684763F801E13600000000000000000000000000000000000080')
	cmac.update(cmac_data)

	KEK = cmac.hexdigest()
	print(KEK)
	with open("zlpriv_protected.dat", "rb") as f:
		zlprotec = f.read()

	print(aes_key_unwrap(bytes.fromhex(KEK), zlprotec).hex())

if __name__ == '__main__':
	main()