from flask import Flask, request, render_template

app = Flask(__name__)

# /map/
# /map/?island=oahu
@app.route('/map/')
def maps():
  island_func = request.args.get('island')
  vaild_islands = ["oahu", "kauai", "maui", "big_island","molokai"]
  if island_func in vaild_islands:
    return(
      render_template(
        'map.html',
        valid_island_template=True,
        island_name_template=island_func
      )
    )
  else:
    return(
      render_template(
        'map.html',
        valid_island_template=False,
        island_name_template=island_func
      )
    )
