# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 
DATA = [ 
	[ "Sl. No." , "Name", "Duration"], 
	[ "1", "Mastermind Problem", "30 mins"], 
	[ "2", "Rock Paper Scissors Problem", "15 mins"], 
	[ "3", "Payement Receipt Problem", "40 mins"], 
	[ "", "", ""], 
	[ "", "Total Time Taken", "1 hour 25 mins"], 
] 
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 
styles = getSampleStyleSheet() 
title_style = styles[ "Heading1" ] 
title_style.alignment = 1
title = Paragraph( "Payement Receipt" , title_style ) 
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
table = Table( DATA , style = style ) 
pdf.build([ title , table ]) 
