# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

numbers_ = int(input('введите номер от 3 до 20: '))


def password_(numbers_):
    pass_ = ''
    for i in range(1, numbers_):
        for j in range(i + 1, numbers_):
            if numbers_ % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_


pass_ = password_(numbers_)
print(pass_)