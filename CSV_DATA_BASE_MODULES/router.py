
def sesion_filter( event : int, possible_variants_of_events: dict ):

	if event in possible_variants_of_events.keys():
		return True,possible_variants_of_events[ event ]

	else:
		return False,None


if __name__ == '__main__':
	events = {
		0 : "view_commands",
		1 : "register",
		2 : "login",
		3 : "replenish_the_balance",
		4 : "view_list_of_all_rooms",
		5 : "book_room_for_date_arrival",
		6 : "book_room_for_date_departure",

	}
	print( "Введите название команды:" )

	answer = sesion_filter( int( input() ), events )
	
	if answer[ 0 ]:
		if answer[ 1 ] == "view_commands":
			for key,value in events.items():
				max_ident = len( max( [ value for key,value in events.items() ], key=len ) ) + 1
				print( f"[ command name %s :: command = {key} ]" % value.ljust( max_ident ), sep= '' )


		elif answer[ 1 ] == "register":
			print( "register sesion")
		
		elif answer[ 1 ] == "login":
			print( "login sesion")

		elif answer[ 1 ] == "replenish_the_balance":
			print( "replenish the balance sesion" )

		elif answer[ 1 ] == "view_list_of_all_rooms":
			print( "view list of all rooms sesion" )

		elif answer[ 1 ] == "book_room_for_date_arrival":
			print(" book room for date arrival sesion ")

		elif answer[ 1 ] == "book_room_for_date_departure":
			print(" book room for date departure sesion")


	else:
		print( "Команда не найдена" )