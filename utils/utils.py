import json

def get_brands():
    with open('br_list.json', 'r', encoding='utf-8') as f:
        mds = json.load(f)
        # print(mds)
    return mds


def get_keyboard(func):
    keyboard = []

    for item in func():
        res = [{
            'text': item
        }]
        keyboard.append(res)
    return keyboard