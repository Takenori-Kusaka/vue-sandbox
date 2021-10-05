from index import *

# URL
app.add_api_route('/', index)
app.add_api_route('/videofiles/{foldername}/{filename}', videofile)
