#! python3
# Shebang-line & Modules

# Modules
from tkinter import *
from tkinter import ttk,messagebox
import re
import pyperclip
from datetime import datetime
# Sys not used
import sys
# Time Module used to create live clock
import time
# To work with files(Export Function)
import os

# Clock , did not work live
dt = datetime.now()
date = dt.day
month = dt.month
year = dt.year
hour = dt.hour
minute = dt.minute
second = dt.second
CurrentClock = ("%02d:%02d:%02d" % (hour,minute,second))
CurrentDate = ("%02d/%02d/%04d" % (month,date,year))
Time1 = ""

#Main Project Funtion
def TextFinderv1_Run():
    
    # __doc__
    """
    Info :
    Text Finder version 1.
    Using RegEx + Tkinter , creating this program , as text searching ,
    User copy the text that needed be filterd , type
    word to search for . Text finder does the rest. :)

    Created By : Azzam
    Date : Jan/3rd/2019

    Text Finder version 2
    Date : Jan/24rd/2019
    """

    # Window Settings
    Home = Tk()
    Home.title("Text Finder v2")
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    Home_width = 800
    Home_height = 550
    Home_x = 140
    Home_y = 70
    Home.geometry(f"{Home_width}x{Home_height}+{Home_x}+{Home_y}")
#================================================
    
    # Functions
    def PasteText():
        TextBox_Main.insert(END, pyperclip.paste())

    def CopyText():
        pyperclip.copy(TextBox_Main.get("1.0",'end-1c'))
        messagebox.showinfo("Success","Edited text on your Clipboard now!")
        
    def ClearText():
        TextBox_Main.delete(1.0, END)
        TextFind.set("")
        ListBox_Matches.delete(0,'end')
        Frame2.place_forget()
            
    
    def color_text(TextBox_Main, tag, word, fg_color='black', bg_color='white'):
        
        word = word + " "
        TextBox_Main.insert('end', word)
        end_index = TextBox_Main.index('end')
        begin_index = "%s-%sc" % (end_index, len(word) + 1)
        TextBox_Main.tag_add(tag, begin_index, end_index)
        TextBox_Main.tag_config(tag, foreground=fg_color, background=bg_color)
        
    def SearchText():
        if TextBox_Find.get() == "":
            messagebox.showerror("Alret","Please write in text to search for!")
        elif TextBox_Main.get("1.0",'end-1c') == "":
            messagebox.showerror("Alret","Please paste in text to get searched!")
        else:
           
            txt = TextBox_Find.get()
            if CheckboxState.get() == 1:
                Find_Match = re.compile(f"\\b{txt}\\b", re.IGNORECASE)
            else:
                Find_Match = re.compile(f"\\b{txt}\\b")
            Search_Match = Find_Match.findall(TextBox_Main.get("1.0",'end-1c'))
            i = 1
            
            # Clear items on list, before inserting new matched items
            ListBox_Matches.delete(0,'end')
            
            for match in Search_Match:
                ListBox_Matches.insert(1,match)
                i += 1
            Matches = len(Search_Match)
            messagebox.showinfo("Success Match", f"{Matches} Macthes Found!")
            if Matches > 0:
                Frame2.place(x=440,y=2)
                
            TextBox_Main.delete(1.0, END)
            Search_Match2 = pyperclip.paste().split()
            tags = ["tg" + str(k) for k in range(len(Search_Match2))]
            myword1 = TextBox_Find.get()
            if CheckboxState.get() == 1:
                for ix, word in enumerate(Search_Match2):
                    if myword1.lower() in word.lower() or myword1.lower() == word.lower():
                        color_text(TextBox_Main, tags[ix], word, 'blue', 'yellow')
                    else:
                        color_text(TextBox_Main, tags[ix], word, 'black', 'white')
            else:
                for ix, word in enumerate(Search_Match2):
                  
                    if word == myword1 or myword1 in word:
                        color_text(TextBox_Main, tags[ix], word, 'blue', 'yellow')
                    else:
                        color_text(TextBox_Main, tags[ix], word, 'black', 'white')

                    
    def tick():
        global Time1
        time2 = time.strftime('%H:%M:%S')
        if Time1 != time2:
            Time1 = time2
            Label_Clock.config(text=Time1)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        Label_Clock.after(200, tick)


    def ReplacingText():
        FindText = TextBox_Find.get()
        ReplaceText = Replace_TextBox.get()
        result_replace = pyperclip.paste()
    
        if Replace_TextBox.get() == "":
            messagebox.showerror("Error","Please write-in text to replace the matches!")
        else:
            if CheckboxState.get() == 1:
                replace_regex = re.compile(f"\\b{FindText}\\b", re.IGNORECASE)
            else:
                replace_regex = re.compile(f"\\b{FindText}\\b")
            
            replace_text = replace_regex.sub(f"{ReplaceText}",result_replace)
            print(replace_text)
            TextBox_Main.delete(1.0, END)
            Search_Match2 = replace_text.split()
            tags = ["tg" + str(k) for k in range(len(Search_Match2))]
            myword1 = Replace_TextBox.get()
            if CheckboxState.get() == 1:
                for ix, word in enumerate(Search_Match2):
                    if myword1.lower() in word.lower() or myword1.lower() == word.lower():
                        color_text(TextBox_Main, tags[ix], word, 'blue', 'yellow')
                    else:
                        color_text(TextBox_Main, tags[ix], word, 'black', 'white')
            else:
                for ix, word in enumerate(Search_Match2):
                
                    if word == myword1 or myword1 in word:
                        color_text(TextBox_Main, tags[ix], word, 'blue', 'yellow')
                    else:
                        color_text(TextBox_Main, tags[ix], word, 'black', 'white')
            Frame2.place_forget()
            messagebox.showinfo("Success","Your matches had been Replaced Successfully!")


    def ExportText():
        MainText = TextBox_Main.get("1.0",'end-1c')
        if  MainText == "":
            messagebox.showerror("Error","  No Avaiable text to Export!  ")
        else:

            
            CurrentDirectory = os.getcwd()

            ExportWindow = Tk()
            ExportWindow.title("Export to a file...")
            ExportWindow.geometry("450x150+450+230")
            
            # FUNCTIONS
            def HoveredOnExport(event):
                ExportButton["background"] = "green"
                ExportButton["foreground"] = "gold"
            def HoveredOffExport(event):
                ExportButton["background"] = "SystemButtonFace"
                ExportButton["foreground"] = "black"
                
            def HoveredOnBack(event):
                BackButton["background"] = "#FE7F9C"
                BackButton["foreground"] = "red"
            def HoveredOffBack(event):
                BackButton["background"] = "SystemButtonFace"
                BackButton["foreground"] = "black"

            def backButton():
                ExportWindow.destroy()

            def exportButton():
                Filetxt = FilenameTextBox.get()
                Pathtxt = PathTextBox.get()
                if Filetxt == ".txt":
                    messagebox.showerror("Error","  Please Type-in your file name!  ")
                elif Filetxt.endswith(".txt") == False:
                    messagebox.showerror("Error","  This can accept only .txt Files extenstion!  ")
                elif os.path.exists(r"{}".format(Pathtxt)) == False:
                    messagebox.showerror("Error","  Invalid path! Please re-check it..  ")
                else:
                    File_Export = open(Filetxt,"w")
                    File_Export.write(f"\n{TextBox_Main.get('1.0','end-1c')}\n")
                    File_Export.close()
                    messagebox.showinfo("Success",f" Your text had been exported to {Filetxt[:-4]} text file! ")
                    ExportWindow.destroy()
                    
            # WIDGETS
            FrameE1 = Frame(ExportWindow, width = 450, height = 150, bg="white")
            FrameE1.place(x=0,y=0)

            FilenameLabel = Label(FrameE1, text = "File Name", font = ("Arial",12,"bold","underline") ,bg="white")
            FilenameLabel.place(x=5,y=10)

            FileText = StringVar()
            FilenameTextBox = Entry(FrameE1, textvariable = FileText ,font = ("COURIER",12),width=40,bg="SystemButtonFace")
            FilenameTextBox.insert(0,".txt")
            FilenameTextBox.place(x=10,y=35)

            PathLabel = Label(FrameE1, text = "Path", font = ("Arial",12,"bold","underline") ,bg="white")
            PathLabel.place(x=5,y=65)
            
            PathText = StringVar()
            PathTextBox = Entry(FrameE1, font = ("COURIER",12),textvariable = PathText,width=40,bg="SystemButtonFace")
            PathTextBox.insert(0,CurrentDirectory)
            PathTextBox.place(x=10,y=90)            
            
            FrameE2 = Frame(FrameE1,width=450, height = 50,bg="aqua")
            FrameE2.place(x=0,y=120)
            
            ExportButton = Button(FrameE2,text = "Export",font=("Arial",9),command = exportButton)
            ExportButton.bind("<Enter>",HoveredOnExport)
            ExportButton.bind("<Leave>",HoveredOffExport)
            ExportButton.place(x=350,y=2)
            
            BackButton = Button(FrameE2,text = "Back",font=("Arial",9),command = backButton)
            BackButton.bind("<Enter>",HoveredOnBack)
            BackButton.bind("<Leave>",HoveredOffBack)
            BackButton.place(x=400,y=2)
            
            ExportWindow.mainloop()



        
    def HoveredOnPaste(event):
        Button_Paste["background"] = "lightgray"
    
    def HoveredOffPaste(event):
        Button_Paste["background"] = "SystemButtonFace"

    def HoveredOnCopy(event):
        Button_Copy["background"] = "lightgray"
    
    def HoveredOffCopy(event):
        Button_Copy["background"] = "SystemButtonFace"

    def HoveredOnClear(event):
        Button_Clear["background"] = "lightgray"
    
    def HoveredOffClear(event):
        Button_Clear["background"] = "SystemButtonFace"

    def HoveredOnSearch(event):
        Button_Search["background"] = "lightgray"
    
    def HoveredOffSearch(event):
        Button_Search["background"] = "SystemButtonFace"

    def HoveredOnExport(event):
        Export_Button["background"] = "lightgray"
    
    def HoveredOffExport(event):
        Export_Button["background"] = "SystemButtonFace"

    def WordCount():
        Countxt = ""
        MainText = TextBox_Main.get("1.0",'end-1c')
        x = MainText.split()
        Count = 0
        for i in x:
            Count += 1
        Countxt2 = f"Word Count : {Count}"
        if Countxt != Countxt2:
            Countxt = Countxt2
            WordCount_Label.config(text=Countxt)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        WordCount_Label.after(200, WordCount)
        
    def HoveredOnImport(event):
        Import_Button["background"] = "lightgray"
    
    def HoveredOffImport(event):
        Import_Button["background"] = "SystemButtonFace"
        
    def ImportText():
        ImportWindow = Tk()
        ImportWindow.title("Import a file...")
        ImportWindow.geometry("450x150+450+230")

        # FUNCTIONS
        def importButton():
            importPath = ImportPathTextBox.get()
            if importPath == "":
                messagebox.showerror("Error","  Please provide path of txt file to import!  ")
            elif importPath.endswith(".txt") == False:
                messagebox.showerror("Error","  InValid Entry! path source shall include txt file.  ")
            else:
                try:
                    importFile = open(r"{}".format(importPath),"r")
                    importText = importFile.read()
                    MainText = TextBox_Main.get("1.0",'end-1c')
                    if MainText != "":
                        MsgBox = messagebox.askquestion("Import File","Importing file, will overwrite the existing string on the board, Continue?")
                        if MsgBox == "yes":
                            TextBox_Main.delete(1.0, END) 
                            TextBox_Main.insert(END, importText)
                            messagebox.showinfo("Success","Your file contents had been imported successfully to the board!")
                            ImportWindow.destroy()
                    else:
                        TextBox_Main.insert(END, importText)
                        messagebox.showinfo("Success","Your file contents had been imported successfully to the board!")
                        ImportWindow.destroy()
                except Exception as err:
                    messagebox.showerror("Error",err)
                    
        def back2Button():
            ImportWindow.destroy()
        
        def HoveredOnImport(event):
            ImportButton["background"] = "green"
            ImportButton["foreground"] = "gold"
        def HoveredOffImport(event):
            ImportButton["background"] = "SystemButtonFace"
            ImportButton["foreground"] = "black"
            
        def HoveredOnBack2(event):
            Back2Button["background"] = "#FE7F9C"
            Back2Button["foreground"] = "red"
        def HoveredOffBack2(event):
            Back2Button["background"] = "SystemButtonFace"
            Back2Button["foreground"] = "black"

        # WIDGETS
        FrameI1 = Frame(ImportWindow, width = 450, height = 150, bg="white")
        FrameI1.place(x=0,y=0)

        ImportPathLabel = Label(FrameI1, text = "Fill with you full file path", font = ("Arial",15,"bold","underline") ,bg="white")
        ImportPathLabel.place(x=5,y=15)
        
        ImportPathTextBox = Entry(FrameI1, font = ("COURIER",17),width=30,bg="SystemButtonFace")
        ImportPathTextBox.place(x=10,y=50)
        
        FrameI2 = Frame(FrameI1,width=450, height = 50,bg="aqua")
        FrameI2.place(x=0,y=120)
        
        ImportButton = Button(FrameI2,text = "Import",font=("Arial",9),command = importButton)
        ImportButton.bind("<Enter>",HoveredOnImport)
        ImportButton.bind("<Leave>",HoveredOffImport)
        ImportButton.place(x=350,y=2)
        
        Back2Button = Button(FrameI2,text = "Back",font=("Arial",9),command = back2Button)
        Back2Button.bind("<Enter>",HoveredOnBack2)
        Back2Button.bind("<Leave>",HoveredOffBack2)
        Back2Button.place(x=400,y=2)
        
        ImportWindow.mainloop()
#===============================================
            


#================================================
        
    # Fonts
    Button_Font = ("tahoma",10,"bold")
    Title_Font = ("Times New Roman",20,"bold","underline")
    Label_Font = ("Arial",12,"bold")
    TextBox_Font = ("Palatino")

    
#================================================
    
    # Widgets
    Frame1 = Frame(Home,width = Home_width , height = Home_height,bg="lightgrey")
    Frame1.pack()

    Label_Title = Label(Frame1, text = "Text Finder",fg = "white", bg="lightgrey", font= Title_Font)
    Label_Title.place(x=5,y=-3)

    Label_Find = Label(Frame1, text = "Find :",fg= "white", bg ="lightgrey", font= Label_Font)
    Label_Find.place(x=90,y=65)

    Label_Matches = Label(Frame1, text = "Matched",font =Title_Font,fg= "white", bg= "lightgray")
    Label_Matches.place(x=640,y=100)

    Label_Date = Label(Frame1, text = CurrentDate,font = Label_Font,bg= "lightgray",fg = "white")
    Label_Date.place(x=700,y=10)

    Label_Clock = Label(Frame1, font = Label_Font,bg= "lightgray",fg = "white")
    Label_Clock.place(x=705,y=32)
    
    TextBox_Main = Text(Frame1, width = 75,height = 27,spacing1 = 1)
    TextBox_Main.place(x=5,y=100)
    
    
    TextFind = StringVar()
    TextBox_Find = Entry(Frame1,width = 40,font =TextBox_Font, textvariable = TextFind)
    TextBox_Find.place(x=145,y=65)
    
    Button_Paste = Button(Frame1, text = "Paste text" , font = Button_Font, command = PasteText)
    Button_Paste.bind("<Enter>",HoveredOnPaste)
    Button_Paste.bind("<Leave>",HoveredOffPaste)
    Button_Paste.place(x=5,y=66)
    
    Button_Copy = Button(Frame1, text = "Copy text " , font = Button_Font, command = CopyText)
    Button_Copy.bind("<Enter>",HoveredOnCopy)
    Button_Copy.bind("<Leave>",HoveredOffCopy)
    Button_Copy.place(x=5,y=35)
    
    Button_Clear = Button(Frame1, text = '" "', font = Button_Font, command = ClearText)
    Button_Clear.bind("<Enter>",HoveredOnClear)
    Button_Clear.bind("<Leave>",HoveredOffClear)
    Button_Clear.place(x=580,y=66)

    Button_Search = Button(Frame1, text = "Search",font = Button_Font, command = SearchText)
    Button_Search.bind("<Enter>",HoveredOnSearch)
    Button_Search.bind("<Leave>",HoveredOffSearch)
    Button_Search.place(x=510,y=66)

    ListBox_Matches = Listbox(Frame1,width=25,height=25)
    ListBox_Matches.place(x=620,y=140)

    CheckboxState = IntVar()
    CheckBox_Casing = Checkbutton(Frame1, onvalue = 1,offvalue=0,variable = CheckboxState,text = "Ignore-upper&lower case",bg="lightgray")
    CheckBox_Casing.place(x=310,y=40)

    Frame2 = Frame(Frame1,width = 190 , height = 40,bg ="lightgray")
    #Frame2.place(x=440,y=2)

    Replace_Label = Label(Frame2,text = "Replace:",bg = "black", fg="white",font = Label_Font)
    Replace_Label.place(x=2,y=5)

    ReplaceText = StringVar()
    Replace_TextBox = Entry(Frame2, width =12, textvariable = ReplaceText)
    Replace_TextBox.place(x=80,y=8)

    Replace_Button = Button(Frame2, text = "Go!",bg = "Yellow",fg="black",command = ReplacingText)
    Replace_Button.place(x=160,y=8)

    imageexport = "export2.png"
    if os.path.isfile(imageexport) == True:
        photo = PhotoImage(file = imageexport)
        Export_Button = Button(Frame1, image= photo, command = ExportText)
        Export_Button.place(x=740,y=65)
    else:
        Export_Button = Button(Frame1, text= "Export", command = ExportText)
        Export_Button.place(x=740,y=65)
    Export_Button.bind("<Enter>",HoveredOnExport)
    Export_Button.bind("<Leave>",HoveredOffExport)
    

    imageimport = "import.png"
    if os.path.isfile(imageimport) == True:
        photo2 = PhotoImage(file = imageimport)
        Import_Button = Button(Frame1, image= photo2, command = ImportText)
        Import_Button.place(x=700,y=65)
    else:
        Import_Button = Button(Frame1, text= "Import", command = ImportText)
        Import_Button.place(x=690,y=65)
    Import_Button.bind("<Enter>",HoveredOnImport)
    Import_Button.bind("<Leave>",HoveredOffImport)
    
    
    WordCount_Label = Label(Frame1 , text = "Word Count : ",font = Label_Font,fg = "white",bg="lightgray")
    WordCount_Label.place(x=100,y=35)
    
    tick()
    WordCount()
    Home.mainloop()



print(TextFinderv1_Run.__doc__)
if __name__ == "__main__":
    TextFinderv1_Run()
    




    
