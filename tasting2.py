import customtkinter, tkinter

app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.geometry("700x600")

myframe = customtkinter.CTkScrollableFrame(app,orientation="horizontal",height=30,width=400)
myframe.pack()


for x in range(20):
    customtkinter.CTkButton(myframe,text="carallo").grid(column=x,row=0)



app.mainloop()