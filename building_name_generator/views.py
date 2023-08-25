import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from building_name_generator.models import Chowk, District, Municipality, Province, Road, Wardnumber
from .forms import GenerateHashForm
# Create your views here.


def index(request):
    if (request.method == 'POST'):
        form = GenerateHashForm(request.POST)
        print(form.data['province'])
        provinceCode = Province.objects.get(pk=form.data['province']).code
        districtCode = District.objects.get(pk=form.data['district']).code
        municipalityCode = Municipality.objects.get(
            pk=form.data['municipality']).code
        wardNumberCode = Wardnumber.objects.get(
            pk=form.data['wardnumber']).code
        roadCode = Road.objects.get(pk=form.data['road']).roadnumber
        chowkCode = Chowk.objects.get(pk=form.data['chowk']).code
        direction = form.data['direction']
        # calcualte midpoint
        midpoint = (int(form.data['start_distance']) +
                    int(form.data['end_distance'])) / 2
        midpoint = int(midpoint)
        if (form.data['side'] == 'R'):
            if (midpoint % 2 == 0):
                locationnumber = midpoint
            else:
                locationnumber = midpoint + 1
        else:
            if (midpoint % 2 != 0):
                locationnumber = midpoint
            else:
                locationnumber = midpoint + 1
        print(locationnumber)
        hashCode = f"{provinceCode}{districtCode}{municipalityCode}{wardNumberCode}{roadCode}{chowkCode}{direction}{locationnumber}"
        shortHashCode = f"{roadCode}{chowkCode}{direction}{locationnumber}"
        return render(request, "building_name_generator/generated-hash.html", {"hash": hashCode, "short_hash": shortHashCode, "details": {

        }})
    else:
        form = GenerateHashForm()
    return render(request, "building_name_generator/index.html", {"form": form})


def generateHash(request):
    return render(request, "building_name_generator/generated-hash.html", {"hash": "LuRdBu02EChaE36", "short_hash": "EChaE36"})


def view_map(request):
    mycoordinates = [
        {"name": "LuRuBu07KmcE199", "lat": 27.694401487589776, "lon": 83.47254691586639},
        {"name": "LuRuBu07BpcE370", "lat": 27.693595129709916, "lon": 83.47294560225534},
        {"name": "LuRuBu07MpcE79", "lat": 27.69407448603197, "lon": 83.47192580442817},
        {"name": "LuRuBu07MpcE149", "lat": 27.69356995428179, "lon": 83.47102311860016},
    ]
    coordinates_json = json.dumps(mycoordinates)
    return render(request, "building_name_generator/map.html", {'coordinates': coordinates_json})

# //getting data


def get_districts(request):
    province_id = request.GET.get('province_id')
    districts = District.objects.filter(province_id=province_id)
    data = [{'id': district.id, 'name': district.name}
            for district in districts]
    return JsonResponse({'districts': data})


def get_municipalites(request):
    district_id = request.GET.get('district_id')
    municipalities = Municipality.objects.filter(district_id=district_id)
    data = [{'id': municipality.id, 'name': municipality.name}
            for municipality in municipalities]
    return JsonResponse({'municipalities': data})
