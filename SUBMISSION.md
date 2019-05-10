There are two endpoints

GET /route/shortest/

params:
	origin:      String   {The three digit code of the airport of origin}
	destination: String   {The three digit code of the airport of destination}

returns:
	A json representation of the shortest route
	
Example:
	http://127.0.0.1:5001/route/shortest/?origin=COO&destination=WAW
	
result:
	[
	  [
	    "COO", 
	    "ABJ"
	  ], 
	  [
	    "ABJ", 
	    "IST"
	  ], 
	  [
	    "IST", 
	    "WAW"
	  ]
	]


GET /route/shortest/pretty/

params:
	Same as above

returns:
	String representations of the routes, including names of airports and airlines
	
Example:
	http://127.0.0.1:5001/route/shortest/pretty?origin=COO&destination=WAW
	
result:
	From Cadjehoun Airport to Port Bouet Airport via United Airlines
	From Port Bouet Airport to Atatürk International Airport via Turkish Airlines
	From Atatürk International Airport to Warsaw Chopin Airport via Turkish Airlines

If the names of the Airports or Airlines are not available on the dataset, the code is shown.


To run, install the latest version of python2.x, and use pip to install the additional libraries: flask,pandas
after that, run the app with python: 

python TakeHome.py

The app is set to use the por 5001.