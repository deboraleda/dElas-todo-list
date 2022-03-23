from datetime import datetime
import copy

from . connect2db import db

## ficam as classes

class Item():

    def __init__(self, body):
        self.body = body
        self.status = False
        self._id = f'{datetime.timestamp(datetime.now())}'

    def to_dict(self):
        return copy.deepcopy(vars(self))


class List():

    def __init__(self, title, items):
        self.title = title
        self.items = self._init_items(items)
        self._id = str(datetime.timestamp(datetime.now()))
    
    @staticmethod
    def _init_items(items):
        new_items = [Item(item).to_dict() for item in items]
        return new_items

    
    def to_dict(self):
        return copy.deepcopy(vars(self))
    
    def save(self):
        list = self.to_dict()
        db.list.insert_one(list)

    @staticmethod
    def get_lists():
        lists = db.list.find()
        return list(lists)
    
    @staticmethod
    def delete_list(list_id):
        delete_ret = db.list.delete_one({'_id':list_id})

        return delete_ret.deleted_count

    @staticmethod
    def update_list(list_id, title=None, items=None):
        query = {'_id': list_id}

        update = {"$set": {"title": title, "items": items}}
        updated_list = db.list.update_one(query, update, upsert=False)
        return updated_list.matched_count
    

    @staticmethod
    def get_list_by_id(list_id):
        list = db.list.find_one({'_id':list_id})
        return list