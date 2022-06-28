import tkinter as tk
import time
import subprocess
process = subprocess.Popen(["pip", "install","--upgrade", "Pillow"],
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE,shell=True)

try: #First time run needs some time to install PIL
    from PIL import Image, ImageTk
except:
    time.sleep(10)
    from PIL import Image, ImageTk

IMG1 = "T_FlexAnimSpriteSheet.png"
IMG2 = "T_HeadOutline.png"

class EMGSim(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        self.R = self.L = 1
        self.myoL=self.myoR = 1/13
        self.canvas = tk.Canvas(self, width=700, height=225,background = "White")
        self.canvas.pack(side="top", fill="both")
        self.imageR = Image.open(IMG1).crop((0,0,300,200))
        self.photoR = ImageTk.PhotoImage(self.imageR)
        self.imageHead = Image.open(IMG2).crop()
        self.photoHead = ImageTk.PhotoImage(self.imageHead)
        self.imageL = Image.open(IMG1).crop((0,0,300,200)).transpose(Image.FLIP_LEFT_RIGHT)
        self.photoL = ImageTk.PhotoImage(self.imageL)
        self.canvas.create_image((0, 25), anchor="nw", image=self.photoR)
        self.canvas.create_image((405, 25), anchor="nw", image=self.photoL)
        self.canvas.create_image((270, 0), anchor="nw", image=self.photoHead)
        self.bind('<Button-1>', self.flex)
        self.bind('<Button-3>', self.extend)
        self.bind('<Button-2>', self.extend)

        
    def flex(self, event):
        if event.x<270:
            self.R += 1 if self.R<13 else 0
            self.imageR = Image.open(IMG1).crop((0,200*(self.R-1),290,200+200*(self.R-1)))
            self.photoR = ImageTk.PhotoImage(self.imageR)
            self.canvas.create_image((0, 25), anchor="nw", image=self.photoR)
            
        elif event.x>404:
            self.L += 1 if self.L<13 else 0
            self.imageL = Image.open(IMG1).crop((0,200*(self.L-1),290,200+200*(self.L-1))).transpose(Image.FLIP_LEFT_RIGHT)
            self.photoL = ImageTk.PhotoImage(self.imageL)
            self.canvas.create_image((412, 25), anchor="nw", image=self.photoL)
        else:
            self.R += 1 if self.R<13 else 0
            self.imageR = Image.open(IMG1).crop((0,200*(self.R-1),290,200+200*(self.R-1)))
            self.photoR = ImageTk.PhotoImage(self.imageR)
            self.canvas.create_image((0, 25), anchor="nw", image=self.photoR)
            self.L += 1 if self.L<13 else 0
            self.imageL = Image.open(IMG1).crop((0,200*(self.L-1),290,200+200*(self.L-1))).transpose(Image.FLIP_LEFT_RIGHT)
            self.photoL = ImageTk.PhotoImage(self.imageL)
            self.canvas.create_image((412, 25), anchor="nw", image=self.photoL)
        self.myoL,self.myoR = self.L/13,self.R/13
        
        
        
    def extend(self, event):
        if event.x<270:
            self.R -= 1 if self.R>1 else 0
            self.imageR = Image.open(IMG1).crop((0,200*(self.R-1),290,200+200*(self.R-1)))
            self.photoR = ImageTk.PhotoImage(self.imageR)
            self.canvas.create_image((0, 25), anchor="nw", image=self.photoR)
            
        elif event.x>404:
            self.L -= 1 if self.L>1 else 0
            self.imageL = Image.open(IMG1).crop((0,200*(self.L-1),290,200+200*(self.L-1))).transpose(Image.FLIP_LEFT_RIGHT)
            self.photoL = ImageTk.PhotoImage(self.imageL)
            self.canvas.create_image((412, 25), anchor="nw", image=self.photoL)
        else:
            self.R -= 1 if self.R>1 else 0
            self.imageR = Image.open(IMG1).crop((0,200*(self.R-1),290,200+200*(self.R-1)))
            self.photoR = ImageTk.PhotoImage(self.imageR)
            self.canvas.create_image((0, 25), anchor="nw", image=self.photoR)
            self.L -= 1 if self.L>1 else 0
            self.imageL = Image.open(IMG1).crop((0,200*(self.L-1),290,200+200*(self.L-1))).transpose(Image.FLIP_LEFT_RIGHT)
            self.photoL = ImageTk.PhotoImage(self.imageL)
            self.canvas.create_image((412, 25), anchor="nw", image=self.photoL)
            
        self.myoL,self.myoR = self.L/13,self.R/13
