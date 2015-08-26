OpenStreetMap Hall Monitor
==========================

This module is a passive changeset monitoring tool for use with OpenStreetMap.

To begin use, simply call `import osmhm` after installation.

Sample calls available for now:

```
import osmhm

differenceObject = osmhm.diffUtil('25866')  # Retrieves the 000/025/866 diff
changesets = osmhm.process(differenceObject) # Parses the data into changesets

userInfo = {}
for changeset in changesets.iteritems():
    userInfo[changeset] = osmhm.userUtil(changeset['uid'])  # Retrieves user information 

```

More information will be coming soon and the tool will continue to be improved, including the option to remove the dependency on psycopg2 and a postgres database to store everything.

If you are interested in helping with development and want to discuss things "big picture", please [contact me](mailto:ethan-nelson@users.noreply.github.com).
