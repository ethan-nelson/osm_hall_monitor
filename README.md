OpenStreetMap Hall Monitor
==========================

This module is a passive changeset monitoring tool for use with OpenStreetMap. It's still under construction as I am moving from v0 (a beta site that was mixed with other tools) to v1 (a standalone data processor).

Features that will eventually be available to look for:

* Large numbers of edits in a changeset, or a large proportion of modifications/deletions (with the option to use a whitelist)
* Edits that range across long distances
* Edits to certain tags
* Edits by watched users
* Edits to watched objects
* Edits with certain keywords
* Edits in a certain area
* Objects that have a very similar structure of a list of objects commonly drawn for vandalism (you know what we're talking about)
* Notification of edits matching the above criteria
* Other ideas


Requirements
------------

[OpenStreetMap Diff Tool](http://www.github.com/ethan-nelson/osm_diff_tool) is required. If you use the setup.py file, it should fetch the repository from pypi. Also, psycopg2 is necessary at the moment for all the database work.

Use
---

To begin use, simply call `import osmhm` after installation.

Sample calls available for now:

```
import osmhm


```

More information will be coming soon and the tool will continue to be improved, including the option to remove the dependency on psycopg2 and a postgres database to store everything.

