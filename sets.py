#-----------Day_1-------------------
#-------class_11_sets method_use _in _python--------
arman_watchlist = {"Iron Man", "Avengers", "Batman", "Interstellar"}
rahul_watchlist = {"Batman", "Spiderman", "Avengers", "Inception"}
print(f"Arman_watchlist is : {arman_watchlist}")
print(f"Rahul_watchlist is : {rahul_watchlist}")
print("------------------------")
print(arman_watchlist.intersection(rahul_watchlist))
print("------------------------------------")
print(arman_watchlist.difference(rahul_watchlist))
print("------------------------------------")

print(rahul_watchlist.union(arman_watchlist))
print("-------------------------------------------------")
print("Iron Man" in rahul_watchlist)

#-------------------------------------------------------------------
#------------Day_2-------------------------
#----------Saets_wuth_functions_use_and_conditional_statement_use-----------
def pasword_check_systam():
	vailid_pasword= {"arman123","jarvish01","python77"}
	pasword= input("Enter your old pasword :")
	if (pasword in (vailid_pasword)):
		print("Your pasword sucsessfull change :")
	else:
		print("wrong pasword try again")
		
pasword_check_systam()
