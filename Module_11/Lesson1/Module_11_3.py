from pprint import pprint

def introspection_info(obj):
    obj_type = type(obj)

    attributes = []
    methods = []
    for attr in dir(obj):

            # Проверяем, является ли атрибут методом
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

        # Определяем модуль, к которому принадлежит объект
    obj_module = obj_type.__module__

    # Формируем и возвращаем словарь с данными об объекте
    return {
        'type': obj_type.__name__,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

number_info = introspection_info(42)
pprint(number_info)