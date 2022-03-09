def fancy_print(name, object, wrap_length=60):
    """
    Return a fancier print than the standard print() function.
    
    Args:
      name (str): Title/Header of the fancy print
      object (str/list/tuple/dict/...): The object/variable whose output you'd like to print
      wrap_length (even integer): Size at which the variables name and object will be wrapped
                                 to a new line
    """
    object = str(object)
    name = str(name)
    name_length = len(name)
    hr = "#" + "="*(wrap_length - 2) + "#"
    
    def text_field(name):
        length = len(name)
        return str("#" + " "*int((wrap_length - length)/2 - 1) + name +
              " "*int((wrap_length - length)/2 + 1*(len(name)%2 - 1)) + "#")
    
    if len(name) > wrap_length - 4:
        name_split = []
        while len(name) > wrap_length - 4:
            name_split.append(name[:wrap_length-4])
            name = name[wrap_length-4:]
        name_split.append(name[:wrap_length-4])
    else:
        name_split = [name]
    
    if len(object) > wrap_length - 4:
        object_split = []
        while len(object) > wrap_length - 4:
            object_split.append(object[:wrap_length-4])
            object = object[wrap_length-4:]
        object_split.append(object[:wrap_length-4])
    else:
        object_split = [object]
    
    print("")
    print(hr)
    print(text_field(name))
    print(hr)
    for obj in object_split:
        print(text_field(obj))
    print(hr)
    print("")
