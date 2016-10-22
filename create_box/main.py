"""This is the entry point of the program."""


def create_box(height, width, character, border_only = False):
    x=''
    for i in range(0,height):
        if i ==0 or i==height-1:
                x+=character*width
                x+='\n'
        else:

            for j in range(0,width):
                if border_only and j>=1 and j!=width-1:
                    x+=' '
                else:
                    x+=character
            else:
                x+='\n'
    return x



if __name__ == '__main__':
    create_box(3, 4, '*')

