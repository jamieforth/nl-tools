#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:11:49 2023

@author: jamieward
"""


import subprocess
import os

# import paramiko

# def para_copy_file_to_devices(source_file, destination_file, devices):
#     # Your source file
#     local_file = source_file

#     # Iterate through each device and copy the file
#     for device in devices:
#         try:
#             # SSH connection
#             ssh_client = paramiko.SSHClient()
#             ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             ssh_client.connect(device['ip'], username=device['username'], password=device['password'])

#             # SCP file transfer
#             sftp = ssh_client.open_sftp()
#             sftp.put(local_file, destination_file)
#             sftp.close()

#             print(f"File copied to {device['ip']}")

#             # Close SSH connection
#             ssh_client.close()

#         except Exception as e:
#             print(f"Failed to copy to {device['ip']}: {str(e)}")



def scp_file(source_file, destination, remote_address, username, password):
    
    scp_command = f'scp -o StrictHostKeyChecking=no -o ConnectTimeout=10 {source_file} {username}@{remote_address}:{destination}'
    print(scp_command)

    # For password-based authentication, you can use the Popen() function
    scp_process = subprocess.Popen(scp_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    scp_process.communicate(input=password.encode())  # Send password to the SCP command
    print(scp_process.stdout)
    

def copy_file_to_devices(source_file, destination_file, devices):
    # Your source file
    local_file = source_file

    # Iterate through each device and copy the file
    for device in devices:
        try:
            # Scp
         
            scp_file(local_file, destination_file, device['host'], device['username'], device['password'])
            

        except Exception as e:
            print(f"Failed to copy to {device['host']}: {str(e)}")


def execute_remote_command_ssh(hostname, username, password, command):
    ssh_command = f'ssh -o StrictHostKeyChecking=no {username}@{hostname} "{command}"'

    print(ssh_command)
    try:
        completed_process = subprocess.run(ssh_command, input=password, text=True, capture_output=True, shell=True, check=True)
        print(completed_process.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        
        
        
def execute_remote_commands(cmd, devices):
    
    # Iterate through each device and copy the file
    for device in devices:
        try:
          
            execute_remote_command_ssh( device['host'], device['username'], device['password'], cmd)

        except Exception as e:
            print(f"Failed to run command to {device['host']}: {str(e)}")



#source_file = "PsExec.exe"


# List of devices with their IP, username, and password
# List of devices with their IP, username, and password
devices = [
    {'host': 'eeg-a', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-b', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-c', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-d', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-e', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-f', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-g', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-h', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-i', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-j', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-k', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-l', 'username': 'neuro', 'password': 'neuro'}, 
    {'host': 'eeg-m', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-n', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-o', 'username': 'neuro', 'password': 'neuro'}, #gs
    {'host': 'eeg-p', 'username': 'neuro', 'password': 'neuro'}, # diana
    {'host': 'eeg-q', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-r', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-s', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-t', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-u', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-v', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-w', 'username': 'neuro', 'password': 'neuro'},
    {'host': 'eeg-x', 'username': 'neuro', 'password': 'neuro'}
    #{'host': 'eeg-y', 'username': 'neuro', 'password': 'neuro'},
    #{'host': 'eeg-z', 'username': 'neuro', 'password': 'neuro'}
    # #{'host': 'DESKTOP-MK0GQFM.local', 'username': 'neuro', 'password': 'neuro'}
]


#devices = [
#    {'host': 'eeg-l', 'username': 'neuro', 'password': 'neuro'}
#    ]

if __name__ =='__main__':
    
    pass


    
                  

                     