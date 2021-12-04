

from General_imp import *
class Bibliographic_entry:


    def setType(self, typeof:str):
        self.typeof = typeof
    def setFormat(self, formatof:str) :
        self.formatof = formatof
    def setTitle(self, title:str):
        self.title = title
    def setLanguage(self, language:str):
        self.language = language
    def setMain_author(self, main_author:str):
        self.main_author = main_author
    def setGenre(self, genre:str):
        self.genre = genre
    def setLength(self, length:str):
        self.length = length
    def setDate_published(self, date_published:str):
        self.date_published = date_published
     
##    /**
##     * Overrides the print location in memory method
##     * Use split(",") to print in lines
##     */
    def toString(self):
        return "Bibliographic_entry{"  \
                + "; type='" + self.typeof + '\'' \
                + "; format='" + self.formatof + '\''  \
                + "; title='" + self.title + '\''  \
                + "; language='" + self.language  +'\''  \
                + "; genre='" + self.genre + '\'' \
                + "; length='" + self.length + '\''  \
                + "; date_published='" + self.date_published + '\''  \
                + "; main_author='" + self.main_author + '\''  \
                + "; secondary_authors=" + self.secondary_authors  \
                + '}';
    

##
##    /**
##     * Sets the new value for the atribute passed as arg
##     * @param atrib new value of the atrib
##     * @param type type of atribute to change
##     */
    def setatribs(self,atrib:str, typeof:str):
        if (typeof.toLowerCase().contains("genre")):
            self.setGenre(atrib)
        elif (typeof.toLowerCase().contains("length")):
            self.setLength(atrib)
        elif (typeof.toLowerCase().contains("format")):
            self.setFormat(atrib)
        elif (typeof.toLowerCase().contains("date_published")):
            self.setDate_published(atrib)
        elif (typeof.toLowerCase().contains("title")):
            self.setTitle(atrib)
        elif (typeof.toLowerCase().contains("main")):
            self.setMain_author(atrib)
        elif (typeof.toLowerCase().contains("language")):
            self.setLanguage(atrib)
        elif (typeof.toLowerCase().contains("secondary_author")):
            self.setSecondary_authors(atrib)
        else:
            print("No change made in parent's attributes")
                    

    def set_array(self,typeof:str):
        # Calls >> setatribs >> setter
        while (1>0):

            construct = General_imp()

            construct.print_type(typeof)
            ans = construct.input()
            if (ans.equals("EXIT")):
                break;
            self.setatribs(ans, typeof)

    def print_atrib(self):
        atribs =  self.toString()
        temp_array = atribs.split(";")
        count = 0
        for  count in temp_array.length:
            print(temp_array[count])
           



##    /**
##     * Simple iter to add secondary authors
##     * Examples: ilustrator
##     * @param author
##     */
    def setSecondary_authors(self,author:str):

        construct_gen = General_imp();

        print( self.secondary_authors);
        gen_construct = General_imp()

        atrib = "secondary_author";
        ans = gen_construct.print_mod_array(atrib)
        if (ans in self.secondary_authors.length ):
            self.secondary_authors.remove(ans)
        self.secondary_authors.add(author)

            
    def __init__(self,typeof:str,formatof:str,title:str,
             language:str,genre:str,length:str,date_published:str,main_author:str,
             secondary_authors:list):

        construct_gen = General_imp()
        input_print ={"format","title","language","main author","genre","length","date_published"}
        ans_array = construct_gen.input(input_print)
        self.typeof = typeof
        self.formatof = ans_array[0]
        self.title = ans_array[1]
        self.language = ans_array[2]
        self.main_author = ans_array[3]
        self.genre = ans_array[4]
        self.length = ans_array[5]
        self.date_published = ans_array[6]
        self.set_array("secondary_author")

##} // END class bibliographic entry
