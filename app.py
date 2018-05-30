from flask import Flask, Response, redirect, url_for
import requests
app = Flask(__name__, static_url_path='', static_folder='static')


TOKEN = None


@app.route('/location/<query>')
def location(query):
    url = "http://nominatim.openstreetmap.org/search?q=" + query + "&format=json"
    r = requests.get(url, headers={'User-Agent': 'recent-birds'})
    return Response(r.text, mimetype='text/json')


@app.route('/observations/<lat>/<lng>/<dist>/<daysback>/<maxresults>')
@app.route('/observations/<lat>/<lng>/<dist>/<daysback>/<maxresults>/<species>')
def observations(lat, lng, dist, daysback, maxresults, species=None):
    url = 'http://ebird.org/ws2.0/data/obs/geo/recent?fmt=json'
    if species:
        url = 'http://ebird.org/ws2.0/data/obs/geo/recent/' + species + '?fmt=json'
    url += '&dist=' + dist
    url += '&back=' + daysback
    url += '&maxResults=' + maxresults
    url += '&lat=' + lat
    url += '&lng=' + lng
    url += '&includeProvisional=true';

    r = requests.get(url, headers={'X-eBirdApiToken': TOKEN})
    return Response(r.text, mimetype='text/json')


@app.route('/')
def root():
    return redirect(url_for('static', filename='index.html'))


if __name__ == '__main__':
    with open('ebird-api-token') as f:
        TOKEN = f.read().strip()
    app.run()
