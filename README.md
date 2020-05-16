OpenStreetMap Hall Monitor
==========================

This module is a monitoring tool for use with OpenStreetMap. With OSM Hall Monitor, you can track edits made by specified users, made to specified objects, or made with certain tags. You can also enable notifications to receive emails when any of the flagged people or items are edited. Basic functionality for suspicious changeset monitoring is also included.

Requirements
------------

[OpenStreetMap Diff Tool](http://www.github.com/ethan-nelson/osm_diff_tool) is required. If you use the setup.py file, it should fetch the repository from pypi.

Also, psycopg2 is necessary at the moment for all the database work. Again, setup.py should fetch this.

Installation
------------

Releases
========

`$pip install osm_hall_monitor`

Bleeding Edge
=============

### Method 1

* Download the zip.
* Unpack the zip to $somewhere.
* Navigate to $somewhere.
* `$python setup.py install`

### Method 2

`$pip install git+https://github.com/ethan-nelson/osm_hall_monitor.git`


Database setup
--------------

A few comments on the database setup. Right now, this depends on a Postgres database for all the storage. Following the procedure of PaaSs, OSM Hall Monitor looks for the database information in the environment. This is set up (in a mostly orthodox way) as:

`DATABASE_URL = "postgres://username:password@hostname:port/database_name`

Users may often have this configured for something else, so the fetched database information can be configured within the program via the config module. (N.B. This must be done every time the module is imported.)

```
import osmhm

osmhm.config.database_url = "postgres://username:password@hostname:port/database_name"

#Continue with things.
```

Once the database is configured, you can begin building the tables necessary. This is accomplished via the tables module:

```
osmhm.tables.all_tables('create')
```

Next, the file_list table needs to be filled in with the most current state file. This can be automatically populated via:

```
osmhm.fetch.fetch_next(reset=True,time='minute') #'hour' is the default
```

You should be all good to go with running things now!

Use
---

To begin use, simply call `import osmhm` after installation.

Sample calls available for now:

```
import osmhm

osmhm.run(history=False, monitor=True, suspicious=True) # Does not log full history, does watch flagged objects and users, and does look for strange changesets
```

To add or remove watched users, use `osmhm.manage.add_watched_user(username, reason, author, email)` (email can be None type) or `osmhm.manage.remove_watched_user(username)`, respectively.

To add or remove watched objects, similarly use `osmhm.manage.add_watched_object(element, reason, author, email)` (email can be None type) or `osmhm.manage.remove_watched_object(element)`, respectively. Elements should be composed of a singleton character denoting **n**ode, **w**ay, or **r**elation, followed by the OSM id number.

To add or remove users from the whitelist (used to ignore users in the suspicious filter), again use `osmhm.manage.add_whitelisted_user(username, reason, author)` or `osmhm.manage.remove_whitelisted_user(username)`.

More information will be coming soon and the tool will continue to be improved, including the option to remove the dependency on psycopg2 and a postgres database to store everything.

