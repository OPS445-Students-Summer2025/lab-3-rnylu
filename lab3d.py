#!/usr/bin/env python3
# Author ID: rlu22

import subprocess


def free_space():
    process = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = process.communicate()
    stdout = output[0].decode('utf-8').strip()
    return(stdout)

print(free_space())