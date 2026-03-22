2026-03-21 16:32

Status: Incomplete

Tags: [[Day 33 - API Endpoints & API Parameters]]
[[Day 37 - API Post Reqs and Headers]]

## **What is REST**
It stands for Representational State Transfer, In order to understand what this means, we have to understand the Client > Server Architecture, this is the architecture that the entire server is built on.
The other styles are GraphQL, SOAP and FALCOR. But REST is the gold standard for web APIs.
It's essentially a set of rules that web developers use when building APIs.
**How to make an API RESTful**
- Use HTTP Request Verbs
- Use Specific pattern of Routes/Endpoint URLs
*HTTP Verbs*
GET, POST, PUT, PATCH(new) and DELETE.They are very similar to CRUD functions

*Specific pattern of Routes/Endpoints*
In our server we can specify specific routes  in order to access certain resources. In order for our API to be RESTful we have to have a certain pattern for our routes.
![[Restful Routing.png]]
### Creating an API
REST APIs usually return json data, so in order to return our resource, we have to return our SQLAlchemy Object into A JSON. This process is called *Serialization*. Flask has a serialization helper method built in called jsonify(). But we have to provide a structure for the JSON to return.
```
@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
    return jsonify(
        Cafe={
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
            "has_sockets": random_cafe.has_sockets,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "id": random_cafe.id,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "map_url": random_cafe.map_url,
            "name": random_cafe.name,
            "seats": random_cafe.seats,
        }
    )

```
You can also make the Cafe class a dataclass using the @dataclass decorator from the dataclasses package to make serialization simpler
```
from dataclasses import dataclass
@dataclass  # We can make this class a dataclass to make serialization simpler
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
    return jsonify(Cafe=random_cafe)

```
We can also restructure responses to omit some properties or even create sub sections
```

|@app.route("/random")|
|def get_random_cafe():|
|result = db.session.execute(db.select(Cafe))|
|all_cafes = result.scalars().all()|
|random_cafe = random.choice(all_cafes)|
|return jsonify(cafe={|
|#Omit the id from the response|
|# "id": random_cafe.id,|
|"name": random_cafe.name,|
|"map_url": random_cafe.map_url,|
|"img_url": random_cafe.img_url,|
|"location": random_cafe.location,|
||
|#Put some properties in a sub-category|
|"amenities": {|
|"seats": random_cafe.seats,|
|"has_toilet": random_cafe.has_toilet,|
|"has_wifi": random_cafe.has_wifi,|
|"has_sockets": random_cafe.has_sockets,|
|"can_take_calls": random_cafe.can_take_calls,|
|"coffee_price": random_cafe.coffee_price,|
|}|
|})
```
The SQLAlchemy object returns a dict object i.e. random_cafe.__dict__ but it contains an extra key "_sa_instance_state". it can be removed and rendered as follows
```
@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
    random_cafe.__dict__.pop("_sa_instance_state")
    return jsonify(Cafe=random_cafe.__dict__)
```

To get all the entries in the database at the api endpoint
```
@app.route("/all", methods=["GET"])
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()

    return jsonify(cafes=all_cafes)

```

Accessing cafes based on their location using url parameters
```
@app.route("/search", methods=["GET"])
def search_location():
    location = (request.args.get("loc")).title()
    cafes_in_location = (
        db.session.execute(db.select(Cafe).where(Cafe.location == location))
        .scalars()
        .all()
    )
    if cafes_in_location:
        return jsonify(cafes=cafes_in_location)
    else:
        return jsonify(
            errors={"Not Found": "Sorry, we don't have a cafe at that location."}
# when a user enters /search?loc=somewher, the api returns all data in somewhere else it returns an error.
```

### Interacting APIs
Interacting with your api can get tiring if you have to continue typing everything out in your url, we can use tools like Postman to test apis.

#### HTML PUT and PATCH 
- PUT - Updating the database by sending an entire entry to replace the previous one.
- PATCH - updating just a part of the entire entry.
 #Note In order to pass a response code, you can place it after your jsonify data after a comma
 ```
 return jsonify(response), 404 # response code
 ```

#### syntax


## References
[jsonify Docs](https://tedboy.github.io/flask/generated/flask.jsonify.html)
[Flask jsonify](https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify)
[Create API docs with Postman](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/)
[Cafe API project](https://github.com/kayymarklearn/small_python_projects/tree/8d09cce414244d75b47366c864f5bb2fcc4b43bf/cafe_api)
[Blog project](https://github.com/kayymarklearn/small_python_projects/tree/8d09cce414244d75b47366c864f5bb2fcc4b43bf/blog_with_db)
