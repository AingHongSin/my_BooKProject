from tkinter import *
from tkmacosx import Button
from tkinter import ttk
import tkinter.messagebox
import sqlite3
import Database
import os
from contextlib import contextmanager


class NewAlbumAction():
    def __init__(self):

        self.VarName = StringVar()
        self.AlbumName = []

        self.addAlbum_Interface = Toplevel()
        self.addAlbum_Interface.title("Album Adding")
        self.addAlbum_Interface.geometry('280x100+600+400')

        self.mainFrame_AlbumAdding_topLevel = Frame(self.addAlbum_Interface)
        self.mainFrame_AlbumAdding_topLevel.pack()

        self.buttonFrame_AlbumAdding_topLevel = Frame(self.addAlbum_Interface)
        self.buttonFrame_AlbumAdding_topLevel.pack(pady = 10)

        self.lblTitleAlbum = Label(self.mainFrame_AlbumAdding_topLevel, text = 'Album Title', font = ('defult', 14, 'bold'))
        self.lblTitleAlbum.grid(row = 0, column = 0, columnspan = 2)

        self.lblNameAlbum = Label(self.mainFrame_AlbumAdding_topLevel, text = 'Name')
        self.lblNameAlbum.grid(row = 1, column = 0)

        self.inputNameAlbum = Entry(self.mainFrame_AlbumAdding_topLevel, width = '20', textvariable = self.VarName)
        self.inputNameAlbum.grid(row = 1, column = 1)
        self.inputNameAlbum.bind('<Return>', self.AddAlbumName_to_Database_usingReturnButton)
        self.inputNameAlbum.focus()

        self.btnCancel = Button(self.buttonFrame_AlbumAdding_topLevel, text = 'Cancel', borderless = 4,  command = self.addAlbum_Interface.destroy)
        self.btnCancel.grid(row = 1, column = 0)

        self.btnDone = Button(self.buttonFrame_AlbumAdding_topLevel, text = 'Done', borderless = 4,  command = self.AddAlbumName_to_Database)
        self.btnDone.grid(row = 1, column = 1)

        self.addAlbum_Interface.mainloop()
    


    def AddAlbumName_to_Database_usingReturnButton(self, event):
        self.AddAlbumName_to_Database()

    def AddAlbumName_to_Database(self):
        #os.chdir(os.path.dirname(os.getcwd()))
        print(os.getcwd())
        with self.change_dir('my_BookData/Database'):
            self.conn = sqlite3.connect('Libraries.db')
            self.c = self.conn.cursor()

            self.AlbumName_in_AlbumTable = self.VarName.get()

            if  self.AlbumName_in_AlbumTable != '':
                Database.addAlbum(self.AlbumName_in_AlbumTable)
                self.inputNameAlbum.delete(0, 'end')
                self.addAlbum_Interface.destroy()

                self.AlbumName.append(self.AlbumName_in_AlbumTable)

                self.c.execute("INSERT INTO Album (Album_NameList) VALUES (?)", self.AlbumName[0:])
                self.conn.commit()

                self.AddData_into_List = Toplevel()
                self.AddData_into_List.title('AlbumAdding')
                self.AddData_into_List.geometry('730x330+500+250')


                self.topFrame = Frame(self.AddData_into_List, bg = '#00ebff')
                self.topFrame.pack(fill = 'x', side = 'top')

                self.SecondFrame = Frame(self.AddData_into_List)
                self.SecondFrame.pack(fill = 'x')

                self.mainFrame = LabelFrame(self.AddData_into_List)
                self.mainFrame.pack()

                self.BottomFrame = Frame(self.AddData_into_List, bg = '#00ebff')
                self.BottomFrame.pack(side = 'bottom', fill = 'x')

                # Interface
                self.lblTitle = Label(self.topFrame, text = 'Album Adding Data', bg = '#00EBFF', font = ('Times', 21, 'bold'))
                self.lblTitle.pack()

                self.btnAdd  = Button(self.SecondFrame, text = 'Add', borderless = 4, command = self.AddingFunction)
                self.btnAdd.pack(side = 'right', pady = 5)

                self.listBook_Interface = ttk.Treeview(self.mainFrame, column = ('ID', 'Title', 'Author', 'Lenght', 'Last Readed', 'Date Added'), show = 'headings', height = '10')
                self.listBook_Interface.pack(padx = 10, pady = 10)

                self.listBook_Interface.column('ID', width = '30')
                self.listBook_Interface.heading('ID', text = 'ID')

                self.listBook_Interface.column('Title', width = '180')
                self.listBook_Interface.heading('Title', text = 'Title')

                self.listBook_Interface.column('Author', width = '120')
                self.listBook_Interface.heading('Author', text = 'Author')

                self.listBook_Interface.column('Lenght', width = '50')
                self.listBook_Interface.heading('Lenght', text = 'Length')

                self.listBook_Interface.column('Last Readed', width = '160')
                self.listBook_Interface.heading('Last Readed', text = 'Last Readed')

                self.listBook_Interface.column('Date Added', width = '160')
                self.listBook_Interface.heading('Date Added', text = 'Date Added')

                self.btnDone = Button(self.BottomFrame, text = 'Done', borderless = 4, height = 30, command = self.ReviewFunction)
                self.btnDone.pack(side = 'right', padx = 5, pady = 5)
                
                self.c.execute("SELECT * FROM Data_list ")

                self.items = self.c.fetchall()

                for item in self.items:
                    if item[2] == None:
                        self.listBook_Interface.insert("", END, values = (item[0], item[1], 'Unknown Author', item[3],  item[4], item[5] ))
                    else: 
                        self.listBook_Interface.insert("", END, values = (item[0], item[1], item[2], item[3],  item[4], item[5] ))

                self.AddData_into_List.mainloop()
            else: tkinter.messagebox.showwarning('Warmming', "Please Enter Data into the box")



    def ReviewFunction(self):


        self.Data_in_AlbumName = []
        j = self.AlbumName_in_AlbumTable


        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute(f"SELECT * FROM [{j}]")
        for h in self.c.fetchall():
            self.Data_in_AlbumName.append(h[0])

        if self.Data_in_AlbumName == []:
            self.c.execute(f"DROP TABLE [{j}]")
            self.c.execute("DELETE FROM Album WHERE Album_NameList = (?)", self.AlbumName[0:])
            self.conn.commit()
            self.conn.close()

            tkinter.messagebox.showerror('Error', 'Your book had not been add in to your album.')

        os.chdir(os.path.dirname(os.getcwd()))
        os.chdir(os.path.dirname(os.getcwd()))
        print(os.getcwd())
        self.AddData_into_List.destroy()


    def AddingFunction(self):
        
        DatainAlbumDatabase = []

        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        self.c.execute(f"SELECT * FROM [{self.AlbumName_in_AlbumTable}]")
        for item in self.c.fetchall():
            DatainAlbumDatabase.append(item[1])

        SelectData = self.listBook_Interface.focus()
        Data = self.listBook_Interface.item(SelectData, "values")
        DatafromList = str(Data[1])

        if DatafromList in DatainAlbumDatabase:
            tkinter.messagebox.showerror('Error', 'This book was added already.')
        else:
            if DatafromList != DatainAlbumDatabase:
                Data_Adding_to_Database = [
                        (
                            Data[0], Data[1], Data[2], Data[3], Data[4], Data[5]
                        )
                    ]
                p = self.AlbumName[0]

                self.c.executemany(f"INSERT INTO [{p}] VALUES (?,?,?,?,?,?) ", Data_Adding_to_Database)
                self.conn.commit()

    def AddingFunction_usingDounble_Click(self, event):
        self.AddingFunction()

    @contextmanager
    def change_dir(self, destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)
