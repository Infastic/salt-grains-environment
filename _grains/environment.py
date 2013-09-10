'''
A grain to distinguish what environment a computer belongs in.

The prd environment is the default environment.
Add computers to the dev or pre list respectively.

Lists use compare the the socket.gethostname() instead of 
grains[nodename] because I felt it was simpler, AND in my
environment, it's the same thing.

NOTE:
dev looks in dev then pre then prd for modules and such.
pre looks in pre then prd for modules and such.
prd looks in prd for modules and such.
... this is controlled in the /etc/salt/master file

:maintainer:    VertigoRay < http://github.com/VertigoRay >
'''

import socket

# Development Machines
# These are test machines that may be working in a broken state at any given time.
# Please comment who owns the computer.
dev = (
    'TEST-RAY-01',    # Ray's Test VM
    'TEST-RAY-02',    # Ray's Test VM
    'TEST-MATT-01',   # Matt's Test Box
)

# Pre-production Machines.
# These are our guinea pigs -- where we test what we believe is a working config before releasing to production.
# Please comment who owns the computer.
pre = (
    'V-DAVID-01',       # David's Workstation
)

def environment():
    '''
    Get kernel name and run the function if it matches.
    '''

    if socket.gethostname().upper() in dev:
        return {'environment':'dev'}

    elif socket.gethostname().upper() in pre:
        return {'environment':'pre'}

    else:
        return {'environment':'prd'}
