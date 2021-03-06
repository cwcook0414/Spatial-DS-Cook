# query1 : Finding Features - Examples/Usage
###### `python query3.py [start] [end] [radius]`
  - `[start]` is a 3 character airport code ('DFW'). This is the starting point.
  - `[end]` is a 3 character airport code. This is the endpoint.
  - `[radius]` is in miles.
  - `python query1.py DFW MNL 1000`
  - `python query1.py DFW ORD 300`
###### `python query1.py`
  - Allows the users to click on the map to select starting and ending points.
  - The radius defaults to 500 miles.
  - Left click sets the starting point. Right click sets the ending point. It will not run without both mouse button clicks.
  - `python query2.py`
##### Other:
- query1.png is a picture of the map after all points have been plotted. It is overwritten each time this is run. 
- May have a difficult time finding a path across the oceans.

# query2 : Nearest Feature - Examples/Usage
###### `python query2.py [feature] [field] [field value] [min/max] [max results] [radius] [lon,lat]`
  - `[feature]` must be: 'earthquakes', 'meteorites' or 'volcanos'. Anything else will not work.
  - `[field]` some field in `[properties]`
  - `[field value]` the value to compare with
  - `[min/max]` must be either 'min' or 'max'. Whether we want values greater or less than `[field value]`
  - `[radius]` is in miles.
  - `[lon,lat]` not required! If left blank, the user can click on the map to selct a point. If filled in, the program will ignore all map clicking.
  - `python query2.py earthquakes mag 6 min 6 500 [46.20,-121.937]`
  - `python query2.py earthquakes mag 6 min 6 500 [26.382028,117.070313]`
  - `python query2.py volcanos Altitude 2500 min 6 500 [46.20,-121.937]`
###### `python query2.py [radius]`
  - Allows the users to click on the map to select a point.
  - `radius` is in miles.
  - Finds all features within the radius.
  - `python  query2.py 1500`
  - `python  query2.py 425.1789`
###### `python query2.py`
  - Allows the users to click on the map to select a point.
  - The radius defaults to 200 miles.
  - `python query2.py`
##### Other:
- query2.png is a picture of the map after all points have been plotted. It is overwritten each time any of these are run. 

# query3 : Clustering - Examples/Usage
###### `python query3.py [feature] [min_pts] [eps]`
  - `[feature]` must be: 'earthquakes', 'meteorites' or 'volcanos'. Anything else will not work.
  - `[min_pts]` minimum number of points to make a cluster
  - `[eps]` distance for dbscan
  - `python query3.py earthquakes 3 5`
  - `python query3.py volcanos 3 5`
  - `python query3.py meteorites 3 5`
##### Other:
- query3.png is a picture of the map after all points have been plotted. It is overwritten each time this is run. 
- Only produces 5 clusters.
