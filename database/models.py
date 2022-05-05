# Import external packages -- brcypt functions to use with User class
from flask_bcrypt import generate_password_hash, check_password_hash

# Local imports -- functions
from .db import db

# Utilize Monogengine to create document schemas -- call classes to unpack json data into class/schema and save into MongoDB
class OneHandedWeapons(db.Document):
    name = db.StringField(required = True, unique = True)
    item_type = db.StringField(required = True)
    item_series = db.StringField(required = True)
    base_power = db.IntField(required = True)
    base_durability = db.IntField(required = True)
    modifiers = db.ListField(db.StringField(), required = True)
    points_to_evolve = db.StringField(required = True)
    selling_price = db.StringField(required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class TwoHandedWeapons(db.Document):
    name = db.StringField(required = True, unique = True)
    item_type = db.StringField(required = True)
    item_series = db.StringField(required = True)
    base_power = db.IntField(required = True)
    base_durability = db.IntField(required = True)
    modifiers = db.ListField(db.StringField(), required = True)
    points_to_evolve = db.StringField(required = True)
    selling_price = db.StringField(required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class Shields(db.Document):
    name = db.StringField(required = True, unique = True)
    item_type = db.StringField(required = True)
    item_series = db.StringField(required = True)
    base_shieldguard = db.IntField(required = True)
    base_durability = db.IntField(required = True)
    modifiers = db.ListField(db.StringField(), required = True)
    points_to_evolve = db.StringField(required = True)
    selling_price = db.StringField(required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class Bows(db.Document):
    name = db.StringField(required = True, unique = True)
    item_type = db.StringField(required = True)
    item_series = db.StringField(required = True)
    base_power = db.IntField(required = True)
    base_durability = db.IntField(required = True)
    modifiers = db.ListField(db.StringField(), required = True)
    points_to_evolve = db.StringField(required = True)
    selling_price = db.StringField(required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class Monsters(db.Document):
    name = db.StringField(required = True, unique = True)
    monster_series = db.StringField(required = True)
    base_power = db.IntField(required = True)
    base_health = db.IntField(required = True)
    points_per_kill = db.StringField(required = True)
    points_to_evolve = db.StringField(required = True)
    item_drops = db.ListField(db.StringField(), required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class Creatures(db.Document): # Things like Horse
    name = db.StringField(required = True, unique = True)
    creature_series = db.StringField(required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class ConsumableCreatures(db.Document): # Things like Hyrule Bass
    name = db.StringField(required = True, unique = True)
    creature_series = db.StringField(required = True)
    hearts_restored = db.StringField(required = True)
    hearts_restored_cooked = db.StringField(required = True)
    item_drops = db.ListField(db.StringField(), required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class Materials(db.Document): # Things like Sapphire, Swiftwing Butterfly
    name = db.StringField(required = True, unique = True)
    item_type = db.StringField(required = True)
    selling_price = db.StringField(required = True)
    used_in = db.ListField(db.StringField(), required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class ConsumableMaterials(db.Document): # Things like Apples, Raw Gourmet Meat, etc. NOT THE ANIMAL ITSELF, THEY'RE COVERED IN CONSUMABLE CREATRUES
    name = db.StringField(required = True, unique = True)
    item_type = db.StringField(required = True)
    hearts_restored = db.StringField(required = True)
    hearts_restored_cooked = db.StringField(required = True)
    selling_price = db.StringField(required = True)
    used_in = db.ListField(db.StringField(), required = True)
    locations = db.ListField(db.StringField(), required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class Recipes(db.Document):
    name = db.StringField(required = True, unique = True)
    hearts_restored = db.StringField(required = True)
    ingredients = db.ListField(db.StringField(), required = True)
    selling_price = db.StringField(required = True)
    description = db.StringField(required = True)
    url = db.StringField(reuired = True)

class User(db.Document):
    email = db.EmailField(required = True, unique = True)
    password = db.StringField(required = True, min_length = 6)

    # Function takes password given in POST request and hashes it
    def hash_password(self):
        self.password = generate_password_hash(password = self.password).decode('utf8')

    # Function takes password given in POST request on login and checks it against the hashed, saved password
    def check_password(self, password):
        return check_password_hash(pw_hash = self.password, password = password)