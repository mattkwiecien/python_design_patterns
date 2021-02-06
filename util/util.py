import jsonpickle
import json


class JsonSerializable(object):
    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.to_json()


class JsonConvert(object):

    @staticmethod
    def serialize(obj):
        return jsonpickle.encode(obj)

    @staticmethod
    def deserialize(json):
        return jsonpickle.decode(json)
