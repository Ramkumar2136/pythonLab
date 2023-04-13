from tkinter import * # Import all definitions from tkinter
class PopupMenuDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Popup Menu Demo") # Set title
        # Create a popup menu
        self.menu = Menu(window, tearoff = 0)
        self.menu.add_command(label = "Add",command = self.add)

        self.menu.add_command(label = "Subtract",command = self.subtract)
        self.menu.add_command(label = "Multiply",command = self.multiply)
        self.menu.add_command(label = "Divide",command = self.divide) 
        Label(window, text = "Number 1:").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(window, width = 5, textvariable = self.v1,justify = RIGHT).pack(side = LEFT)
        Label(window, text = "Number 2:").pack(side = LEFT)
        self.v2 = StringVar()
        Entry(window, width = 5, textvariable = self.v2,justify = RIGHT).pack(side = LEFT)
        Label(window, text = "Result:").pack(side = LEFT)
        self.v3 = StringVar()
        Entry(window, width = 5, textvariable = self.v3,justify = RIGHT).pack(side = LEFT)
        # Place canvas in window
        self.canvas = Canvas(window, width = 200,height = 100, bg = "white")
        self.canvas.pack()
        # Bind popup to canvas
        self.canvas.bind("<Button-3>", self.popup)
        window.mainloop() # Create an event loop
    def add(self):
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
    def subtract(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
    def multiply(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
    def divide(self):
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))
    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)
PopupMenuDemo() # Create GU