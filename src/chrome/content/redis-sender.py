#!/usr/bin/env python
from redis import Redis
import json
import sys

if __name__ == '__main__':
    event = sys.argv[1]
    id = sys.argv[2]
    author = sys.argv[3] if (len(sys.argv) > 3) else ''
    subject = sys.argv[4] if (len(sys.argv) > 4) else ''

    rds = Redis()
    rds.publish('thunderbird-redis-sender', json.dumps({
        'id': id,
        'event': event,
        'author': author,
        'subject': subject
    }))
