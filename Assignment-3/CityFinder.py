import urllib.request, urllib.parse, urllib.error
import json
import ssl
from tkinter import *

root = Tk()
root.title('City Details Finder')
e = Entry(root,width=25,borderwidth=5,bg="lightsteelblue",font=('poor richard',18,"bold"))
e.insert(0,'Enter Location...')
root.configure(bg="lightblue")
def xyz():
    count=0
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = e.get()

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)


    print(json.dumps(js, indent=4))
    #placeid
    placeid=('place_id -',js['results'][0]['place_id'])
    #state
    state=str(js['results'][0]['address_components'][2]['long_name'])+" , "+str(js['results'][0]['address_components'][2]['short_name'])

    #country
    country=str(js['results'][0]['address_components'][3]['long_name'])+" , "+str(js['results'][0]['address_components'][3]['short_name'])
    #bounds
    bounds_NE_lat=str(js['results'][0]['geometry']['bounds']['northeast']['lat'])
    bounds_NE_lng=str(js['results'][0]['geometry']['bounds']['northeast']['lng'])
    bounds_SW_lat=str(js['results'][0]['geometry']['bounds']['southwest']['lat'])
    bounds_SW_lng=str(js['results'][0]['geometry']['bounds']['southwest']['lng'])
    #location
    location_lat=str(js['results'][0]['geometry']['location']['lat'])
    location_lng=str(js['results'][0]['geometry']['location']['lng'])
    #types
    types=str(js['results'][0]['types'][0]+" , "+js['results'][0]['types'][1])

    if count ==0:
        stateEntry.delete(0,END)
        countryEntry.delete(0,END)
        bounds_latitudeEntry_NE.delete(0,END)
        bounds_latitudeEntry_SW.delete(0,END)
        bounds_longitudeEntry_NE.delete(0,END)
        bounds_longitudeEntry_SW.delete(0,END)
        locationEntry_lat.delete(0,END)
        locationEntry_lng.delete(0,END)
        typesEntry.delete(0,END)

    stateEntry.insert(0,state)
    countryEntry.insert(0,country)
    bounds_latitudeEntry_NE.insert(0,'NE: '+bounds_NE_lat)
    bounds_latitudeEntry_SW.insert(0,'SW: '+bounds_SW_lat)
    bounds_longitudeEntry_NE.insert(0,'NE: '+bounds_NE_lng)
    bounds_longitudeEntry_SW.insert(0,'SW: '+bounds_SW_lng)
    locationEntry_lat.insert(0,'Latitude: '+location_lat)
    locationEntry_lng.insert(0,'Longitude '+location_lng)
    typesEntry.insert(0,types)

submitbutton = Button(root,text="Submit",command=xyz,border=2,font=("poor richard",18),bg="lightsteelblue")
submitbutton.grid(row=0,column=1)

state = Label(root,text="State :",bg="lightblue",font=('poor richard', 18,'bold'))
stateEntry = Entry(root,text=state,width=30,bg="lightsteelblue",border=4)
country = Label(root,text='Country :',bg="lightblue",font=('poor richard', 18,'bold'))
countryEntry = Entry(root,text=country,width=30,bg="lightsteelblue",border=4)
bounds_latitude = Label(root,text='Bounds latitude: ',bg="lightblue",font=('poor richard', 18,'bold'))
bounds_latitudeEntry_NE = Entry(root,text="",width=30,bg="lightsteelblue",border=4)
bounds_latitudeEntry_SW = Entry(root,text="",width=30,bg="lightsteelblue",border=4)
bounds_longitude = Label(root,text='Bounds longitude :',bg="lightblue",font=('poor richard', 18,'bold'))
bounds_longitudeEntry_NE = Entry(root,text="",width=30,bg="lightsteelblue",border=4)
bounds_longitudeEntry_SW = Entry(root,text="",width=30,bg="lightsteelblue",border=4)
location = Label(root,text='Location :',bg="lightblue",font=('poor richard', 18,'bold'))
locationEntry_lat = Entry(root,text="",width=30,bg="lightsteelblue",border=4)
locationEntry_lng = Entry(root,text="",width=30,bg="lightsteelblue",border=4)
types = Label(root,text='Types:',bg="lightblue",font=('poor richard', 18,'bold'))
typesEntry= Entry(root,text="",width=30,bg="lightsteelblue",border=4)

e.grid(row=0,column=0,padx=40,pady=30)
state.grid(row=1,column=0,padx=20,pady=10)
stateEntry.grid(row=1,column=1,padx=20,pady=10)
country.grid(row=2,column=0,padx=20,pady=10)
countryEntry.grid(row=2,column=1,padx=20,pady=10)
bounds_latitude.grid(row=3,column=0,padx=20,pady=10)
bounds_latitudeEntry_NE.grid(row=3,column=1,padx=20,pady=10)
bounds_latitudeEntry_SW.grid(row=4,column=1,padx=20,pady=10)
bounds_longitudeEntry_NE.grid(row=3,column=2,padx=20,pady=10)
bounds_longitudeEntry_SW.grid(row=4,column=2,padx=20,pady=10)
location.grid(row=5,column=0,padx=20,pady=10)
locationEntry_lat.grid(row=5,column=1,padx=20,pady=10)
locationEntry_lng.grid(row=5,column=2,padx=20,pady=20)
types.grid(row=6,column=0,padx=20,pady=10)
typesEntry.grid(row=6,column=1,padx=20,pady=10)
#building the elements

# putting elemnts in the frame




root.mainloop()
