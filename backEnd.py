# the imports so far, LEAVE THEM ALONE, if you wanna do anything, add to them in a seperate list
import pymongo
import datetime as dt

# space for your imports, expand as neccessary
# import whatever.py
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# this is important and allows for the database to work, dont touch it
def makeDB():
    Client = pymongo.MongoClient("mongodb://localhost:27017/")
    DataBase = Client["mydatabase"]
    collection = DataBase["posts"]
    
    return collection


# this is a template that i like having as a reference
dic = {"postType" : "", 
              "title" : "", 
              "text" : "", 
              "date+time" : ""
    }

# prints out all the items in the collection ----- this might be useless, remove if such
def displayInCollection():
    for x in mCollec.find():
        print(x)

# this is a command line interpretation of what i want from the final product, getting the data from the website itself
def makePost():
    time = dt.datetime.now() # gets the time so that i can be stored
    print("""What is post type: 
          a) announcement
          b) news
          c) work
          """)
    inp = input()
    if (inp=="a"): # this will be something that decides how it should be outputted later on
        postType = "announcement"
    elif inp=="b":
        postType = "news"
    elif inp=="c":
        postType = "work"
    
    print()
    title = input("Write your title here: \n")
    text = input("Write your text here: \n")
    
        
    dic = {"postType" : postType, 
              "title" : title, 
              "text" : text, 
              "date+time" : time}
    addDicToCollection(mCollec, dic)

# this makes a post into it's useful vars from an inputed dictionary
def storePostAsVars(dictionary):
    title = dictionary["title"]
    text = dictionary["text"]
    type = dictionary["postType"]
    
    return title, text, type

# this adds a dictionary to the collection
def addDicToCollection(collection, dictionary):
    collection.insert_one(dictionary)

# sorts a collection by an input
def sortCollection(collection, sort, ascending):
    
    if ascending:
        return collection.find().sort(sort, 1)
    else:
        return collection.find().sort(sort, -1)

if __name__ == "__main__": # Will only run if the program has
    
    mCollec = makeDB()
    
    makePost()
    
    dicList = sortCollection(mCollec, "date+time", False)
    for x in dicList:
        title, text, _ = storePostAsVars(x)
        print(title)
    


