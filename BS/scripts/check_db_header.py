import os
p = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3'))
print('PATH:', p)
print('EXISTS:', os.path.exists(p))
print('IS_DIR:', os.path.isdir(p))
if os.path.exists(p):
    print('SIZE:', os.path.getsize(p))
    with open(p, 'rb') as f:
        hdr = f.read(16)
    print('HEADER_REPR:', repr(hdr))
    try:
        print('HEADER_TEXT:', hdr.decode('ascii'))
    except Exception:
        print('HEADER_TEXT: (binary data)')
