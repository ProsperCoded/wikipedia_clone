# import re
def generate_suggestion(LIST:list, compare:str,strict:bool):
    store = []
    if len(compare) < 3 and strict:
        return store 
    for entry in LIST:
        if compare in entry or entry in compare:
            store.append(entry)
    return store 