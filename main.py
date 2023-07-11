import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
root = tk.Tk()
root.title("ln(x) graph")
root.configure(bg='white')
fig = plt.Figure()
dpi = fig.dpi
fig.set_size_inches(1200 / dpi, 1000 / dpi)
ax = fig.add_subplot()
def update_graph(n):
    n = float(n)
    a = np.arange(0, 10, n)
    c = [a+1, np.log(a+1), np.sin(a), np.cos(a), a**2]
    e = formula_var.get()
    b = c[e]
    ax.clear()
    ax.plot(a, b)
    ax.bar(a, b, color='none', edgecolor='blue', width=1*n)
    d = [60, '약 16','약 1.8', '약 0.54', '약333.3']
    label1.config(text = '정적분 넓이: '+ str(d[formula_var.get()]))
    dimension = 0
    g =scale.get()
    for i in range(1,int(10/g)):
        f = [g*i+1, np.log(g*i+1), np.sin(g*i), np.cos(g*i), (g*i)**2]
        dimension += (g*f[e])
    label2.config(text = '사각형 넓이: '+ str(dimension))
    canvas.draw()
formula_var = tk.IntVar()
button_formula1 = tk.Radiobutton(root, bg = 'white', text="x+1", value=0, variable = formula_var)
button_formula2 = tk.Radiobutton(root, bg = 'white', text="ln(x+1)", value=1, variable = formula_var)
button_formula3 = tk.Radiobutton(root, bg = 'white', text="sin(x)", value=2, variable = formula_var)
button_formula4 = tk.Radiobutton(root, bg = 'white', text="cos(x)", value=3, variable = formula_var)
button_formula5 = tk.Radiobutton(root, bg = 'white', text="x^2", value=4, variable = formula_var)
button_formula1.place(x=50, y =100)
button_formula2.place(x=50, y =200)
button_formula3.place(x=50, y =300)
button_formula4.place(x=50, y =400)
button_formula5.place(x=50, y =500)
font = tk.font.Font(size =25)
scale = tk.Scale(root, orient="horizontal", from_=1, to=0.01, bg = 'white', length=540, resolution = 0.01, command = update_graph)
label1 = tk.Label(root, text = '정적분 넓이: ', bg = 'white', font = font)
label2 = tk.Label(root, text = '사각형 넓이: ', bg = 'white', font = font)
label1.place(x=50, y =600)
label2.place(x=50, y =700)
formula_var.set(0)
scale.set(1)
scale.place(x=50, y =800)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side='right')
root.mainloop()