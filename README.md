<p align="center">
  <img src=https://user-images.githubusercontent.com/43150822/174932764-b48a6190-b96c-41da-b795-91ec1106956d.png />
</p>

***
<h3 align="center">
  THIS API IS A WIP
 </h3>
<p align="center">
  <img src=https://user-images.githubusercontent.com/43150822/174935064-992e560a-6c83-41d8-b639-5d279a740906.png />
</p>
<p algin="center">
  
## About
**Pyrule Champion** is a REST API for *The Legend of Zelda: Breath of the Wild*, providing detailed data on ingame resources. **Pyrule Champion** is robust and structured, serving data on multiple categories of ingame content at various endpoints, each categorized by their resource type enabling organized data return.

Coded in Python, **Pyrule Champion** is built with the Flask framework and works with MongoDB as its backend database, utilizing `flask-restful` and `flask-mongoengine` to structure, control and communicate the JSON data the API and its database works with.

## Data Categories & Endpoints
The API contains and gives access to ingame data on various content in *Breath of the Wild* such as:
1. Weapons
2. Monsters
3. Creatures
4. Materials

A few of the categories above are broken down even further, allowing for further organization of data:
1. Weapons
   * One-Handed Weapons
   * Two-Handed Weapons
   * Spears
   * Bows
   * Shields

2. Creatures
   * Non-Consumable Creatures
   * Consumable Creatures

3. Materials
   * Non-Consumable Materials
   * Consumable Materials

Each category has its endpoints with its apprpriate resource/content tied to the route available for consumption. Each category has two routes for `GET` requests to be made returning all the data within the database's respective collection as JSON data or returning a single document/entry in the database's respective collection.
  
### Routes
  Below are the currently available API routes:
  ```
  /api/onehandedweapons
  /api/onehandedweapons/<name>
  /api/shields
  /api/shields</name>
  ```

 Note the two routes per data/content category, allowing endusers to consume all documents in the MongoDB database's collection for that ingame content or an individual item/entry/document in the ingame content's respective collection.
  
 **Pyrule Champion** only accepts `GET` requests.
 
Users cannot make any other standard operating CRUD requests to the API: `DELETE`, `PUT`, `POST`, `PATCH`.
 
# Attributions
1. <a href="https://www.flaticon.com/free-icons/work" title="work icons">Work icons created by Freepik - Flaticon</a>
