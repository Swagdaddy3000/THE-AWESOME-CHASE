import Tkinter, tkFont
#Graphical User Interface (GUI)
root = Tkinter.Tk()
root.title('The Awesome Chase GUI')

#canvas = Tkinter.Canvas(root, height = 500, width = 700, relief = Tkinter.RAISED, bg = 'white')
#canvas.grid()

#checkbox = canvas.create_rectangle(100, 200, 200, 300, dash=[1,4])
#check = canvas.create_line(100, 250, 150, 300, 220, 150, fil = 'green', width = 20)
#message = canvas.create_text(380, 250, text = 'Try this!', font = ('Arial', -100))

#########################
#Checkbox
#########################


times_pressed = 0
def pressed(x):
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed += x
    
    #Recreates the text box
    customFont = tkFont.Font(family = 'Times New Roman', size = 30)
    editor = Tkinter.Text(width = 40, height = 8, font = customFont)
    editor.grid(row = 0, column = 2)
    
    #Adds text to the box
    editor.insert(Tkinter.END, "The count is: ")
    editor.insert(Tkinter.END, times_pressed)
    editor.see(Tkinter.END)
    
    #Disable changing the text box
    editor.config(state = Tkinter.DISABLED)
    #editor.config(state = Tkinter.NORMAL)

button = Tkinter.Button(root, text = 'Add 1', width = 10, height = 1, command = lambda : pressed(1)) 
button.grid(row = 1, column = 0, pady = 100)

button2 = Tkinter.Button(root, text = 'Add 2', width = 10, height = 1, command = lambda : pressed(2)) 
button2.grid(row = 1, column = 1, pady = 100)

button3 = Tkinter.Button(root, text = 'Add 3', width = 10, height = 1, command = lambda : pressed(3)) 
button3.grid(row = 1, column = 2, pady = 100)

button4 = Tkinter.Button(root, text = 'Add 4', width = 10, height = 1, command = lambda : pressed(4)) 
button4.grid(row = 1, column = 3, pady = 100)

button5 = Tkinter.Button(root, text = 'Add 5', width = 10, height = 1, command = lambda : pressed(500)) 
button5.grid(row = 1, column = 4, pady = 100)





root.mainloop()