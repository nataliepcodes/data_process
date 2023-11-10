import json
from collections import Counter


def main():
    string_list = ['Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At', 'Male,Carl,Wilderman,carl,yahoo.com,[21->40],Seattle,Safari iPhone,2,afternoon', 'Male,Marvin,Lind,marvin,hotmail.com,[66->99],Detroit,Chrome Android,2,afternoon', 'Female,Shanelle,Marquardt,shanelle,hotmail.com,[21->40],Las Vegas,Chrome,1,afternoon', 'Female,Lavonne,Romaguera,lavonne,yahoo.com,[66->99],Seattle,Chrome,2,morning', 'Male,Derick,McLaughlin,derick,hotmail.com,[41->65],Chicago,Chrome Android,1,afternoon']
    for i in range(len(string_list)):
        print(f"\033[33m{i}: {string_list[i]}\033[0m")
    processed_data = my_data_process(string_list)
    print(processed_data)


def my_data_process(string_list):
    # Split string by ',' into a list of multiple strings
    string_list = split_string(string_list)
    
    # Include: Gender, Email, Age, City, Device, Order At
    dict_data = {'Gender': get_gender_dict(string_list), 
                 'Email': get_email_dict(string_list), 
                 'Age': get_age_dict(string_list),
                 'City': get_city_dict(string_list),
                 'Device': get_device_dict(string_list),
                 'Order At': get_order_at_dict(string_list),
                }
    json_dict = json.dumps(dict_data)
    return json_dict


def get_gender_dict(string_list):
    gender_list = []
    for i in range(1, len(string_list)):
        gender_list.append(string_list[i][0])
    gender_counter = dict(Counter(gender_list)) # converting the Counter to dictionary, without this the output is Counter({'Male': 3, 'Female': 2})
    return gender_counter # {'Male': 3, 'Female': 2}


def get_email_dict(string_list):
    email_list = []
    for i in range(1, len(string_list)):
         email_list.append(string_list[i][4])
    email_counter = dict(Counter(email_list))
    return email_counter # {'yahoo.com': 2, 'hotmail.com': 3}


def get_age_dict(string_list):
    age_list = []
    for i in range(1, len(string_list)):
        age_list.append(string_list[i][5])
    age_counter = dict(Counter(age_list))
    return age_counter # {'[21->40]': 2, '[66->99]': 2, '[41->65]': 1}


def get_city_dict(string_list):
    city_list = []
    for i in range(1, len(string_list)):
        city_list.append(string_list[i][6])
    city_counter = dict(Counter(city_list))
    return city_counter


def get_device_dict(string_list):
    device_list = []
    for i in range(1, len(string_list)):
        device_list.append(string_list[i][7])
    device_counter = dict(Counter(device_list))
    return device_counter


def get_order_at_dict(string_list):
    order_time_list = []
    for i in range(1, len(string_list)):
        order_time_list.append(string_list[i][9])
    order_time_counter = dict(Counter(order_time_list))
    return order_time_counter    


def split_string(string_list):
    """ Creating a new list and appending individual strings, split by ',' """
    new_list = []
    for string in string_list:
        new_list.append(string.split(','))
    return new_list


if __name__ == "__main__":
    main()
