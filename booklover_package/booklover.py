import pandas as pd
import numpy as np
class BookLover():
    '''Stores data about books users have read.'''
    
    
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self,name,email,fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        
        
    def add_book(self,book_name,book_rating):
        # Check if value book_name exists in any rows of any columns
        if self.book_list.isin([book_name]).any().any():
            print("Book already exists in the DataFrame")
        else:
            self.num_books += 1
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
        
    def has_read(self,book_name):
        #The method should return True if the person has read the book, False otherwise.
        if self.book_list.isin([book_name]).any().any():
            return True
        else:
            return False
        
             
    def num_books_read(self):
        #return self.book_list.shape[0]
        return self.num_books
    
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
    

        