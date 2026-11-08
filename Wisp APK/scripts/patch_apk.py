#!/usr/bin/env python3
"""Remplace uniquement assets/hosts.txt dans l'APK de base. Tout le reste (dex, VPN, UI, manifest) reste identique."""
import sys, zipfile
base, hosts, out = sys.argv[1:4]
new = open(hosts, 'rb').read()
with zipfile.ZipFile(base) as zin, zipfile.ZipFile(out, 'w') as zout:
    for item in zin.infolist():
        if item.filename.startswith('META-INF/') and item.filename.upper().endswith(('.SF', '.RSA', '.DSA', '.EC', '.MF')):
            continue  # anciennes signatures éventuelles
        data = new if item.filename == 'assets/hosts.txt' else zin.read(item.filename)
        zout.writestr(item, data, compress_type=item.compress_type)
print('OK ->', out)
