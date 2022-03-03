import pymongo
import datetime as dt

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

myDB = myClient["mydatabase"]

mCollec = myDB["posts"]

dic = {"postType" : "", 
              "title" : "", 
              "text" : "", 
              "date+time" : ""
    }

def displayInCollection():
    for x in mCollec.find():
        print(x)


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
              "date+time" : time
    }
    addDicToCollection(dic)
        
def addDicToCollection(dictionary):
    mCollec.insert_one(dictionary)
    
    
    
if __name__ == "__main__":
    makePost()
    displayInCollection()
    
    
