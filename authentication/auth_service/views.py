from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.parse
from django.http import HttpResponse
import json
# Create your views here.


def check(request):
    # Encode username and password
    username = urllib.parse.quote_plus("admin")
    password = urllib.parse.quote_plus("Cj5$Mm@hZPMYjxu")

    # Construct the connection URI with encoded username and password
    uri = f"mongodb+srv://{username}:{password}@tamer.9lyvvlj.mongodb.net/sample_airbnb"

    # Connect to MongoDB
    cluster = MongoClient(uri)

    # Access the database and collection
    db = cluster["sample_airbnb"]
    collection = db["listingsAndReviews"]

    # Query the collection

    # Query the collection and convert results to a list of dictionaries
    results = list(collection.find({"_id": "10006546"}))

    # Log or print query results for debugging
    print("Query results:", results)

    # Close the connection
    cluster.close()

    print(results)
    # Return an HttpResponse with the data
    return HttpResponse(results, content_type='application/json')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        body_data = request.body.decode('utf-8')
        body_json = json.loads(body_data)
        username = body_json.get('username')
        password = body_json.get('password')

        username = 'fuck'
        password = 'fuck'
        print(f'Escaped username: {username}')
        print(f'Escaped password: {password}')

        # Initialize client outside the try block
        client = None

        try:
            # Construct the MongoDB connection string with the escaped username and password
            client = MongoClient(
                "mongodb+srv://admin:Cj5$Mm@hZPMYjxu@tamer.9lyvvlj.mongodb.net/")
            db = client["Messages"]
            collection = db["Users"]

            if collection.find_one({'username': username}):
                return JsonResponse({'message': 'Username already exists'}, status=400)

            result = collection.insert_one(
                {'username': username, 'password': password})

            if result.inserted_id:
                return JsonResponse({'message': 'User registered successfully'})

            else:
                return JsonResponse({'message': 'Failed to register user'}, status=500)

        except Exception as e:
            print(f'An error occurred during database operation: {e}')
            return JsonResponse({'message': 'Failed to register user. Database operation error.'}, status=500)

        finally:
            # Close the client connection if it's initialized

            client.close()

    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
