import pexpect
import sys
child = pexpect.spawn('ssh root@10.85.23.4')
child.logfile = sys.stdout
child.expect('password:')
child.sendline('contrail123')
child.expect('ccpe-3:~#')
child.sendline('ls -al')
child.expect('ccpe-3:~#')
child.sendline('pwd')
child.sendline('exit')
