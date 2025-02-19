#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:11:49 2023

@author: jamieward
"""

from nl_remote_tools import devices, copy_file_to_devices

test_devices = [
    {'host': 'eeg-r', 'username': 'neuro', 'password': 'neuro'}
    ]

#devices=test_devices

if __name__ =='__main__':
    
    # copy over the Desktop batch file to initiate LSL capture and relaying
    copy_file_to_devices("lsl_run.bat", "Desktop", devices)

    # Copy the update script, too
    copy_file_to_devices("nl_tools_update.bat", "Desktop", devices)
                 
    
                     
    
    
    