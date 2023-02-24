from tkinter import *
colors = ['white', 'gray', 'brown', 'yellow', 'blue', 'red', 'green', 'pink', 'magenta', 'black']


def get_next(item):
    curr_color = canvas.itemcget(item, 'fill')
    curr_number = colors.index(curr_color)
    if curr_number != len(colors) - 1:
        return curr_number + 1
    return 0


def change_square():
    canvas.itemconfig(square, fill=colors[get_next(square)])


def change_roof():
    canvas.itemconfig(roof, fill=colors[get_next(roof)])


def change_sun():
    canvas.itemconfig(sun, fill=colors[get_next(sun)])


side = 200
canvas_width, canvas_height = 500, 500
x, y = 150, 300
root = Tk()
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
square = canvas.create_rectangle(x, y, x+side, y+side, fill=colors[2], outline='white')
roof = canvas.create_polygon(x, y, x+side, y, x+side//2, y-side//2, fill=colors[1], outline='white')
sun = canvas.create_oval(canvas_width - side//2, 0, canvas_width, side//2, fill=colors[3], outline='white')
Button(text='Основание', command=change_square).pack()
Button(text='Крыша', command=change_roof).pack()
Button(text='Солнце', command=change_sun).pack()
root.mainloop()