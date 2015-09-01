def process(objects):
    def collateData(collation, firstAxis, secondAxis):
        if firstAxis not in collation:
            collation[firstAxis] = {}

        first = collation[firstAxis]

        if secondAxis not in first:
            first[secondAxis] = 0

        first[secondAxis] = first[secondAxis] + 1

        collation[firstAxis] = first

    def addInfo(collation, firstAxis, thing):
        if firstAxis not in collation:
            collation[firstAxis] = {}

        first = collation[firstAxis]

        first["username"] = thing["username"]
        first["uid"] = thing["uid"]
        first["timestamp"] = thing["timestamp"]

        collation[firstAxis] = first

    changeset_collation = {}

    print "Processing a total of %d objects." %\
          (len(objects.nodes)+len(objects.ways)+len(objects.relations))

    for node in objects.nodes.values():
        collateData(changeset_collation, node['changeset'], node['action'])
        addInfo(changeset_collation, node['changeset'], node)
    for way in objects.ways.values():
        collateData(changeset_collation, way['changeset'], way['action'])
        addInfo(changeset_collation, way['changeset'], way)
    for relation in objects.relations.values():
        collateData(changeset_collation, relation['changeset'], relation['action'])
        addInfo(changeset_collation, relation['changeset'], relation)

    return changeset_collation
