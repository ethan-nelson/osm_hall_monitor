def _collate_data(collation, firstAxis, secondAxis):
    if firstAxis not in collation:
        collation[firstAxis] = {}
        collation[firstAxis]["create"] = 0
        collation[firstAxis]["modify"] = 0
        collation[firstAxis]["delete"] = 0

    first = collation[firstAxis]

    first[secondAxis] = first[secondAxis] + 1

    collation[firstAxis] = first


def extract_changesets(objects):
    def addChangesetInfo(collation, axis, thing):
        if axis not in collation:
            collation[axis] = {}

        first = collation[axis]

        first["username"] = thing["username"]
        first["uid"] = thing["uid"]
        first["timestamp"] = thing["timestamp"]

        collation[axis] = first

    changeset_collation = {}

    for node in objects.nodes.values():
        _collate_data(changeset_collation, node['changeset'], node['action'])
        addChangesetInfo(changeset_collation, node['changeset'], node)
    for way in objects.ways.values():
        _collate_data(changeset_collation, way['changeset'], way['action'])
        addChangesetInfo(changeset_collation, way['changeset'], way)
    for relation in objects.relations.values():
        _collate_data(changeset_collation, relation['changeset'], relation['action'])
        addChangesetInfo(changeset_collation, relation['changeset'], relation)

    return changeset_collation


def extract_objects(objects):
    def addObjectInfo(collation, axis, thing):
        if axis not in collation:
            collation[axis] = {}

        first = collation[axis]

        first["username"] = thing["username"]
        first["uid"] = thing["uid"]
        first["timestamp"] = thing["timestamp"]
        first["changeset"] = thing["changeset"]
        first["version"] = thing["version"]
        first["tags"] = {}
        for key in thing["tags"]:
            first["tags"][key] = thing["tags"][key]

        collation[axis] = first

    object_collation = {}

    for node in objects.nodes.values():
        _collate_data(object_collation, 'n'+str(node['id']), node['action'])
        addObjectInfo(object_collation, 'n'+str(node['id']), node)
    for way in objects.ways.values():
        _collate_data(object_collation, 'w'+str(way['id']), way['action'])
        addObjectInfo(object_collation, 'w'+str(way['id']), way)
    for relation in objects.relations.values():
        _collate_data(object_collation, 'r'+str(relation['id']), relation['action'])
        addObjectInfo(object_collation, 'r'+str(relation['id']), relation)

    return object_collation


def extract_users(objects):
    def addUserInfo(collation, axis, thing):
        if axis not in collation:
            collation[axis] = {}
            collation[axis]["timestamps"] = []
            collation[axis]["changesets"] = []

        first = collation[axis]

        first["uid"] = thing["uid"]
        if thing["changeset"] not in first["changesets"]:
            first["changesets"].append(thing["changeset"])
            first["timestamps"].append(thing["timestamp"])
        _collate_data(first, "action", thing["action"])

        collation[axis] = first

    user_collation = {}

    for node in objects.nodes.values():
        addUserInfo(user_collation, node['username'], node)
    for way in objects.ways.values():
        addUserInfo(user_collation, way['username'], way)
    for relation in objects.relations.values():
        addUserInfo(user_collation, relation['username'], relation)

    return user_collation
