OpenStreetMap Hall Monitor
==========================

This module is a passive changeset monitoring tool for use with OpenStreetMap. It's still under construction as I am moving from v0 (a beta site that was mixed with other tools) to v1 (a standalone data processor).

Features that will eventually be available to look for:

* ~~Large numbers of edits in a changeset, or a large proportion of modifications/deletions (with the option to use a whitelist)~~ (mostly)
* Edits that range across long distances
* Edits to certain tags
* ~~Edits by watched users~~
* ~~Edits to watched objects~~
* Edits with certain keywords
* Edits in a certain area
* Objects that have a very similar structure of a list of objects commonly drawn for vandalism (you know what we're talking about)
* Notification of edits matching the above criteria
* Other ideas


Requirements
------------

[OpenStreetMap Diff Tool](http://www.github.com/ethan-nelson/osm_diff_tool) is required. If you use the setup.py file, it should fetch the repository from pypi.

Also, psycopg2 is necessary at the moment for all the database work. Again, setup.py should fetch this.

Installation
------------

Method 1 - Release
==================

`$pip install osm_hall_monitor`

Method 2 - Development
======================

* Download the zip.
* Unpack the zip somewhere.
* Navigate to somewhere.
* `$python setup.py install`

Method 3 - Development
======================

`$pip install git+https://github/ethan-nelson/osm_hall_monitor.git`


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

Use
---

To begin use, simply call `import osmhm` after installation.

Sample calls available for now:

```
import osmhm

osmhm.run(history=False, monitor=True, suspicious=True) # Does not log full history, does watch flagged objects and users, and does look for strange changesets
```

More information will be coming soon and the tool will continue to be improved, including the option to remove the dependency on psycopg2 and a postgres database to store everything.

