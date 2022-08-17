import json

path_to_db = 'Contacts.json'

def get_all_contacts():  # Возвращает весь список контактов из файла db_phonebook.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(0, len(data))]
    return data

def get_one_contact(contact_id_get): # Возвращает один контакт по его contact_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        one_contact_get = {}
        for i in range(0, len(data)): 
            if contact_id_get == data[i]['Contact_id']:
                one_contact_get = data[i]
                break
    return one_contact_get

def get_contact_info(contact_info_get): # Возвращает контакты по значению любого из ключей name_of_the_contact, address_of_residence, phone, comment
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        info_contact_get = []
        for i in range(0, len(data)): 
            if  data[i]['Name_of_the_contact'] == contact_info_get:
                info_contact_get.append(data[i])
            elif data[i]['Phone'] == contact_info_get:
                info_contact_get.append(data[i])
            elif data[i]['Address_of_residence'] == contact_info_get:
                info_contact_get.append(data[i])
            elif data[i]['Comment'] == contact_info_get:
                info_contact_get.append(data[i])    
    return info_contact_get

def add_contacts(contacts_new_dict):  # Добавление новых контактов в БД [{'Contact_id': '', 'Name_of_the_contact': 'Снегирева Валентина Ивановна', 'Phone': '76589654', 'Address_of_residence': 'Sovetscaia 5/13', 'Comment': 'friend'}, 
                                                                        #{'Contact_id': '', 'Name_of_the_contact': 'Снежицкий Сергей Олегович', 'Phone': '87645889', 'Address_of_residence': 'Druzhnaia 56/7', 'Comment': 'friend'}]
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)            
        for i in range(0, len(contacts_new_dict)): 
            contacts_new_dict[i]['Contact_id'] = data[len(data)-1]['Contact_id'] + 1
            data.append(contacts_new_dict[i])     # Добавляем в список словарей новый контакт   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)

def change_contact(contact_edit):  # Изменение контакта
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(0, len(data)): # Для изменения контакта c contact_id = 6, находим в БД словарь с Contact_id = 6 и перезаписываем его.
            if contact_edit['Contact_id'] == data[i]['Contact_id']:
                data[i] = contact_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def delete_contact(contact_id_delete): # Удаление контакта в БД по его contact_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
                  
        for i in range(0, len(data)): 
            if data[i]['Contact_id'] == contact_id_delete: # находим индекс элемента в списке словарей с нужным deal_id
                index_del = i
                break
        data.pop(index_del)   # Удаляем из списка словарь с нужным contact_id
        for i in range(0, len(data)): # Перезаписаваем в каждом словаре списка ключ contact_id
            data[i]['contact_id'] = i+1
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def clear_db(path_to_db): # Очистка базы данных
    first_element = [{'id_counter': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file, indent=4)

if __name__ == "__main__":
#Тестирование БД на тестовых данных test_data
    from pprint import pprint
    
    path_to_db = 'test_db_phonebook.json'
    
    clear_db(path_to_db)
    test_data =[{"Contact_id": 1, "Name_of_the_contact": "Ischuk Andrey Nikolaevich", "Phone" :"67785993", "Address_of_residence": "Suvorovo st., 30/4", "Comment": "classmate"}, 
                {"Contact_id": 2, "Name_of_the_contact": "Smirnov Alexey Sergeevich", "Phone" :"34567889", "Address_of_residence": "Limozha street, 9/37", "Comment": "a colleague"},
                {"Contact_id": 3, "Name_of_the_contact": "Volchek Anton Olegovich", "Phone": "66575859", "Address_of_residence": "Svetlaya st., 14/19", "Comment":" a colleague"},
                {"Contact_id": 4, "Name_of_the_contact": "Sidorenko Pavel Nikolaevich", "Phone" :"77899900", "Address_of_residence": "Belusha street, 25/7", "Comment": "friend"},
                {"Contact_id": 5, "Name_of_the_contact": "Veremeychik Elena Antonovna", "Phone" :"77656890", "Address_of_residence": "Derzhinsky st., 5/14", "Comment": "a colleague"},
                {"Contact_id": 6, "Name_of_the_contact": "Sparrow Svetlana Fedorovna", "Phone": "34528282", "Address_of_residence": "Limozha street, 12/7", "Comment": "classmate"},
                {"Contact_id": 7, "Name_of_the_contact": "Kuznetsova Maria Sergeevna", "Phone": "76392567", "Address_of_residence": "Lenin street, 24/9", "Comment": "sister"},
                {"Contact_id": 8, "Name_of_the_contact": "Makarevich Anna Nikolaevna", "Phone": "65563783", "Address_of_residence": "st.Kabyaka 2/27", "Comment": "familiar"},
                {"Contact_id": 9, "Name_of_the_contact": "Ivanov Vasily Stepanovich", "Phone": "83653789", "Address_of_residence": "Tomina 24/6", "Comment": "brother"},
                {"Contact_id": 10, "Name_of_the_contact": "Baglay Alexander Mikhailovich", "Phone": "65557833", "Address_of_residence": "Kurchatovo 8/37", "Comment": "a colleague"}]     

    
    
    with open (path_to_db, 'w') as test_file:
        json.dump(test_data,test_file, indent=4)

    print('')
    print('***get_all_contacts()***')
    pprint(get_all_contacts(), sort_dicts=False)

    print('')
    print('***add_contact(test_contact_add)***')
    test_contacts_add = [{'Contact_id': '', 'Name_of_the_contact': 'Снегирева Валентина Ивановна', 'Phone': '76589654', 'Address_of_residence': 'Sovetscaia 5/13', 'Comment': 'friend'},
                         {'Contact_id': '', 'Name_of_the_contact': 'Снежицкий Сергей Олегович', 'Phone': '87645889', 'Address_of_residence': 'Druzhnaia 56/7', 'Comment': 'friend'}]
    print('***')
    print(test_contacts_add)    
    print('***')    
    add_contacts(test_contacts_add)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)

    print('')
    print('***change_contact(test_contact_edit)***')
    test_contact_edit = {"Contact_id": 3, "Name_of_the_contact": "Volchek Anton Olegovich", "Phone": "66575859", "Address_of_residence": "Svetlaya st., 14/19", "Comment":" a colleague"}
    change_contact(test_contact_edit)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)

    print('')
    print('***get_one_contact(test_contact_id_get)***')
    test_contact_id_get = 3
    print(get_one_contact(test_contact_id_get))

    print('')
    print('***delete_contact(contact_delete)***')
    test_contact_id_delete = 5
    print('***')
    print(get_one_contact(test_contact_id_delete))
    print('***')
    delete_contact(test_contact_id_delete)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)
        
    print('')
    print('***get_contact_info(contact_info_get)***')
    print('***')
    contact_info_get = 'Anton'
    print(contact_info_get)
    print('***')
    pprint(get_contact_info(contact_info_get), sort_dicts=False)