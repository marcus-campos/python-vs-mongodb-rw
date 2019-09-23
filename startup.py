import time
from multiprocessing import Process
from random import randint

from pymongo import MongoClient

#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient(port=27020)
db=client.business

#Step 2: Create sample data
def insertReviews():
    names = ['Kitchen', 'Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
    company_type = ['LLC', 'Inc', 'Company', 'Corporation']
    company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

    for x in range(1, 1001):
        business = {
            'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
            'rating' : randint(1, 5),
            'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
        }
        #Step 3: Insert business object directly into MongoDB via isnert_one
        result=db.reviews.insert_one(business)
        #Step 4: Print to the console the ObjectID of the new document
        print('Created {0} of 1000 as {1}'.format(x,result.inserted_id))
    #Step 5: Tell us that you are done
    print('Finished creating 1000 business reviews')

#Step 6: Search data
def searchReviews():
    names = ['Kitchen', 'Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
    company_type = ['LLC', 'Inc', 'Company', 'Corporation']
    company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

    for x in range(1, 50001):
        result = db.reviews.find({"$text": {"$search": company_cuisine[randint(0, (len(company_cuisine)-1))]}}).limit(10)
        print('Search {0} of 50000 - {1}'.format(x,result))
    #Step 7: Tell us that you are done

if __name__ == "__main__":
    s = time.perf_counter()
    p1 = Process(target=insertReviews)
    p1.start()
    p2 = Process(target=searchReviews)
    p2.start()
    p1.join()
    p2.join()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
