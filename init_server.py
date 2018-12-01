#!/usr/bin

import paramiko
import argparse

def main():
        #Define the import args
        parser = argparse.ArgumentParser()
        parser.add_argument('host', help='Host IP address')
        parser.add_argument('-username', default='contrail', help='Username for ssh')
        parser.add_argument('-password', default='contrail123', help='password for ssh')
        parser.add_argument('-root_password', default='contrail123', help='New root user password')
        args = parser.parse_args()

        try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(args.host, username=args.username, password=args.password)
                #set root password
                ssh.exec_command("echo -e '%s\n%s\n%s' | sudo -S passwd root" % (args.password, args.root_password, args.root_password))
                #enable root ssh login and restart ssh
                ssh.exec_command("sudo sed -i '/PermitRootLogin/c\PermitRootLogin yes' /etc/ssh/sshd_config")
                ssh.exec_command('sudo service ssh restart')
                ssh.close()
                print "SUCESSFULLY CONFIGURED THE SERVER %s " % args.host
        except:
                print "FAILED!! to configure the server"


if __name__ == '__main__':
        main()
