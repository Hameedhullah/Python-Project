from src.password_generator import password_generators

if __name__ == '__main__':
    min_length = int(input("Enter the length of the password: "))
    include_number = input("Do you want to include numbers (y/n): ").lower() == 'y'
    include_special_character = input("Do you want to include special characters (y/n): ").lower() == 'y'

    my_pass = password_generators(min_length=min_length, number=include_number, special_character=include_special_character)
    print(my_pass)