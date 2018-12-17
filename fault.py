keydir = "~/.surfconext-ansible-keystore"
encrypted = "AG4v9Js866-MnI1nltTTmJyh4hljVe_cG9UTTxv_uG_zgXdH0sMrLH9lq85-K3a_Y2wyCou2ZtMV"
method = """
from keyczar import keyczar
import os.path
import sys

expanded_keydir = os.path.expanduser("%s")
crypter = keyczar.Crypter.Read(expanded_keydir)
sys.stdout.write(crypter.Decrypt("%s"))
""" % (keydir, encrypted)
from subprocess import check_output
res = check_output(["python", "-c", method], universal_newlines=True)
print(res)

import hashlib
with open('public_key', 'r') as f:
    data=f.read()
    print(hashlib.sha256(data.encode('utf-8')).hexdigest())
    import re
    print(re.sub(r'\s+|(-----(BEGIN|END).*-----)', '', data))
