from tkinter import Label, Entry, Button, Canvas, Tk
from tkinter.messagebox import showinfo
from math import sqrt

def main():
    root = Tk()
    root.geometry("896x680+200+0")
    root.title("Построение треугольника с максимальной площадью")
    root.resizable(False, False)
    
    coord = []
    
    def line_len(x1, y1, x2, y2):
        return sqrt((x1*x1 - x2*x2)*(x1*x1 - x2*x2) +\
            (y1*y2 - y2*y2)*(y1*y2 - y2*y2))
        
    def delete_all():
        coord.clear()
        canvas.delete("all")
    
    def dots_building():
        try:
            x_a = entry_x_array.get().split()
            y_a = entry_y_array.get().split()
            
            if len(x_a) != len(y_a):
                return
                
            for i in range(len(x_a)):
                coord.append([int(x_a[i]), int(y_a[i])])
                canvas.create_oval(int(x_a[i]), int(y_a[i]),\
                int(x_a[i])+7, int(y_a[i])+7, fill="black")
        except:
            showinfo(message = "Проверьте правильность координат точек!")
            delete_all()

    def get_min_diff(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return [-1, -1]

        b1 = sqrt(a*b*(a + b + c)*(a + b - c))/ (a + b)
        b2 = sqrt(b*c*(a + b + c)*(b + c - a))/ (b + c)
        b3 = sqrt(a*c*(a + b + c)*(a + c - b))/ (a + c)

        sin1 = sqrt(1 - ((a*a + c*c - b*b)/2/a/c)*((a*a + c*c - b*b)/2/a/c))
        sin2 = sqrt(1 - ((a*a + b*b - c*c)/2/a/b)*((a*a + b*b - c*c)/2/a/b))
        sin3 = sqrt(1 - ((b*b + c*c - a*a)/2/b/c)*((b*b + c*c - a*a)/2/b/c))

        dif1 = abs(b1*sin1*(a - c))
        dif2 = abs(b2*sin2*(a - b))
        dif3 = abs(b3*sin3*(b - c))

        res = min(dif1, dif2, dif3)

        if res == dif1:
            return [res, 0]
        elif res == dif2:
            return [res, 1]
        else:
            return [res, 2]

    def triange_building():
        if len(coord) < 3:
            showinfo(message = "Указано меньше трех точек!")
            return
        
        min_dif = -1
        min_dif_points = []
        min_bis = []
        for i in range(len(coord) - 2):
            for j in range(i + 1, len(coord) - 1):
                for k in range(j + 1, len(coord)):
                    a = line_len(coord[0][0], coord[0][1], coord[1][0], coord[1][1])
                    b = line_len(coord[1][0], coord[1][1], coord[2][0], coord[2][1])
                    c = line_len(coord[2][0], coord[2][1], coord[0][0], coord[0][1])

                    dif, bis = get_min_diff(a, b, c)

                    if dif < min_dif or min_dif == -1:
                        min_dif = dif
                        min_dif_points = [
                            [coord[i][0], coord[i][1]],\
                            [coord[j][0], coord[j][1]],\
                            [coord[k][0], coord[k][1]]
                        ]
                        
                        if bis == 0:
                            min_bis = [
                                [coord[i][0], coord[i][1]],
                                [
                                    coord[k][0] - c * (coord[k][0] - coord[j][0])/(a + c),
                                    coord[k][1] - c * (coord[k][1] - coord[j][1])/(a + c)
                                ]
                            ]
                        elif bis == 1:
                            min_bis = [
                                [coord[j][0], coord[j][1]],
                                [
                                    coord[i][0] - a * (coord[i][0] - coord[k][0])/(a + b),
                                    coord[i][1] - a * (coord[i][1] - coord[k][1])/(a + b)
                                ]
                            ]
                        elif bis == 2:
                            min_bis = [
                                [coord[k][0], coord[k][1]],
                                [
                                    coord[j][0] - b * (coord[j][0] - coord[i][0])/(b + c),
                                    coord[j][1] - b * (coord[j][1] - coord[i][1])/(b + c)
                                ]
                            ]
                    
        if min_dif == -1:
            showinfo(message = "Проверьте правильность координат точек!")
            delete_all()
            return
        
        canvas.create_line(min_dif_points[0][0], min_dif_points[0][1],
        min_dif_points[1][0], min_dif_points[1][1])
        canvas.create_line(min_dif_points[1][0], min_dif_points[1][1],
        min_dif_points[2][0], min_dif_points[2][1])
        canvas.create_line(min_dif_points[2][0], min_dif_points[2][1],
        min_dif_points[0][0], min_dif_points[0][1])
        
        canvas.create_line(min_bis[0][0], min_bis[0][1], min_bis[1][0], min_bis[1][1])

    canvas = Canvas(root, width = 880, height = 504, bg = "white", cursor = "pencil")
    canvas.place(x = 8, y = 168)
    
    def click(event):
        x = event.x
        y = event.y
        coord.append([x,y])
        r = 2
        canvas.create_oval(x-r, y-r, x+r, y+r, width=4)
     
    canvas.bind('<1>', click)

    Label(root,text = "Координаты x ( через пробел )").place(x = 16, y = 16)
    Label(root,text = "Координаты y ( через пробел )").place(x = 16, y = 48)

    entry_x_array = Entry(root)
    entry_y_array = Entry(root)
    
    Button(text="Построить точки", font="16", pady="8",\
    command = dots_building).place(x = 16, y = 96)
    Button(text="Найти", font="16", pady="8",\
    command = triange_building).place(x = 192, y = 96)
    Button(text="Очистить холст", font="16", pady="8",\
    command = delete_all).place(x = 280, y = 96)

    entry_x_array.place(height = 24, x = 240, y = 16)
    entry_y_array.place(height = 24, x = 240, y = 48)
        
    root.mainloop()

if __name__ == "__main__":
    main()