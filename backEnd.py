# the imports so far, LEAVE THEM ALONE, if you wanna do anything, add to them in a seperate list 
import pymongo
import datetime as dt

# space for your imports:





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# this is important and allows for the database to work, dont touch it
myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myClient["mydatabase"]
mCollec = myDB["posts"]


# this is largely unimportant, its what im trying to construct the posts out of, you can add to it but please dont remove anything
dic = {"postType" : "", 
              "title" : "", 
              "text" : "", 
              "date+time" : ""
    }


# prints out all the items in the collection
def displayInCollection():
    for x in mCollec.find():
        print(x)

# this is a command line interpretation of what i want from the final product, leave it alone pls
def makePost():
    time = dt.datetime.now()
    print("""What is post type: 
          a) announcement
          b) news
          c) work
          """)
    inp = input()
    if (inp=="a"):
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

# this adds a dictionary to the collection
def addDicToCollection(collection, dictionary):
    collection.insert_one(dictionary)


def formatPosts():
    pass
    
