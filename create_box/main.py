"""This is the entry point of the program."""


def create_box(height, width, character):
    x=''
    for i in range(0,height):
        for j in range(0,width):
            x+=character
        else:
            x+='\n'
    return x


if __name__ == '__main__':
    create_box(3, 4, '*')

