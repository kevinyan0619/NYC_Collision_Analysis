'''
This package inits a user interaction system, displaying relevant tables, maps, figures, 
or descriptions according to commands entered by user.
Version 1
Copyright:
@ Nan Wu 
@ nw1045@nyu.edu
@ wooginawunan@gmail.com
'''
#"WN_User_Interact"
#if __name__ == '__main__':

from .Interaction_Modules  import ProgramIntroduction
from .Interaction_Modules import Mainmenu
if __name__ == "WN_User_Interact":
     
    ProgramIntroduction()
    Mainmenu()
    
    
    
    
    print('Finished!')
