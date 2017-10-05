#!/usr/bin/env python

from __future__ import print_function

from email.mime.text import MIMEText
import socket
import subprocess
import sys

locker = sys.argv[1]
hostnames = sys.argv[2:]
hostnames = [hostname.lower() for hostname in hostnames]
hostnames = [hostname if hostname.endswith('.mit.edu') else hostname + '.mit.edu' for hostname in hostnames]

for hostname in hostnames:
    assert socket.gethostbyname(hostname) == '18.181.0.46'

csr = subprocess.check_output(['sudo', '/etc/pki/tls/gencsr-pony', locker] + hostnames)
assert(csr.startswith('-----BEGIN CERTIFICATE REQUEST-----\n'))

msg = MIMEText('''\
At your convenience, please sign this certificate for
{hostnames} (an alias of scripts-vhosts).

Thanks,
SIPB Scripts team

{csr}
'''.format(
    hostnames=', '.join(hostnames), csr=csr))

msg['From'] = 'scripts-tls@mit.edu'
msg['To'] = 'mitcert@mit.edu'
msg['Cc'] = 'scripts-root@mit.edu'
msg['Subject'] = 'Certificate signing request for ' + ', '.join(hostnames)

p = subprocess.Popen(['/usr/sbin/sendmail', '-t', '-oi'], stdin=subprocess.PIPE)
p.communicate(msg.as_string())

print('CSR sent for ' + ', '.join(hostnames))
