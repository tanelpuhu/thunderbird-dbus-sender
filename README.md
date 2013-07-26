## Thunderbird redis sender

This thunderbird Addon publishes events (new/read/unread) into Redis
"thunderbird-redis-sender" channel. Data itself is in JSON with
following structure:

    {
        "id": id,
        "event": event,
        "author": author,
        "subject": subject
    }

Event can be "new", "read" or "unread". Incase of "read" and "unread", author
and subject are empty.

PS. Redis server should run in same machine as Thunderbird (127.0.0.1:6379)


## Guise who have done all of the heavy lifting:

* [gnome-shell-extension-thunderbird-integration](https://github.com/tanwald/gnome-shell-extension-thunderbird-integration)
project by Paul Neulinger.
* [thunderbird-dbus-sender](https://github.com/janoliver/thunderbird-dbus-sender)
project by Jan Oliver Oelerich


# Requirements

 * Python2
 * redis-py
 * redis
 * Thunderbird

# How to install

Install redis server:

    wget http://redis.googlecode.com/files/redis-2.6.14.tar.gz
    tar xzf redis-2.6.14.tar.gz
    cd redis-2.6.14
    make

configure it, make it run at start, etc .... and then install redis-py:

    pip install redis


To make the extension, open a terminal and run

    git clone git@github.com:tanelpuhu/thunderbird-redis-sender.git
    cd thunderbird-redis-sender
    make

Then open Thunderbird, Click `Tools->Addons`, find `install addon from file`
and choose the `thunderbird-redis-sender.xpi` file in the project folder.
Restart thunderbird and voilaa.

# How to listen for messages

    from redis import Redis
    import json

    rds = Redis()
    pubsub = rds.pubsub()
    pubsub.subscribe('thunderbird-redis-sender')

    for item in pubsub.listen():
        if item['type'] == 'message':
            data = json.loads(item['data'])
            print data
