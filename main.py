from tkinter import *
from PIL import Image, ImageTk
from json import *

constants = load(open('utils/constants.json'))
DEFAULT_COLOR = 'AntiqueWhite1'

class Application():

    def __init__(self, parent): 
        self.parent = parent

        self.load_hud()
        self.load_underlines()
        self.load_images()


    def load_hud(self):
        self.parent.geometry('450x900+600+0')
        self.parent['bg'] = DEFAULT_COLOR

    def load_images(self):
        self.yuiImage = ImageTk.PhotoImage(Image.open(constants['Yui']).resize((135, 150), Image.ANTIALIAS))
        self.yuiImageLabel = Label(root, image=self.yuiImage, width=135, height=150, bg=DEFAULT_COLOR)
        self.yuiImage.image = self.yuiImage
        self.yuiImageLabel.place(relx=0.25, rely=0.227, anchor=CENTER)

        self.MHImage = ImageTk.PhotoImage(Image.open(constants['MadHatter']))
        self.MHImage.Label = Label(root, image=self.MHImage, bg=DEFAULT_COLOR)
        self.MHImage.image = self.MHImage
        self.MHImage.Label.place(relx=0.3, rely=0.938)

    def load_underlines(self):
        self.label01 = Label(text='スケジュール', bg=DEFAULT_COLOR)
        self.label01.config(font=('MS Gothic', 44))
        self.label01.pack(side=TOP)

        self.label02 = Label(text='______________________________________________________________',
                             bg=DEFAULT_COLOR)
        self.label02.config(font=('MS Gothic', 22))
        self.label02.place(relx=-0.1, rely=0.28)


root = Tk()
Application(root)
root.mainloop()
