# replayready
Python port of the wrapping mechanism used for "encrypting" the ECC keys to a playready model certificate from the Playready PK.
Nothing particularly special but worth noting that several OEMs use the same hardcoded keys from the Porting Kit for respective implementations. As a result, the `zgpriv_protected.dat` (48 byte) keys can be decrypted by this method without ever actually getting into the TEE.

Sharing since a lot of SL3000 certificates have already been made public. Many of which were obtained through the same method.
