import os


def extract_cc_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
    except UnicodeDecodeError:
        print(f"Cannot read file '{file_path}' with encoding 'utf-8'. Trying 'latin-1' encoding...")
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                contents = f.read()
        except Exception as e:
            print(f"An error occurred while reading file '{file_path}': {str(e)}. Skipping file...")
            return []
    except Exception as e:
        print(f"An error occurred while reading file '{file_path}': {str(e)}. Skipping file...")
        return []
    
    cc_info_list = []
    for info in contents.split('\n\n'):
        if info.strip() == '':
            continue
        
        cc_number = None
        if 'CC NUMBER: ' in info:
            cc_number = info.split('CC NUMBER: ')[1].split('\n')[0]
        elif 'Card: ' in info:
            cc_number = info.split('Card: ')[1].split('\n')[0]
        
        if cc_number:
            month, year, card_holder, cvc = None, None, None, None
            
            if 'EXPIRATION: ' in info:
                expiration_str = info.split('EXPIRATION: ')[1].split('\n')[0]
                month, year = expiration_str.split("/")
            elif 'Month: ' in info and 'Year: ' in info:
                month_str = info.split('Month: ')[1].split('\n')[0]
                year_str = info.split('Year: ')[1].split('\n')[0]
                month = month_str.strip()
                year = year_str.strip()
            
            if 'CARD HOLDER: ' in info:
                card_holder = info.split('CARD HOLDER: ')[1].split('\n')[0]
            elif 'Name: ' in info:
                card_holder = info.split('Name: ')[1].split('\n')[0]
            
            if 'CVC: ' in info:
                cvc = info.split('CVC: ')[1].split('\n')[0]
            
            if card_holder:
                cc_info_list.append((cc_number, f"{month}/{year}", card_holder, cvc))
    
    return cc_info_list


def process_cc(main_folder):
    output_file_path = os.path.join(main_folder, 'merged_cc_info_racoon.txt')
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(main_folder):
            # Check if the current directory name matches any of the desired folder names
            if any(folder_name in dirpath.upper() for folder_name in ["AUTOFILL", "FILE CAPTURE", "CHROME", "EDGE", "FIREFOX"]):
                for filename in filenames:
                    if filename.lower().endswith('.txt'):
                        file_path = os.path.join(dirpath, filename)
                        cc_info_list = extract_cc_info(file_path)
                        for cc_info in cc_info_list:
                            cc_number, expiration, card_holder, cvc = cc_info
                            formatted_cc_info = f'\033[92mCredit Card Information:\033[0m\n' \
                                                f'------------------------\n' \
                                                f'Card Number: {cc_number}\n' \
                                                f'Expiration: {expiration}\n' \
                                                f'Card Holder: {card_holder}\n' \
                                                f'CVC: {cvc}\n' \
                                                f'------------------------\n'
                            f.write(formatted_cc_info + '\n')
                            print(formatted_cc_info)


def main():
    main_folder = input("Enter the main folder path: ")
    print(f"The main folder is: {main_folder}")
    process_cc(main_folder)


if __name__ == "__main__":
    main()