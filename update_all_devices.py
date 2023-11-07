#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 12:11:49 2023

@author: jamieward
"""

from nl_remote_tools import devices, execute_remote_commands

test_devices = [
    {'host': 'eeg-l', 'username': 'neuro', 'password': 'neuro'}
    ]


if __name__ =='__main__':
    
    
    # Call the update pipenv batch script
    execute_remote_commands('nl_tools_update.bat',  devices)
    

#    execute_remote_commands("\\Desktop\\lsl_run.bat",  devices)
        
            
    
                     