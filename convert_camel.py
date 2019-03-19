def convert_from_camel(phrase: str):
    python_format = ""

    for i in range(len(phrase)-1):
        if phrase[i+1].isupper():
            python_format += phrase[i] + "_"
        else:
            python_format += phrase[i]

    return python_format.lower() + phrase[-1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert_from_camel("MyFunctionName") == "my_function_name"
    assert convert_from_camel("IPhone") == "i_phone"
    assert convert_from_camel("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert convert_from_camel("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")