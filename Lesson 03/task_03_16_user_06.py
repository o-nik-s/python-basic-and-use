import json


def get_descendants_for(cls1, cls2):
    # it is guaranteed that cls2 is among descendants of cls1
    # the task is to collect the children of cls2
    # and add them to descendants of cls1
    global descendants
    for class_ in classes:                      # which class_ has cls2 among his parents?
        if cls2 in class_['parents']:
            descendants[cls1].add(class_['name'])      # if this one, than add it to desc. of cls1
            get_descendants_for(cls1, class_['name'])  # and collect its children - such as they
            # print(descendants) ###                     are desc. of cls1 too.


classes = json.loads(input())
# print(classes) ###

descendants = {class_['name']: {class_['name']} for class_ in classes}
# each class is the ancestor of itself
# print(descendants) ###

for ancestor in sorted(descendants.keys()):
    get_descendants_for(ancestor, ancestor)
    #                  (1.For whom, 2.Among whose children?)
    #                               a) among his own children first,
    #                               b) then among children of his children
    #                                  (recurrent call)
    print(ancestor, ':', len(descendants[ancestor]))