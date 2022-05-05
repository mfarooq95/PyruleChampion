# Import external packages
from flask import Response, request
from flask_restful import Resource

# Local imports -- database models
from database.models import OneHandedWeapons, User

# Flask RESTFUL Resource for working with all One-Handed Weapons documents and the collection
class OneHandedWeaponsAPI(Resource):
    # Function runs when a GET request is made to the route with this resource; gathers all documents/objects in the collection, converts them to json and stores it
    def get(self):
        # Access all objects or documents in collection by calling <.obejcts()> method on class OneHandedWeapons; convert data to json with <.to_json()> method
        all_onehanded_weapons = OneHandedWeapons.objects().to_json()
        # Use Response to return data passed into its parameters
        return Response(response = all_onehanded_weapons, mimetype = "application/json", status = 200)

    # Function runs when a POST request is made to the route with this resource; gathers data sent to API and converts it to json and stores it into database/collection
    def post(self):
        # Get data sent to POST request; convert data to json and store it
        body = request.get_json()
        # Unpack converted json data into document model/schema and use <.save()> method to save data into collection/database; store new entry into variable
        new_entry = OneHandedWeapons(**body).save()
        # Get id of new entry by accessing its 'id' property saved in the document after being unpacked accordingly; save 'id' value of new entry to variable
        id = new_entry.id
        # Return dictionary/json data with new entry's id and status code
        return {'id': str(id)}, 200

# Flask RESTUFL Resource for wokring with single One-Handed Weapon documents/objects in the collection
class OneHandedWeaponAPI(Resource):
    # Function runs when a GET request is made to the route with this resource; gathers individual document/object in the collection matching criteria, converts them to json and stores it
    def get(self, id):
        # Access documents within the collection schema/model by appending the <.objects()> method to class; then appending <.get()> method to search for individual document in collection with given cirtera via parameters; converts document data to json with <.to_json()> and stores it
        entry = OneHandedWeapons.objects().get(id = id).to_json()
        # Use Response to return entry parsed from the collection by its id property/value by passing into Response's parameters
        return Response(response = entry, mimetype = "application/json", status = 200)

    # Function runs when a GET request is made to the route with this resource; gathers individual document/object in the collection matching criteria, converts them to json and stores it
    def delete(self, id):
        # Repeat function similar to line 32, but instead of converting document data to json and storing it, simply remove document by appending <.delete()> method onto document/object
        entry = OneHandedWeapons.objects.get(id = id).delete()
        # Return empty string and status code
        return '', 200