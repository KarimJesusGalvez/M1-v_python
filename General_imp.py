'''

'''


from Bibliographic_entry import Bibliographic_entry
from input import input

class General_imp(input):

    # /**
    #  * general Interfaces.input
    #  * a string type input
    #  * @return The inputted String
    #  * Should be evaluated with evaluate()
    #  */
    def input():

        option = "temp"

        try:
            option = input()
            
        except:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            option = "7"

        return option

    # /**
    #  * An iterator input
    #  * The method print should be invoked before this call
    #  * @param length nº of inputs to pass
    #  * @return an array with the inputs
    #  */
    def input(length:str):

        atrib_array = length
        for a in length:

            print("No trailing white spaces")
            atrib_array[a] = input
        
        return atrib_array

    # /**
    #  *Saves input and matches them to the types provided
    #  * @param type An array of Strings to print before the input
    #  * @return an array with the inputs matching the type indexes
    #  */
    def input(typeof:list) :
        
    
        atrib_array = typeof.length
        for a in typeof:

            print("Please insert: "+ type[a])
            atrib_array[a] = input()
        
        return atrib_array

    # /**
    #  * Simple input
    #  * @param length placehoder to avoid @override of other methods
    #  * @return An int
    #  */
    def input(length:int):
        option = 0

        try :
            option = input()
        except:
            print(" ")
            print(" ")
            print(" ")
            print(" ")

        return option


    def print(registries:list):
        if registries.isEmpty():
            print("No registries to print")
        else:
            for media in registries:

                media.print_atrib()
                print("===")

    def print():
        print("")
        print("Select an option")
        print("")
        print("Option 1 - (P)rint all registries")
        print("")
        print("Option 2 - (C)heck a registry")
        print("")
        print("Option 3 - (A)dd registry")
        print("Option 4 - (M)odify a registry")
        print("")
        print("Option 5 - (E)rase registry")
        print("Option 6 - (D)elete the Database")
        print("")
        print("Option 7 - (S)hutdown")
        print("")
         # println("Option -1 - (T)est")
    


    def print_type(typeof:str):

        print(" ")
        print("Introduce " +  typeof)
        print("Enter EXIT to stop adding names")

    def print_mod_array(atrib:str):
        print("Select the index of the" + atrib + " to replace")
        print("or -1 to annex it to the list, if empty enter any number")

        construct_gen = General_imp()
        placeholder = 0
        ans = construct_gen.input(placeholder)
        return ans


#  // END of class
