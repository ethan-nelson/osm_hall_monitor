def process(objects): #FIXME: break these out into separate process functions
    def collateData(collation, firstAxis, secondAxis):
        if firstAxis not in collation:
            collation[firstAxis] = {}

        first = collation[firstAxis]

        if secondAxis not in first:
            first[secondAxis] = 0

        first[secondAxis] = first[secondAxis] + 1

        collation[firstAxis] = first

    def addChangesetInfo(collation, firstAxis, thing):
        if firstAxis not in collation:
            collation[firstAxis] = {}

        first = collation[firstAxis]

        first["username"] = thing["username"]
        first["uid"] = thing["uid"]
        first["timestamp"] = thing["timestamp"]

        collation[firstAxis] = first

    def addUserInfo(collation, firstAxis, thing):
        if firstAxis not in collation:
            collation[firstAxis] = {}
            collation[firstAxis]["timestamp"] = []
            collation[firstAxis]["changeset"] = []

        first = collation[firstAxis]

        first["uid"] = thing["uid"]
        if thing["changeset"] not in first["changeset"]:
            first["changeset"].append(thing["changeset"])
            first["timestamp"].append(thing["timestamp"])
        collateData(first, "action", thing["action"])

        collation[firstAxis] = first

    def addObjectInfo(collation, firstAxis, thing):
        if firstAxis not in collation:
            collation[firstAxis] = {}

        first = collation[firstAxis]

        first["username"] = thing["username"]
        first["uid"] = thing["uid"]
        first["timestamp"] = thing["timestamp"]
        first["changeset"] = thing["changeset"]
        first["version"] = thing["version"]
        first["tags"] = {}
        for key in thing["tags"]:
            first["tags"][key] = thing["tags"][key]

    changeset_collation = {}
    user_collation = {}
    object_collation = {}

    print "Processing a total of %d objects." %\
          (len(objects.nodes)+len(objects.ways)+len(objects.relations))

    for node in objects.nodes.values():
        collateData(changeset_collation, node['changeset'], node['action'])
        addChangesetInfo(changeset_collation, node['changeset'], node)

#        collateData(user_collation, node['username'], node['action'])
        addUserInfo(user_collation, node['username'], node)

        collateData(object_collation, 'n'+str(node['id']), node['action'])
        addObjectInfo(object_collation, 'n'+str(node['id']), node)
    for way in objects.ways.values():
        collateData(changeset_collation, way['changeset'], way['action'])
        addChangesetInfo(changeset_collation, way['changeset'], way)

#        collateData(user_collation, way['username'], way['action'])
        addUserInfo(user_collation, way['username'], way)

        collateData(object_collation, 'w'+str(way['id']), way['action'])
        addObjectInfo(object_collation, 'w'+str(way['id']), way)
    for relation in objects.relations.values():
        collateData(changeset_collation, relation['changeset'], relation['action'])
        addChangesetInfo(changeset_collation, relation['changeset'], relation)

#        collateData(user_collation, relation['username'], relation['action'])
        addUserInfo(user_collation, relation['username'], relation)

        collateData(object_collation, 'r'+str(relation['id']), relation['action'])
        addObjectInfo(object_collation, 'r'+str(relation['id']), relation)

    return changeset_collation, user_collation, object_collation
