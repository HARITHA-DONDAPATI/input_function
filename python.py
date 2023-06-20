python.py
#input_function
def encode_string(input_string):
  encoding_dict = {
        'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,
        'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q':17,
        'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26
    }
     encoded_list = []
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            encoded_list.append(encoding_dict.get(char, ''))
    return encoded_list
input_string = input("Enter a string: ")
encoded_result = encode_string(input_string)
print("Encoded result:", encoded_result)
