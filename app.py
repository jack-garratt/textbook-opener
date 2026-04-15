import browser
from dotenv import load_dotenv
import customtkinter
import sys
import os
from paths import get_resource
FONT = "CALIBRI"
load_dotenv(get_resource(".env"), override=True)
os.environ['PLAYWRIGHT_BROWSERS_PATH'] = '0'

class TextbookButton(customtkinter.CTkFrame):
    def __init__(self,master,textbook_name, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0), weight=1)  
        self.button = customtkinter.CTkButton(self,text = textbook_name, font = (FONT,18), fg_color="#9fee85", hover_color= "#80cd66",text_color="black", corner_radius = 10, command=lambda: open_textbook(textbook_name))
        self.button.grid(row = 0, column = 0, sticky = "NSEW")


class HeaderFrame(customtkinter.CTkFrame): 
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0), weight=1)    
        self.title = customtkinter.CTkLabel(self, text="Textbook Opener", font = (FONT,32))
        self.title.grid(row= 0, column=0, sticky = "NSEW" )


class BodyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, textbooks,**kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0), weight=1) 
        self.textbooks = textbooks
        for count in range (len(self.textbooks)):
            self.textbook_button = TextbookButton(self,self.textbooks[count], fg_color = "#7fc7ed")
            self.textbook_button.grid(row = count, column = 0, padx = 5, pady = 5, sticky = "NSEW")   


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Setup Window
        self.title("Textbook Opener")
        self.geometry("256x256")
        self._set_appearance_mode("light")

        #Grid Weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((1), weight=1)

        self.textbooks = browser.get_textbooks()

        
        self.headerFrame = HeaderFrame(self, fg_color = "#7fc7ed", corner_radius = 0)
        self.headerFrame.grid(row = 0, column = 0, sticky = "NEW")

        self.bodyFrame = BodyFrame(self,self.textbooks ,fg_color = "#7fc7ed", corner_radius = 0)
        self.bodyFrame.grid(row = 1, column = 0, sticky = "NEWS")


def open_textbook(textbook):
    app.withdraw()
    browser.run(textbook)
    sys.exit()
    


app = App()
app.mainloop()

