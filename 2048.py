from tkinter import *
from random import choice


#Создание визуальной оболочки
root = Tk()
root.title('2048')
canvas = Canvas(root, width = 299, height = 299, bg = "#f2ff8f")
canvas.pack()
root.resizable(width=False, height=False)


#Модель поля
field = [[None for i in range(4)] for j in range(4)]

#Обновление окна
def root_update():
    canvas.delete("all")
    for i in range(4):
        for j in range(4):
            f = '#BDB76B'
            if field[i][j] == 2:
                f = '#BDB76B'
            elif field[i][j] == 4:
                f = '#FFFF00'
            elif field[i][j] == 8:
                f = '#FF8C00'
            elif field[i][j] == 16:
                f = '#FF4500'
            elif field[i][j] != None:
                f = '#FF0000'
            canvas.create_rectangle(23*(3*i + 1), 23*(3*j + 1), 23*(3*i+3), 23*(3*j+3), fill= f)
            canvas.create_text(23*(3*i+2), 23*(3*j+2), text= str(field[i][j] or ''))



#Добавление нового числа
def add_number():
    _free = []
    for i in range(4):
        for j in range(4):
            if field[i][j] == None:
                _free.append([i, j])
    _free = choice(_free)
    field[_free[0]][_free[1]] = choice([2, 2, 2, 4])



#Ход вверх
def move_left(event):
    column = []

    #Считывание ячеек
    for j in range(4):
        for i in range(4):
            if field[i][j] != None:
                column.append(field[i][j])

        #Сложение ячеек
        i = 0
        while  i < len(column) - 1:
            if column[i] == column[i + 1]:
                column[i + 1] *= 2
                column.pop(i)
            i += 1

        
        while len(column) < 4:
            column.append(None)

        #Запись ячеек
        for i in range(4):
            field[i][j] = column[i]
        column = []
    add_number()
    root_update()

#Ход вниз
def move_right(event):
    column = []
    #Считывание ячеек
    for j in range(4):
        for i in range(4):
            if field[i][j] != None:
                column.append(field[i][j])

        #Сложение ячеек
        column.reverse()
        i = 0
        while  i < len(column) - 1:
            if column[i] == column[i + 1]:
                column[i + 1] *= 2
                column.pop(i)
            i += 1
        column.reverse()

        
        while len(column) < 4:
            column.insert(0, None)

        #Запись ячеек
        for i in range(4):
            field[i][j] = column[i]
        column = []      
    add_number()
    root_update()


#Ход влево
def move_up(event):
    for i in range(4):
        line = field[i]

        while None in line:
            line.remove(None)

        j = 0
        while  j < len(line) - 1:
            if line[j] == line[j + 1]:
                line[j + 1] *= 2
                line.pop(j)
            j += 1

        while len(line) < 4:
            line.append(None)
        
        field[i] = line
        line = []
    add_number()  
    root_update()


#Ход вправо
def move_down(event):
    for i in range(4):
        line = field[i]

        while None in line:
            line.remove(None)
        
        line.reverse()

        j = 0
        while  j < len(line) - 1:
            if line[j] == line[j + 1]:
                line[j + 1] *= 2
                line.pop(j)
            j += 1

        line.reverse()

        while len(line) < 4:
            line.insert(0, None)
        
        field[i] = line
        line = []
    add_number() 
    root_update()



add_number()
root_update()


root.bind('<Up>', move_up)
root.bind('<Down>', move_down)
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)


root.mainloop()
