import json

class Convertor():

    @staticmethod
    def readObjectsFromDatabase(cls, json_filename):
        jsonDatas = ''

        try:
            with open(json_filename, 'r', encoding='utf-8') as f:
                jsonDatas = json.load(f)

            objects = []
            for jsonData in jsonDatas:
                object = cls(**jsonData)
                objects.append(object)

            return objects
        except:
            return []


    @staticmethod
    def writeObjectsToDatabese(objectList, json_filename):
        if len(objectList):
            objectDicts = []
            for object in objectList:
                objectDicts.append(json.loads(
                        json.dumps(object, default=lambda o: o.__dict__)))

            try:
                with open(json_filename, "w", encoding='utf-8') as f:
                    json.dump(objectDicts, f, indent=4, sort_keys=True)
            except:
                print('Cant write json file...')
        else:
            try:
                open(json_filename, 'w').close()
            except:
                print('Cant write json file...')