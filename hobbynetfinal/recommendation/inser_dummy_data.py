from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hobbynet"]
mentors_collection = db["mentors"]

# Dummy mentor data
dummy_mentors = [
    {"name": "Alice Johnson", "hobby": "Painting", "experience": 5, "rating": 4.8},
    {"name": "Bob Smith", "hobby": "Guitar", "experience": 7, "rating": 4.9},
    {"name": "Charlie Brown", "hobby": "Dancing", "experience": 3, "rating": 4.5},
    {"name": "David Williams", "hobby": "Photography", "experience": 6, "rating": 4.7},
    {"name": "Emma Davis", "hobby": "Painting", "experience": 4, "rating": 4.6},
    {"name": "Frank Miller", "hobby": "Guitar", "experience": 10, "rating": 5.0},
    {"name": "Grace Lee", "hobby": "Dancing", "experience": 8, "rating": 4.9},
    {"name": "Henry Wilson", "hobby": "Photography", "experience": 2, "rating": 4.3},
    {"name": "Isabella Taylor", "hobby": "Painting", "experience": 9, "rating": 5.0},
    {"name": "Jack Thomas", "hobby": "Guitar", "experience": 5, "rating": 4.2}
]

# Insert data into MongoDB
mentors_collection.insert_many(dummy_mentors)

print("Dummy mentor data inserted successfully!")
