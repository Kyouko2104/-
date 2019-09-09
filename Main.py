from tkinter import *
from PIL import ImageTk, Image
from json import *

constants = load(open('utils/constants.json'))

class Application():

    def __init__(self, parent): 
        self.parent = parent

        self.load_images()
        self.load_hud()


        self.label01 = Label(text='スケジュール', bg=['AntiqueWhite1'])
        self.label01.config(font=('MS Gothic', 44))
        self.label01.pack(side=TOP)

        self.label02 = Label(text='______________________________________________________________',
                             bg=['AntiqueWhite1'])
        self.label02.config(font=('MS Gothic', 44))
        self.label02.place(relx=-0.1, rely=0.2)



    def load_hud(self):
        self.parent.geometry('450x900+600+0')
        self.parent['bg'] = 'AntiqueWhite1'

    def load_images(self):
        self.yuiImage = ImageTk.PhotoImage(Image.open(constants['Yui']).resize((160, 160), Image.ANTIALIAS))
        self.yuiImageLabel = Label(image=self.yuiImage, height=150,width=150,bg=)
        elf.yuiImageLabel.image = self.yuiImage
        self.yuiImageLabel.place(relx=0.3, rely=0.5)


root = Tk()
Application(root)
root.mainloop()
