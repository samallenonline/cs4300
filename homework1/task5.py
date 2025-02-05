# TASK 5: Lists and Dictionaries 

# create a list of your favorite books, including book titles and authors 
def get_top_three_albums():
    # (I don't read books as often as I used to, but I love music so I will be making a list of some of my favorite albums instead)
    my_favorite_albums = ["E - Ecco2k", "Slide - George Clanton", "Warlord - Yung Lean", "Age Of - Oneohtrix Point Never", "The OOZ - King Krule"]
    
    # use list slicing to return the first three (albums) in the list for testing
    return(my_favorite_albums[0:3])

# return values from database for testing 
def get_student_info():
    # create a dictionary that represents a basic student database, including student names and IDs
    student_database = {
        "Name": "Sam Allen",
        "ID": "110782875"
    }
    return student_database, student_database["Name"], student_database["ID"]

if __name__ == "__main__":
    # print the results of each function
    print(get_top_three_albums())
    print(get_student_info())
