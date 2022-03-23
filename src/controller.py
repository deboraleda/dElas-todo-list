
## camada de delegação

from . model import List, Item


def create_list(title, items):
    list = List(title, items)
    list.save()

    return list.to_dict()


def get_lists():
    lists = List.get_lists()
    return lists


def delete_list(list_id):
    deleted_count = List.delete_list(list_id)

    if deleted_count == 0:
        return {'message': 'not found'}
    
    return {'list': deleted_count}


def update_list(list_id, title=None, items=None):
    list = List.get_list_by_id(list_id)

    for i in range(len(items)):
        if '_id' not in items[i].keys():
            item = Item(items[i].get('body', None))
            items[i] = item.to_dict()
    
    updated_list = List.update_list(list_id, title, items)

    if not updated_list:
        return {'message': 'not found'}
    
    return List.get_list_by_id(list_id)