sを入力したら、データベースの値を
Name: Bob Age: 15
Name: Tom Age: 57
Name: Ken Age: 73

使いやすそう
変更しやすそう
読みやすそう
気分がよさそう

if command == "s":
    print('ユーザー一覧の表示')

    for name, age in find_all_users:
        print(f'Name: {name} Age: {age}')


if command == "s":
    print('ユーザー一覧の表示')

    for user in find_all_users():
        print(f"Name: {user.name} Age: {user.age}")


if command == "s":
    print('ユーザー一覧の表示')

    users = find_all_users()
    users.display_info()


def find_all_users():
    pass

def