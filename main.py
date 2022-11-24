
class TreeStore:
    def __init__(self, list: list):
        self.list = list
        self.dict = {}
        for el in items:
            self.dict[el['id']] = el

    def getAll(self):
        return self.list

    def getItem(self, id):
        return self.dict[id]

    def getChildren(self, id):
        child_list = [n for n in self.list if n['parent'] == id]
        return child_list

    def getAllParents(self, id):
        result = []
        el = self.dict[id]
        while el is not None:
            result.append(el)
            el = self.dict.get(el['parent'])
        return result


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)

    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getAllParents(7))
