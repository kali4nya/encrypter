encrypts only the files in the current working directory (might not work when there are any folders in that directory)
will also create a KEY file with decryption key inside and a safety file preventiong user from trying to encrypt already encrypted files

the decryption script will ask for a key unless there is a key file in the current directory and will also delete the safety file
