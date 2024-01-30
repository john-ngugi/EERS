from django.shortcuts import render #Used to render HTML templates and return them as HTTP responses.
import json 
from django.http import JsonResponse
from .models import *
import indexmeter
from indexmeter.models import Emergencies
import modules
from modules import indeces,allocation
from colorama import init, Fore
from django.core.paginator import Paginator
import statistics
import folium 
import requests
# from . import modules 
# from modules import allocation

# Create your views here.



def allocator(emergency,index):
    fire_resources = FireResources.objects.filter().first()
    police_resources = PoliceResources.objects.filter().first()
    medical_resources = MedicalResourses.objects.filter().first()
    
    if emergency == 'Fire':
        allocation_resource = fire_resources.fire
        
    if emergency == 'Crime':
        allocation_resource = police_resources.police

    if emergency == 'Medical':
         allocation_resource = medical_resources.medical

    resource_allocated = allocation.Allocation(emergency,allocation_resource,index)

    resource_allocated=resource_allocated.allocator()

    if emergency == 'Fire':
        fire_resources.fire =  resource_allocated
        resource =  fire_resources    
        
    if emergency == 'Crime':
        police_resources.police =  resource_allocated
        resource =  police_resources    

    if emergency == 'Medical':
        medical_resources.medical =  resource_allocated  
        resource =  medical_resources          

    return resource.save()



# Initialize colorama
init(autoreset=True)

# View function for the index page
def index(request):
    fire_resources = FireResources.objects.filter().first()
    police_resources = PoliceResources.objects.filter().first()
    medical_resources = MedicalResourses.objects.filter().first()

    context={
        'fire': fire_resources.fire,
        'medical': medical_resources.medical,
        'crime':police_resources.police
    }    
    # Render the "home_main_content.html" template and return it as an HTTP response
    return render(request,"home/home_main_content.html",context)
# View function for the emergencies page
def emergencies(request):
    emergencies = Emergencies.objects.filter(user=request.user).values_list()
    paginator = Paginator(emergencies,2)
    page_number =  request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(emergencies)
    emergency_list = list(emergencies)

    print(" emergency list is : \n",emergency_list)
    #   user = request.POST.get('User')
    # emergencies = Emergencies.objects.filter(user= request.user).all()
    print(list(emergencies))
    print(f"{Fore.YELLOW}emergency list length is:", len(emergency_list) )

    total_fire = 0
    total_medical = 0
    total_crime = 0
 
    
    for x in range(len(emergency_list)):
        try:
           fire_index = emergency_list[x].index('Fire')
           if fire_index:
            total_fire+=1
            print(total_fire)
        except:
            print('could not find fire') 

    for x in range(len(emergency_list)):
        try:
           medical_index = emergency_list[x].index('Medical')
           if medical_index:
            total_medical+=1
            print(total_medical)
        except:
            print('could not find medical') 

    for x in range(len(emergency_list)):
        try:
           crime_index = emergency_list[x].index('Crime')
           if crime_index:
            total_crime+=1
            print(total_crime)
        except:
            print('could not find crime') 
    
    def getMode(type,index):
        list_values_for_location = []
        for obj in emergency_list:
            obj_of_interest = obj[index]
            list_values_for_location.append(obj_of_interest)
        print(f"{Fore.BLUE}list of {type} is : {list_values_for_location}") 

        mode = statistics.mode(list_values_for_location)
        print(f"{Fore.GREEN}mode of {type} is: {mode}")
        return mode

    mode_locations = getMode('location',2)
    mode_emergency = getMode('energency',3)
    

    context = {
        'emergency_list':list(emergencies),
        'total_fire':total_fire,
        'total_crime':total_crime,
        'total_medical':total_medical,
        'page_obj':page_obj,
        'mode_locations' : mode_locations,
        'mode_emergency' : mode_emergency,
    }

    


    # Render the "emergencies.html" template and return it as an HTTP response
    return render(request,"home/emergencies.html",context)

def ongoingEmergencies(request):
    # Render the "emergencies.html" template and return it as an HTTP response
    return render(request,"home/ongoing_summary.html")

def dataRetriever(request):
    if request.method == 'POST':
      
       data = json.loads(request.body).get('data')
       x_coords =json.loads(request.body).get('coordinates_x')
       y_coords =json.loads(request.body).get('coordinates_y')
       name =json.loads(request.body).get('name')
       print(x_coords,y_coords,name)
       type = json.loads(request.body).get('type')
       casualty_no = json.loads(request.body).get('casualty_no')
       spread_radius = json.loads(request.body).get('spread_radius')
       specific_res = json.loads(request.body).get('specific_res')
       print(spread_radius)
       print(x_coords,y_coords,name)

       index_obj = indeces.Index(casualty_no=casualty_no,spread=spread_radius,specific_res=specific_res)
       index = index_obj.indexer()
       print(index)
       def save_emergencies_to_database(user,x_coords, y_coords,name,type,index):
            if x_coords is not None and y_coords is not None and name is not None and index is not None:
                # Create a new Coordinates instance
                new_emergency = Emergencies()
                new_emergency.user = user
                new_emergency.lat = x_coords
                new_emergency.lon = y_coords
                new_emergency.location = name 
                new_emergency.emergency = type 
                new_emergency.index = index
                allocator(type,index)
                new_emergency.responded_to = True
                # Save the new instance to the database
                new_emergency.save()
       def save_coordinates_to_database(x_coords, y_coords,name):
            if x_coords is not None and y_coords is not None:
                # Create a new Coordinates instance
                new_coordinates = Coordinates()
                new_coordinates.x_coordinate = x_coords
                new_coordinates.y_coordinate = y_coords
                new_coordinates.name = name 

                # Save the new instance to the database
                new_coordinates.save()

       save_coordinates_to_database(x_coords, y_coords,name)        
       save_emergencies_to_database(request.user,x_coords,y_coords,name,type,index)     

   

       return JsonResponse({'data':data},safe=False)
    return render(request,"collectorapp/collector.html")


def getEmergencyData(request):
    emergency = Emergencies.objects.all()
    emergency_list = list(emergency)
    print(emergency_list)


def getChartData(request):
    if request.method =="GET":
        emergencies = Emergencies.objects.filter(user=request.user).values_list()
        print(emergencies)
        emergency_list = list(emergencies)
        total_fire = 0
        total_medical = 0
        total_crime = 0

        
        for x in range(len(emergency_list)):
            try:
                fire_index = emergency_list[x].index('Fire')
                if fire_index:
                    total_fire+=1
                    print(total_fire)
            except:
                print('could not find fire') 

        for x in range(len(emergency_list)):
            try:
                medical_index = emergency_list[x].index('Medical')
                if medical_index:
                    total_medical+=1
                    print(total_medical)
            except:
                print('could not find medical') 

        for x in range(len(emergency_list)):
            try:
                crime_index = emergency_list[x].index('Crime')
                if crime_index:
                    total_crime+=1
                    print(total_crime)
            except:
                print('could not find crime') 
    
        return JsonResponse({'total_fire': total_fire,'total_crime':total_crime,'total_medical':total_medical}) 
    


def getEmergenciesForMarkers(request):
    emergency = Emergencies.objects.filter(user=request.user).values_list()
    emergency_list = list(emergency)
    locations_list =[]

    for emergency in emergency_list:
        locations_list.append([emergency[5],emergency[6],emergency[3]])
    
    print(f"{Fore.YELLOW} the coordinate list is: " ,locations_list)

    return JsonResponse({'coordinates': locations_list})    
        


def pathfinder(request):
    emergency = Emergencies.objects.filter(user=request.user).first()
    
    # emergency_location = [emergency.lat,emergency.lon]
    
    url = 'https://api.openrouteservice.org/v2/directions/driving-car'
    # api_key = '5b3ce3597851110001cf624821d7977ad17c4d3ab51df82a9d448a97'  
    start_coords = '36.8116,-1.3012'
    end_coords = f"{emergency.lon},{emergency.lat}"
 
 
    print(end_coords)
    headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }

    url = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248336a725ce6af473da9c418c23e073c72&start={start_coords},49.41461&end={end_coords}'
    print('url is : ', url)
    response = requests.get(f'https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248336a725ce6af473da9c418c23e073c72&start={start_coords}&end={end_coords}', headers=headers,)
    context = {}
    if response.status_code == 200:
        data = response.json()
        # print(data)
        feature = data['features'][0]
        coordinates = feature['geometry']['coordinates']

        point_list_converted = [(coord[1], coord[0]) for coord in coordinates]
        print(point_list_converted)
        # Create Folium map
        map_object = folium.Map(location=point_list_converted[0], zoom_start=15)
        folium.PolyLine(locations=point_list_converted, color='red', weight=3, smooth_factor=1).add_to(map_object)
        
        # Add custom markers for start and end coordinates
        folium.Marker(location=point_list_converted[0], popup='Start', icon=folium.Icon(color='red')).add_to(map_object)
        folium.Marker(location=point_list_converted[-1], popup='End', icon=folium.Icon(color='green')).add_to(map_object)
        # Convert the map to an HTML string
        map_html_string = map_object._repr_html_()  # This uses a private method, but it's commonly used for this purpose
        context['map'] = map_html_string
    else:
        print('Error:', response.status_code)

    return render(request, 'pathfinder/pathfinder.html', context)



    



