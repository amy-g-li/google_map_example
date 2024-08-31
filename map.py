from flask import Flask, request, render_template

app = Flask(__name__)

# /map/
# /map/?island=oahu
@app.route('/map/')
def maps():
  island = request.args.get('island')
  vaild_islands = ["oahu", "kauai", "maui", "big_island","molokai"]
  if island in vaild_islands:
    return(
      render_template(
        'map.html',
        valid_island_template=True,
        island_name_template=island,
      )
    )
  else:
    return(
      render_template(
        'map.html',
        valid_island_template=False,
        island_name_template=island
      )
    )
  
# /traps/
# /traps/?island=oahu
@app.route('/traps/')
def traps():
  island = request.args.get('island')

  # Put the JSON of the trap locations here please
  # Each island has their own if,elif,else block
  if island == "kauai":
    locations = [{
      "name": "k56",
      "coordinates": {
        "latitude": 22.0964,
        "longitude": -159.5261,
      },
      "count": 0,
    }]
  elif island == "oahu":
    locations = [{
      "name": "k54",
      "coordinates": {
        "latitude": 21.2998,
        "longitude": -157.8148,
      },
       "count": 1,
    }]
  elif island == "maui":
    locations = [{
      "name": "k58",
      "coordinates": {
        "latitude": 20.7984,
        "longitude": -156.3319,
      },
      "count": 2,
    }]
  elif island == "big_island":
    locations = [{
      "name": "k59",
      "coordinates": {
        "latitude": 19.5429,
        "longitude": -155.6659,
      },
      "count": 3,
    }]
  elif island == "molokai":
    locations = [{
      "name": "k52", 
      "coordinates": {
        "latitude": 21.1444,
        "longitude": -157.0226,
      },
      "count": 4,
    }]
  else:
    locations = []

  return locations
# BYE BYE SEE YOU IN ANOTHER LIFE 