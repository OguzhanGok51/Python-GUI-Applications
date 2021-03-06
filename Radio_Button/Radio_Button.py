from tkinter import *

class RadioFont( Frame ):
   def __init__( self ):
      Frame.__init__( self )
      self.pack( expand = YES, fill = BOTH )
      self.master.title( "Radiobutton " ) 

      self.frame1 = Frame( self )
      self.frame1.pack()
      
      self.text = Entry( self.frame1, width = 40,font = "Arial 10" )
      self.text.insert( INSERT, "First solve the problem. Then, write  the code" )
      self.text.pack( padx = 5, pady = 5 )

      self.frame2 = Frame( self )
      self.frame2.pack()
      
      fontSelections = [ "Plain", "Bold", "Italic","Bold/Italic" ]
      self.chosenFont = StringVar()

      self.chosenFont.set( fontSelections[ 0 ] ) 

      for style in fontSelections:
         aButton = Radiobutton( self.frame2, text = style,variable = self.chosenFont, value = style,command = self.changeFont )
         aButton.pack( side = LEFT, padx = 5, pady = 5 )

   def changeFont( self ):
      desiredFont = "Arial 10"

      if self.chosenFont.get() == "Bold":
         desiredFont += " bold"
      elif self.chosenFont.get() == "Italic":
         desiredFont += " italic"
      elif self.chosenFont.get() == "Bold/Italic":
         desiredFont += " bold italic"

      self.text.config( font = desiredFont )

RadioFont().mainloop()
