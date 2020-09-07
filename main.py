import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import os
from PIL import ImageTk, Image
from tkinter import filedialog
from PyPDF2 import PdfFileReader
from collections import OrderedDict
import datetime
import sqlite3
import shutil



class MainfileApplication():

    def __init__(self):
                
        self.Main_Window = tk.Tk()
        self.Main_Window.title("My_BooK")
        self.Main_Window.geometry("1500x800+100+100")
        #self.Main_Window.resizable(False, False)

        self.disBookList = {}
        self.disBookList["Title"] = self.Title_List = []
        self.disBookList["Author"] = self.Author_List = []
        self.disBookList["Category"] = self.Category_list = []
        self.disBookList["Length"] = self.Length_list = []
        
        self.Amount_Book = 1
        self.Amount_Data = 1

        # Variable
                # Author Tuple
        self.btn_All_AuthorName = ['Author1', 'Author2', 'Author3']
        self.Author_index = 0

                # Category Tuple
        self.btn_All_CategoryName = ['Category1', 'Category2', 'Category3']
        self.Category_index = 0

                # Album Tuple

        self.Add_Data_Into_App()


        # Frame

        self.leftFrame_mainWindow = tk.Frame(self.Main_Window)
        self.leftFrame_mainWindow.pack(side = 'left', fill = 'y')
        self.leftFrame_mainWindow.config(background = '#a6a6a6')

        #self.topFrame_mainWindow = tk.Frame(self.Main_Window )
        #self.topFrame_mainWindow.pack(side = 'top', fill = 'x')
        #self.topFrame_mainWindow.config(background = '#666666')
        
        self.rightFrame_mainWindow = tk.Frame(self.Main_Window)
        self.rightFrame_mainWindow.pack(fill = 'both')

            #
        self.LibraryPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Library2.png")
        self.LibraryPotho_image = self.LibraryPhoto.subsample(3,3)

        self.AuthorPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Author1.png")
        self.AuthorPotho_image = self.AuthorPhoto.subsample(3,3)

        self.CategoriesPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Categories.png")
        self.CategoriesPotho_image = self.CategoriesPhoto.subsample(3,3)

        self.FavoritPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Favorit.png")
        self.FavoritPhoto_image = self.FavoritPhoto.subsample(3,3)

        self.AlbumPhoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Album.png")
        self.AlbumPotho_image = self.AlbumPhoto.subsample(3,3)


        # InterFace 
                            # TopFrame
        #self.lblTitle_TopFrame = tk.Label(self.topFrame_mainWindow, text = 'My BooK', height = '2', font = ('defule',36,'bold'), bg = '#666666')
        #self.lblTitle_TopFrame.pack()


                            # LeftFrame
        self.homephoto = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/home.png")
        self.homePhoto_image = self.homephoto.subsample(1,1)

        self.btnHome_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.homePhoto_image, width = '260' , command = self.homeInterfaceInterface)
        self.btnHome_leftFrame.pack()
        #self.btnHome_leftFrame.configure({"bg": "white", "activebackground": "white"})


        self.btnLibrary_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.LibraryPotho_image, text = '\tLibrary \t\t', bg = 'red', compound = 'left',  command = self.libraryInterface)
        self.btnLibrary_leftFrame.pack()

        self.btnAuthor_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.AuthorPotho_image, text = '\tAuthor \t\t', compound = 'left', command = self.AuthorInterface)
        self.btnAuthor_leftFrame.pack()
        
        self.btnCategory_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.CategoriesPotho_image, text = '\tCategory \t\t', compound = 'left', command = self.CategoryInterface)
        self.btnCategory_leftFrame.pack()

        self.btnFavorit_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.FavoritPhoto_image, text = '\tFevorite \t\t',  compound = 'left', command = self.FavoritInterface)
        self.btnFavorit_leftFrame.pack()

        self.btnAlbum_leftFrame = tk.Button(self.leftFrame_mainWindow, image = self.AlbumPotho_image, text = '\tAlbum \t\t',  compound = 'left', command = self.AlbumInterface)
        self.btnAlbum_leftFrame.pack()

        self.btnExit_leftFrame = tk.Button(self.leftFrame_mainWindow, text = '❌\tExit', height = '2', width = '15', command = self.Main_Window.destroy)
        self.btnExit_leftFrame.pack(side = 'bottom')

        self.homeInterfaceInterface()

        self.Main_Window.mainloop()
        
    def homeInterfaceInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_HomeInterface.pack(pady = 10)

        self.mainFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_HomeInterface.pack(pady =  10)
    
        self.recentFrame_HomeInterface = tk.Frame(self.rightFrame_mainWindow)
        self.recentFrame_HomeInterface.pack(side = 'bottom', fill = 'both')

        # Interface
                        # Title
        self.lblTitle_HomeIterface = tk.Label(self.topFrame_HomeInterface, text = 'Welcome\nto\nLibrary Owner', font = ('Times',20,'bold'))
        self.lblTitle_HomeIterface.pack()

                        # Main
        self.LibraryPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Library2.png")
        self.LibraryPotho_image_HomeInterface = self.LibraryPhoto_HomeInterface.subsample(1,1)
        self.btnLibrary_HomeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.LibraryPotho_image_HomeInterface, text = '\t\tLibrary\t\t', compound = 'top', width = 300, font = ('default',15), command = self.libraryInterface)
        self.btnLibrary_HomeInterface.grid(row = 0, column = 0)

        self.AuthorPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Author1.png")
        self.AuthorPotho_image_HomeInterface = self.AuthorPhoto_HomeInterface.subsample(1,1)
        self.btnAuthor_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.AuthorPotho_image_HomeInterface, text = '\t\tAuthor\t\t\t\t', compound = 'top', font = ('default',15), command = self.AuthorInterface)
        self.btnAuthor_homeInterface.grid(row = 1, column = 0, columnspan = 2)

        self.CategoriesPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Categories.png")
        self.CategoriesPotho_image_HomeInterface = self.CategoriesPhoto_HomeInterface.subsample(1,1)
        self.btnCategory_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.CategoriesPotho_image_HomeInterface, text = '\t\tCategoriest\t\t', compound = 'top', font = ('default',15), command = self.CategoryInterface)
        self.btnCategory_homeInterface.grid(row = 0, column = 1)

        self.FavoritPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Favorit.png")
        self.FavoritPhoto_image_HomeInterface = self.FavoritPhoto_HomeInterface.subsample(1,1)
        self.btnFavorit_homeInterface = tk.Button(self.mainFrame_HomeInterface, image = self.FavoritPhoto_image_HomeInterface, text = '\t\t\tFavorite\t\t', compound = 'top', font = ('default',15), command = self.FavoritInterface)
        self.btnFavorit_homeInterface.grid(row = 1, column = 1, columnspan = 2)

        self.AlbumPhoto_HomeInterface = tk.PhotoImage(file = r"/Users/macbook/Documents/Project/Book_Manager/icon/Album.png")
        self.AlbumPotho_image_HomeInterface = self.AlbumPhoto_HomeInterface.subsample(1,1)
        self.btnAlbum_homeInterfac = tk.Button(self.mainFrame_HomeInterface, image = self.AlbumPotho_image_HomeInterface, text = '\t\tAlbum\t\t', compound = 'top', font = ('default',15), command = self.AlbumInterface)
        self.btnAlbum_homeInterfac.grid(row = 0, column = 2)

        self.btnRefresh_leftFrame = tk.Button(self.mainFrame_HomeInterface, text = 'Refrash', width = '50', height = '3', command = self.resetApplication)
        self.btnRefresh_leftFrame.grid(row = 2, column = 0, columnspan = 3)


        self.lblFrame = tk.LabelFrame(self.rightFrame_mainWindow, text = 'Recent')
        self.lblFrame.pack(fill = 'both', padx = '20', pady = '10')

        self.listRecentBook_HomeInterface = tk.ttk.Treeview(self.lblFrame, column = ('Title', 'Author', 'Category', 'Lenght', 'Favorite' , 'Last Readed', 'Date Added'), show = 'headings', height = '14')
        self.listRecentBook_HomeInterface.pack(pady = '10')

        self.listRecentBook_HomeInterface.column('Title', width = '300')
        self.listRecentBook_HomeInterface.heading('Title', text = 'Title')

        self.listRecentBook_HomeInterface.column('Author', width = '250')
        self.listRecentBook_HomeInterface.heading('Author', text = 'Author')

        self.listRecentBook_HomeInterface.column('Category', width = '150')
        self.listRecentBook_HomeInterface.heading('Category', text = 'Category')
        
        self.listRecentBook_HomeInterface.column('Lenght', width = '130')
        self.listRecentBook_HomeInterface.heading('Lenght', text = 'Length')

        self.listRecentBook_HomeInterface.column('Favorite', width = '130')
        self.listRecentBook_HomeInterface.heading('Favorite', text = 'Favorite')

        self.listRecentBook_HomeInterface.column('Last Readed', width = '100')
        self.listRecentBook_HomeInterface.heading('Last Readed', text = 'Last Readed')

        self.listRecentBook_HomeInterface.column('Date Added', width = '100')
        self.listRecentBook_HomeInterface.heading('Date Added', text = 'Date Added')

    def libraryInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_LibraryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_LibraryInterface.pack(side = 'top', fill = 'x')
        self.topFrame_LibraryInterface.config(background = '#c8c8c8')

        self.mainFrame_libraryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_libraryInterface.pack()
        
        # Interface
                            # Tapbar
        #self.lblnameTap_libraryInterface = tk.Label(self.topFrame_LibraryInterface, text = 'Library', font = ('Times',12,'bold'), bg = '#c8c8c8')
        #self.lblnameTap_libraryInterface.pack(side = 'right')

        self.btnAddBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Add', width = '10',height = '1', command = self.openFileDailog_for_AddFile)
        self.btnAddBook_LibraryInterface.pack(side = 'left')

        self.btnDeleteBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Delete', width = '10', height ='1')
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')      

        self.btnDeleteBook_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Edit', width = '10', height ='1')
        self.btnDeleteBook_LibraryInterface.pack(side = 'left')   

        self.btnBookDetail_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Detail', width = '10', height = '1')
        self.btnBookDetail_LibraryInterface.pack(side = 'left')   

        self.btnFavoritAdding_LibraryInterface = tk.Button(self.topFrame_LibraryInterface, text = 'Favorit Adding', width = '15', height = '1', command = self.FavoritAddingBackend)
        self.btnFavoritAdding_LibraryInterface.pack(side = 'left')

                            # main Interface
        self.listBook_libraryInterface = tk.ttk.Treeview(self.mainFrame_libraryInterface, column = ('ID', 'Title', 'Author', 'Lenght', 'Category', 'Last Readed', 'Date Added'), show = 'headings', height = '50')
        self.listBook_libraryInterface.pack(padx = '10', pady = '10')

        self.listBook_libraryInterface.column('ID', width = '50')
        self.listBook_libraryInterface.heading('ID', text = 'ID')

        self.listBook_libraryInterface.column('Title', width = '300')
        self.listBook_libraryInterface.heading('Title', text = 'Title')

        self.listBook_libraryInterface.column('Author', width = '200')
        self.listBook_libraryInterface.heading('Author', text = 'Author')

        self.listBook_libraryInterface.column('Lenght', width = '130')
        self.listBook_libraryInterface.heading('Lenght', text = 'Length')

        self.listBook_libraryInterface.column('Category', width = '180')
        self.listBook_libraryInterface.heading('Category', text = 'Category')
    
        self.listBook_libraryInterface.column('Last Readed', width = '170')
        self.listBook_libraryInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_libraryInterface.column('Date Added', width = '170')
        self.listBook_libraryInterface.heading('Date Added', text = 'Date Added')

        #self.listBook_libraryInterface.column('Favorite', width = '80')
        #self.listBook_libraryInterface.heading('Favorite', text = 'Favorite')

        self.library_Data_Adding()

    def AuthorInterface(self):

        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_AuthorInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AuthorInterface.config(background = '#dadada')

        self.leftFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_AuthorInterface.pack(side = 'left', fill = 'y')
        #self.leftFrame_AuthorInterface.configure(background = '#c8c8c8')

        self.mainFrame_AuthorInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_AuthorInterface.pack(fill = 'both')

                # Interface
        self.btnAddBook_CategoryInterface = tk.Button(self.topFrame_AuthorInterface, text = 'Add Author', width = '10',height = '2')
        self.btnAddBook_CategoryInterface.pack(side = 'left')

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_AuthorInterface, text = 'Delete Author', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_AuthorInterface, text = 'Edit Author', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.lblnameTap_AuthorInterface = tk.Label(self.topFrame_AuthorInterface, text = 'Author', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AuthorInterface.pack(side = 'right')

        self.listBook_AuthorInterface = tk.ttk.Treeview(self.mainFrame_AuthorInterface, column = ('Title', 'Author', 'Lenght', 'Category', 'Last_Readed' , 'Date_Added'), show = 'headings', height = '80')
        self.listBook_AuthorInterface.pack(padx = '10', pady = '10')

        self.listBook_AuthorInterface.column('Title', width = '250')
        self.listBook_AuthorInterface.heading('Title', text = 'Title')

        self.listBook_AuthorInterface.column('Author', width = '180')
        self.listBook_AuthorInterface.heading('Author', text = 'Author')

        self.listBook_AuthorInterface.column('Category', width = '130')
        self.listBook_AuthorInterface.heading('Category', text = 'Category')

        self.listBook_AuthorInterface.column('Last_Readed', width = '100')
        self.listBook_AuthorInterface.heading('Last_Readed', text = 'Last Readed')
        
        self.listBook_AuthorInterface.column('Date_Added', width = '100')
        self.listBook_AuthorInterface.heading('Date_Added', text = 'Date Added')
        
        #self.listBook_AuthorInterface.column(7, width = '100')
        #self.listBook_AuthorInterface.heading(7, text = 'Favorite')

        self.AuthorNameList_AutorInterface()

    def AuthorNameList_AutorInterface(self):

        self.tvListName = tk.ttk.Treeview(self.leftFrame_AuthorInterface, column = ('Author_Name'), show = 'headings', height = '80')
        self.tvListName.pack(pady = '10')

        self.tvListName.column('Author_Name', width = '250')
        self.tvListName.heading('Author_Name', text = 'All Authors')

        self.AddAuthorlist_into_AuthorInterface()

    def OnDoubleClick_Author(self, event):

        item = self.tvListName.selection()
        print("This is ", str(self.tvListName.item(item ,"values")[0]))

    #def ListName_for_Each_Author(self):

        self.listBook_AuthorInterface = tk.ttk.Treeview(self.mainFrame_AuthorInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_AuthorInterface.pack(padx = '10', pady = '5')

        self.listBook_AuthorInterface.column(1, width = '250')
        self.listBook_AuthorInterface.heading(1, text = 'Title')

        self.listBook_AuthorInterface.column(2, width = '180')
        self.listBook_AuthorInterface.heading(2, text = 'Author')

        self.listBook_AuthorInterface.column(3, width = '130')
        self.listBook_AuthorInterface.heading(3, text = 'Category')

        self.listBook_AuthorInterface.column(4, width = '100')
        self.listBook_AuthorInterface.heading(4, text = 'Last Readed')
        
        self.listBook_AuthorInterface.column(5, width = '100')
        self.listBook_AuthorInterface.heading(5, text = 'Date Added')
        
        self.listBook_AuthorInterface.column(6, width = '100')
        self.listBook_AuthorInterface.heading(6, text = 'Size')
        
        self.listBook_AuthorInterface.column(7, width = '100')
        self.listBook_AuthorInterface.heading(7, text = 'Favorite')

    def CategoryInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()
        # Frame
        self.topFrame_CategoryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_CategoryInterface.pack(side = 'top', fill = 'x')
        self.topFrame_CategoryInterface.config(background = '#dadada')

        self.leftFrame_CategoryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_CategoryInterface.pack(side = 'left', fill = 'y')

        self.mainFrame_CategoryInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_CategoryInterface.pack()


        # Interface
        self.btnAddBook_CategoryInterface = tk.Button(self.topFrame_CategoryInterface, text = 'Add Album', width = '10',height = '2')
        self.btnAddBook_CategoryInterface.pack(side = 'left')

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_CategoryInterface, text = 'Delete Album', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.btnDeleteBook_CategoryInterface = tk.Button(self.topFrame_CategoryInterface, text = 'Edit Album', width = '10', height ='2')
        self.btnDeleteBook_CategoryInterface.pack(side = 'left')      

        self.lblnameTap_CategoryInterface = tk.Label(self.topFrame_CategoryInterface, text = 'Category', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_CategoryInterface.pack(side = 'right')

        self.listBook_CategoryInterface = tk.ttk.Treeview(self.mainFrame_CategoryInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_CategoryInterface.pack(padx = '10', pady = '5')

        self.listBook_CategoryInterface.column(1, width = '250')
        self.listBook_CategoryInterface.heading(1, text = 'Title')

        self.listBook_CategoryInterface.column(2, width = '180')
        self.listBook_CategoryInterface.heading(2, text = 'Author')

        self.listBook_CategoryInterface.column(3, width = '130')
        self.listBook_CategoryInterface.heading(3, text = 'Category')

        self.listBook_CategoryInterface.column(4, width = '100')
        self.listBook_CategoryInterface.heading(4, text = 'Last Readed')
        
        self.listBook_CategoryInterface.column(5, width = '100')
        self.listBook_CategoryInterface.heading(5, text = 'Date Added')
        
        self.listBook_CategoryInterface.column(6, width = '100')
        self.listBook_CategoryInterface.heading(6, text = 'Size')
        
        self.listBook_CategoryInterface.column(7, width = '100')
        self.listBook_CategoryInterface.heading(7, text = 'Favorite')

        self.tvListCategory = tk.ttk.Treeview(self.leftFrame_CategoryInterface, column = ('Category_Name'), show = 'headings', height = '80')
        self.tvListCategory.pack()

        self.tvListCategory.column('Category_Name', width = '250')
        self.tvListCategory.heading('Category_Name', text = 'All Categories')

        for Data in self.btn_All_CategoryName:
            self.tvListCategory.insert("", tk.END, self.Category_index, values = Data)
            self.Category_index = self.Category_index + 1
        self.tvListCategory.bind("<Double-1>", self.OnDoubleClick_Category)

    def OnDoubleClick_Category(self, event):

        item = self.tvListCategory.selection()
        print("This is ", str(self.tvListCategory.item(item ,"values")[0]))

    def FavoritInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()
        # Frame
        self.topFrame_FavoriteInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_FavoriteInterface.pack(side = 'top', fill = 'x')
        self.topFrame_FavoriteInterface.config(background = '#dadada')
        
        self.mainFrame_FevoriteInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_FevoriteInterface.pack(fill = 'both')
        
        # Interface
                            # Tapbar
        self.lblnameTap_FavoriteInterface = tk.Label(self.topFrame_FavoriteInterface, text = 'Favorite', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_FavoriteInterface.pack(side = 'right')

        self.btnAddBook_FavoriteInterface = tk.Button(self.topFrame_FavoriteInterface, text = 'Add', width = '10',height = '2')
        self.btnAddBook_FavoriteInterface.pack(side = 'left')

        self.btnDeleteBook_FavoriteInterface = tk.Button(self.topFrame_FavoriteInterface, text = 'Delete', width = '10', height ='2')
        self.btnDeleteBook_FavoriteInterface.pack(side = 'left')      

                            # main Interface
        self.listBook_FavoriteInterface = tk.ttk.Treeview(self.mainFrame_FevoriteInterface, column = ('Title', 'Author', 'Length', 'Category', 'Last Readed', 'Date Added'), show = 'headings', height = '80')
        self.listBook_FavoriteInterface.pack(padx = '10', pady = '10')

        self.listBook_FavoriteInterface.column('Title', width = '300')
        self.listBook_FavoriteInterface.heading('Title', text = 'Title')

        self.listBook_FavoriteInterface.column('Author', width = '200')
        self.listBook_FavoriteInterface.heading('Author', text = 'Author')

        self.listBook_FavoriteInterface.column('Length', width = '130')
        self.listBook_FavoriteInterface.heading('Length', text = 'Length')

        self.listBook_FavoriteInterface.column('Category', width = '200')
        self.listBook_FavoriteInterface.heading('Category', text = 'Category')

        self.listBook_FavoriteInterface.column('Last Readed', width = '170')
        self.listBook_FavoriteInterface.heading('Last Readed', text = 'Last Readed')

        self.listBook_FavoriteInterface.column('Date Added', width = '170')
        self.listBook_FavoriteInterface.heading('Date Added', text = 'Date Added')
        
        #self.listBook_FavoriteInterfacee.column('Favorite', width = '80')
        #self.listBook_FavoriteInterfacee.heading('Favorite', text = 'Favorite')

        self.Favorite_Insrerting_Data_to_List()

    def AlbumInterface(self):
        for widget in self.rightFrame_mainWindow.winfo_children():
            widget.destroy()

        # Frame
        self.topFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.topFrame_AlbumInterface.pack(side = 'top', fill = 'x')
        self.topFrame_AlbumInterface.config(background = '#dadada')

        self.leftFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.leftFrame_AlbumInterface.pack(side = 'left', fill = 'y')

        self.mainFrame_AlbumInterface = tk.Frame(self.rightFrame_mainWindow)
        self.mainFrame_AlbumInterface.pack(fill = 'both')

        # Interface
        self.btnAddBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Add Album', width = '10',height = '2', command = self.addAlbum_Action)
        self.btnAddBook_AlbumInterface.pack(side = 'left')

        self.btnDeleteBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Delete Album', width = '10', height ='2')
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.btnDeleteBook_AlbumInterface = tk.Button(self.topFrame_AlbumInterface, text = 'Edit Album', width = '10', height ='2')
        self.btnDeleteBook_AlbumInterface.pack(side = 'left')      

        self.lblnameTap_AlbumInterface = tk.Label(self.topFrame_AlbumInterface, text = 'Album', font = ('Times',20,'bold'), bg = '#dadada')
        self.lblnameTap_AlbumInterface.pack(side = 'right')

        self.listBook_AlbumInterface = tk.ttk.Treeview(self.mainFrame_AlbumInterface, column = (1,2,3,4,5,6,7), show = 'headings', height = '30')
        self.listBook_AlbumInterface.pack(padx = '10', pady = '5')

        self.listBook_AlbumInterface.column(1, width = '150')
        self.listBook_AlbumInterface.heading(1, text = 'Title')

        self.listBook_AlbumInterface.column(2, width = '150')
        self.listBook_AlbumInterface.heading(2, text = 'Authot')

        self.listBook_AlbumInterface.column(3, width = '150')
        self.listBook_AlbumInterface.heading(3, text = 'Category')

        self.listBook_AlbumInterface.column(4, width = '100')
        self.listBook_AlbumInterface.heading(4, text = 'Last Readed')
        
        self.listBook_AlbumInterface.column(5, width = '100')
        self.listBook_AlbumInterface.heading(5, text = 'Date Added')
        
        self.listBook_AlbumInterface.column(6, width = '80')
        self.listBook_AlbumInterface.heading(6, text = 'Size')
        
        self.listBook_AlbumInterface.column(7, width = '80')
        self.listBook_AlbumInterface.heading(7, text = 'Favorite')

    def addAlbum_Action(self):
        self.addAlbum_Interface = tk.Toplevel(self.Main_Window)
        self.addAlbum_Interface.title("Album Adding")

        self.mainFrame_AlbumAdding_topLevel = tk.Frame(self.addAlbum_Interface)
        self.mainFrame_AlbumAdding_topLevel.pack()

        self.buttonFrame_AlbumAdding_topLevel = tk.Frame(self.addAlbum_Interface)
        self.buttonFrame_AlbumAdding_topLevel.pack()

        self.lblNameAlbum = tk.Label(self.mainFrame_AlbumAdding_topLevel, text = 'Name')
        self.lblNameAlbum.grid(row = 0, column = 0)

        self.inputNameAlbum = tk.Entry(self.mainFrame_AlbumAdding_topLevel, width = '20')
        self.inputNameAlbum.grid(row = 0, column = 1)

        self.btnCancel = tk.Button(self.buttonFrame_AlbumAdding_topLevel, text = 'Cancel', width = '10', command = self.addAlbum_Interface.quit)
        self.btnCancel.grid(row = 0, column = 0)

        self.btnDone = tk.Button(self.buttonFrame_AlbumAdding_topLevel, text = 'Done', width = '10', command = print("Done!..."))
        self.btnDone.grid(row = 0, column = 1)

        self.addAlbum_Interface.mainloop()
#___________________________________________________________________________________________BACK-END__________________________________________________________________#

    def Add_Data_Into_App(self):

        
        # Database
        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Database')
        self.conn = sqlite3.connect('Libraries.db')
        self.c = self.conn.cursor()

        os.chdir('/Users/macbook/Documents/Project/Book_Manager/Data')

        self.d = os.listdir()

        self.c.execute("SELECT rowid,* FROM Data_list ")

        self.items = self.c.fetchall()

        self.datalist_of_Database = []
        for item in self.items:
            self.datalist_of_Database.append(item[1])

        for row in self.d:
            if row != '.DS_Store':
                print("Row Data:", row)
                if row in self.datalist_of_Database:
                    print("", end="")
                else:
                    self.Title_List.append(str(row))
                    pdf_path = str(row)
                    with open(pdf_path, 'rb') as f:
                        self.pdf = PdfFileReader(f)
                        self.information = self.pdf.getDocumentInfo()
                        self.number_of_pages = self.pdf.getNumPages()

                    self.Author_List.append(str(self.information.author))
                    self.Category_list.append(str(None)) 
                    self.Length_list.append(str(self.number_of_pages))

                    #self.c.execute("""UPDATE Data_list SET Add_Date = self.time_Now 
                    #              WHERE Title = titleData 
                    #              """)
                    #self.conn.commit()


                    Title = str(row)
                    Author = (self.information.author)
                    Category = ('None')
                    Number_of_Pages = (self.number_of_pages)
                    Last_Read = ("None Date")
                    Add_Date = ("Unknown")

                    #print("Author :", self.disBookList['Author'])
                    #print("Title :", self.disBookList['Title'])
                    #print("All Amount data :", len(self.disBookList['Title'][0:]))

                    libraryData = [
                                (Title, Author, Number_of_Pages, Category, Last_Read, Add_Date)
                                ]

                    self.c.executemany("INSERT INTO Data_list VALUES (?,?,?,?,?,?)" , libraryData)
                    self.conn.commit()
                    
                               
    def library_Data_Adding(self):
        self.c.execute("SELECT rowid,* FROM Data_list ")

        self.items = self.c.fetchall()

        for item in self.items:
            print(item)
            if item[2] == None:
                self.listBook_libraryInterface.insert("", tk.END, values = (item[0], item[1], 'Unknown Author', item[3],  item[4], item[5], item[6] ))
            else: 
                self.listBook_libraryInterface.insert("", tk.END, values = (item[0], item[1], item[2], item[3],  item[4], item[5], item[6] ))
            self.listBook_libraryInterface.bind("<Double-Button-1>", self.openFeature)

    def openFeature(self, event):
        self.time_Now = (datetime.datetime.now().astimezone().strftime("%Y-%m-%d,  %H:%M:%S"))
        item = self.listBook_libraryInterface.selection()
        ID_Data = str(self.listBook_libraryInterface.item(item, "values")[0])
        print(ID_Data, 'Open at', self.time_Now)

        #self.c.execute("INSERT INTO Date (LastModifiedTime) VALUES()")
        
        #self.c.execute(f"UPDATE Data_list SET Last_Read = ( date(yyyy-MM-dd HH:mm:ss) ) WHERE rowid = {ID_Data} ")
        #self.conn.commit()
    
    def AddAuthorlist_into_AuthorInterface(self):
        if self.disBookList["Author"] == self.Author_List:
            for a in range(len(self.disBookList["Author"])):
                self.tvListName.insert("", tk.END, values = ((self.disBookList["Author"][a:])))
                self.tvListName.bind("<Double-Button-1>", self.AuthorList)

    def AuthorList(self, event):
        item = self.tvListName.selection()
        print(self.tvListName.item(item, "values")[0])
    
    def FavoritAddingBackend(self):
        Dataitem = self.listBook_libraryInterface.selection()
        FavoriteData = (self.listBook_libraryInterface.item(Dataitem, "values"))
        
        if FavoriteData[6] == '' or FavoriteData != '':

            FavoriteManyData = [
                (
                    FavoriteData[1], FavoriteData[2], FavoriteData[3], FavoriteData[4], FavoriteData[5], FavoriteData[6]
                )
                ]

            self.c.executemany("INSERT INTO Favorite VALUES (?,?,?,?,?,?)", FavoriteManyData)
            self.conn.commit()

    def Favorite_Insrerting_Data_to_List(self):
        self.c.execute("SELECT * FROM Favorite")
        
        self.FavoriteItems = self.c.fetchall()

        for FavoriteItem in self.FavoriteItems:
            self.listBook_FavoriteInterface.insert("", tk.END, values = (FavoriteItem[0], FavoriteItem[1], FavoriteItem[2], FavoriteItem[3], FavoriteItem[4], FavoriteItem[5]))

    def resetApplication(self):
        self.Main_Window.destroy()
        self.__init__()

    def openFileDailog_for_AddFile(self):
        self.Main_Window.filename = tk.filedialog.askopenfilename(initialdir = "/Users/macbook/Documents", title = "Select a pdf file", filetypes = (("pdf files", "*.pdf"),("all files", "*.*")) )

        self.orginalpath = self.Main_Window.filename
        self.destinationPath = "/Users/macbook/Documents/Project/Book_Manager/Data"

        self.o = shutil.move(self.orginalpath, self.destinationPath)
        self.Add_Data_Into_App()

    
    #def FavoriteBackend(sefl):
    #    self.c.execute("CREATE TABLE Facvorite")


if __name__ == "__main__":
    MainfileApplication() 
