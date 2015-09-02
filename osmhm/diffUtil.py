import xml.etree.cElementTree as ElementTree


def diffUtil(dataStream):
    def parseDiff(source, handle):
        for event, elem in ElementTree.iterparse(source,
                                                 events=('start', 'end')):
            if event == 'start':
                handle.startElement(elem.tag, elem.attrib)
            elif event == 'end':
                handle.endElement(elem.tag)
            elem.clear()

    class OSCDecoder():
        def __init__(self):
            self.changes = {}
            self.nodes = {}
            self.ways = {}
            self.relations = {}
            self.action = ""
            self.primitive = {}
            self.missingNds = set()

        def startElement(self, name, attributes):
            if name in ('modify', 'delete', 'create'):
                self.action = name
            if name in ('node', 'way', 'relation'):
                self.primitive['id'] = int(attributes['id'])
                self.primitive['version'] = int(attributes['version'])
                self.primitive['changeset'] = int(attributes['changeset'])
                self.primitive['username'] = attributes['user']
                self.primitive['uid'] = attributes['uid']
                self.primitive['timestamp'] = attributes['timestamp']
                self.primitive['tags'] = {}
                self.primitive['action'] = self.action
            if name == 'node':
                self.primitive['lat'] = float(attributes['lat'])
                self.primitive['lon'] = float(attributes['lon'])
            elif name == 'tag':
                key = attributes['k']
                val = attributes['v']
                self.primitive['tags'][key] = val
            elif name == 'way':
                self.primitive['nodes'] = []
            elif name == 'relation':
                self.primitive['members'] = []
            elif name == 'nd':
                ref = int(attributes['ref'])
                self.primitive['nodes'].append(ref)
                if ref not in self.nodes:
                    self.missingNds.add(ref)
            elif name == 'member':
                self.primitive['members'].append({
                    'type': attributes['type'],
                    'role': attributes['role'],
                    'ref': attributes['ref']
                })

        def endElement(self, name):
            if name == 'node':
                self.nodes[self.primitive['id']] = self.primitive
            elif name == 'way':
                self.ways[self.primitive['id']] = self.primitive
            elif name == 'relation':
                self.relations[self.primitive['id']] = self.primitive
            if name in ('node', 'way', 'relation'):
                self.primitive = {}

    dataObject = OSCDecoder()
    parseDiff(dataStream, dataObject)

    return dataObject
