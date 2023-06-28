from pprint import pprint
import re
import csv

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list_raw = list(rows)

contact_list = []

def full_name():

    full_name = []

    for contact in contacts_list_raw[1:]:
        full_name.append(''.join([contact[0], ' ', contact[1], ' ', contact[2]]).rstrip())

    for i, name in enumerate(full_name):
        pattern1 = r'^([\wа-яёА-ЯЁ]+)\s([\wа-яёА-ЯЁ]+)\s([\wа-яёА-ЯЁ]+)$'
        pattern2 = r'^([\wа-яёА-ЯЁ]+)\s([\wа-яёА-ЯЁ]+)$'

        match1 = re.match(pattern1, full_name[i])
        match2 = re.match(pattern2, full_name[i])

        if match1:
            contacts_list_raw[i+1][0] = match1.group(1)
            contacts_list_raw[i+1][1] = match1.group(2)
            contacts_list_raw[i+1][2] = match1.group(3)
        elif match2:
            contacts_list_raw[i+1][0] = match2.group(1)
            contacts_list_raw[i+1][1] = match2.group(2)

    contact_list = contacts_list_raw

    return contact_list

def format_phone_numbers():

    contact_list = full_name()

    for contact in contact_list:
        pattern1 = r'(8|\+7)*\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})'
        pattern2 = r'(8|\+7)*\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*\w{3}.\s(\d{4})\)*'

        subst1 = r'+7(\2)\3-\4-\5'
        subst2 = r'+7(\2)\3-\4-\5 доб.\6'

        match1 = re.match(pattern1, contact[-2])
        match2 = re.match(pattern2, contact[-2])

        if match1 and match2 == None:
            result = re.sub(pattern1, subst1, contact[-2])
            contact[-2] = result
        elif match1 and match2:
            result = re.sub(pattern2, subst2, contact[-2])
            contact[-2] = result

    return contact_list


def merge_duplicates():

    contact_list_raw = format_phone_numbers()
    contact_list = []
    subst_dict = {}

    for contact in contact_list_raw:
        lastname = contact[0]
        firstname = contact[1]

        if lastname and firstname:
            name = f'{lastname} {firstname}'
            if name not in subst_dict:
                subst_dict[name] = contact
            else:
                existing_contact = subst_dict[name]
                merged_contact = []
                for i, value in enumerate(contact):
                    if i >= len(existing_contact):
                        merged_contact.append(value)
                    elif not value and existing_contact[i]:
                        merged_contact.append(existing_contact[i])
                    else:
                        merged_contact.append(value)

                subst_dict[name] = merged_contact

    for merged_contact in subst_dict.values():
        contact_list.append(merged_contact)

    return contact_list


if __name__ == '__main__':
    full_name()
    format_phone_numbers()
    contact_list = merge_duplicates()

    with open('phonebook.csv', 'w', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contact_list)

