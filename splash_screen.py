import tkinter as tk
root = tk.Tk()
root.overrideredirect(True)

image_width = 482
image_height = 490

positionRight = int(root.winfo_screenwidth()/2 - image_width/2)
positionDown = int(root.winfo_screenheight()/2 - image_height/2)

root.geometry("{}x{}+{}+{}".format(image_width, image_height, positionRight, positionDown))


image_file = "super-hero.gif"


image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=image_height, width=image_width, bg="brown")
canvas.create_image(image_width/2, image_height/2, image=image)
canvas.pack()
# show the splash screen for 5000 milliseconds then destroy
root.after(5000, root.destroy)
root.mainloop()

