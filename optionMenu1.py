#python
import BaxUI_S

#Declare our functions
def baxui_printName():
	print BaxUI_S.baxui_var_robotName

#Pass them to BaxUI_S
BaxUI_S.baxui_printName = baxui_printName


#Declare our options
def baxui_opts_robotName():
	#			   The Question			       The variables      The Options [Display,Value]		
	baxui_opts_robotName_Arr = [["What is the robots name?", "baxui_var_robotName"],     ["Bertie","Bertie"],["Baxter","Baxter"]]
	BaxUI_S.showOption(baxui_opts_robotName_Arr)

#Pass them to BaxUI_S
BaxUI_S.baxui_opts_robotName = baxui_opts_robotName

#Remember to pass the initial value of the option as well.
BaxUI_S.baxui_var_robotName = "Baxter" 


mainMenu = [["I do Nothing",""],["Robot Name","baxui_printName"],["Change The Name","baxui_opts_robotName"]]
BaxUI_S.showList(mainMenu)
