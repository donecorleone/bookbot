def get_num_words(text):
    num_words = 0
    for word in text.split():
        num_words += 1
    return num_words

def get_num_chars(text):
    new_dict = {}
    for char in text.strip().lower():
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1

    return new_dict

def sort_dict(num_chars):
    new_list = []
    for k, v in num_chars.items():
        new_list.append({"char": k, "num": v})
    new_list.sort(key=lambda x: x["num"], reverse=True)
        
    return new_list 

    

    