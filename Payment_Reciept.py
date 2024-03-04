# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

# data which we are going to display as tables 
DATA = [ 
	[ "Sl. No." , "Name", "Duration"], 
	[ "1", "Mastermind Problem", "30 mins"], 
	[ "2", "Rock Paper Scissors Problem", "15 mins"], 
	[ "3", "Payement Receipt Problem", "40 mins"], 
	[ "", "", ""], 
	[ "", "Total Time Taken", "1 hour 25 mins"], 
] 

# creating a Base Document Template of page size A4 
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 

# standard stylesheet defined within reportlab itself 
styles = getSampleStyleSheet() 

# fetching the style of Top level heading (Heading1) 
title_style = styles[ "Heading1" ] 

# 0: left, 1: center, 2: right 
title_style.alignment = 1

# creating the paragraph with 
# the heading text and passing the styles of it 
title = Paragraph( "Payement Receipt" , title_style ) 

# creates a Table Style object and in it, 
# defines the styles row wise 
# the tuples which look like coordinates 
# are nothing but rows and columns 
style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
		( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.blue ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.salmon ), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.wheat ), 
	] 
) 

# creates a table object and passes the style to it 
table = Table( DATA , style = style ) 

# final step which builds the 
# actual pdf putting together all the elements 
pdf.build([ title , table ]) 
