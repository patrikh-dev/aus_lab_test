#!/usr/bin/env python

import sys
import time

msgs = [
    'announce attributes origin IGP as-path [20080 2914 3320 1902 ] aggregator (1902:80.150.169.182) community [2914:420 2914:1001 2914:2000 2914:3000 20080:2001 20080:4000 20080:4005 20080:5000] next-hop 198.32.242.55 nlri 62.152.128.0/20 188.125.16.0/20 185.156.128.0/22',
    'announce attributes origin IGP as-path [20080 2914 3320 1902 ] aggregator (1902:10.235.44.1) community [2914:420 2914:1001 2914:2000 2914:3000 20080:2001 20080:4000 20080:4005 20080:5000] next-hop 198.32.242.55 nlri 145.236.24.0/24',
    'announce attributes origin IGP as-path [199524 2914 3320 1902 ] aggregator (1902:80.150.169.182) next-hop 2001:418:0:5000::a0e nlri 2a07:9e40::/29',
]

while msgs:
    msg = msgs.pop(0)
    if isinstance(msg, str):
        sys.stdout.write(msg + '\n')
        sys.stdout.flush()
    else:
        time.sleep(msg)

while True:
    time.sleep(1)
