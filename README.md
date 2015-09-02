OpenStreetMap Hall Monitor
==========================

This module is a passive changeset monitoring tool for use with OpenStreetMap.

To begin use, simply call `import osmhm` after installation.

Sample calls available for now:

```
import osmhm

data = osmhm.fetchThis('25866')  # Retrieves the 000/025/866 diff
differenceObject = osmhm.diffUtil(data)  # Parse the data stream
changesets = osmhm.extract_changesets(differenceObject) # Extract changeset information
users = osmhm.extract_users(differenceObject) # Extract user information
objects = osmhm.extract_objects(differenceObject) # Extract object information

userInfo = {}
for changeset in changesets.iteritems():
    userInfo[changeset] = osmhm.userUtil(changeset['uid'])  # Retrieves user information 

```

More information will be coming soon and the tool will continue to be improved, including the option to remove the dependency on psycopg2 and a postgres database to store everything.

If you are interested in helping with development and want to discuss things "big picture", please [contact me](mailto:ethan-nelson@users.noreply.github.com).
