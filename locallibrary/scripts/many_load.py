import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import State, Category, Iso, Site, Region

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    State.objects.all().delete()
    Category.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()
    Region.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None
        try:
            lo = int(row[4])
        except:
            lo = None
        try:
            la = int(row[5])
        except:
            la = None
        try:
            a = int(row[6])
        except:
            a = None


        site = Site(name=row[0],description=row[1],justification=row[2],year=y,longitude=lo,latitude=la,area_hectares=a,category=c,state=s,region=r,iso=i)
        site.save()



