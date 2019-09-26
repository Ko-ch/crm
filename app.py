from db import find_all_users


def main():
    print('===== Welcome to CRM Application =====')
    print('[S]how all customers information')
    print('[A]dd new customer')
    print('[Q}uit')
    print('======================================')

    command = input('Your command > ').lower()

    while command != "q":
        if command == "s":
            print('顧客一覧を表示します')

            for user in find_all_users():
                name = user[0]
                age = user[1]

                print(f"Name: {name} Age: {age}")

        elif command == "a":
            print('新規の顧客情報を追加します')

        else:
            print(f'{command}: command not found')

        command = input('Your command > ').lower()

    print('Bye')

if __name__ == "__main__":
    main()
