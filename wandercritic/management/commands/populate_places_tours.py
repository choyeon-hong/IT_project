from wandercritic.models import Place, Tour 
from django.core.management.base import BaseCommand

class Command(BaseCommand):
     #need to fill with data
    def handle (self, *args, **kwargs):
        places_data = [
            {
                'pname': 'Edinburgh Castle',
                'about': 'World Heritage Site in Edinburgh, Scotland',
                'picture': 'assets/Landscape/AdobeStock_168532350_Preview.jpeg',
                'geolocation':'55.9486° N, 3.1999° W',
                'seasons':'All year round',
                'activity': 'Sightseeing',
                'travel_theme':'Historical',
                'budget': 30,
                'description':'A mighty fortress, the defender of the nation and a world-famous visitor attraction – Edinburgh Castle has dominated the skyline for centuries.',
                'address': 'Castlehill, Edinburgh EH1 2NG, United Kingdom',
            },
            
        ]
        for place in places_data: 
            obj, created = Place.objects.update_or_create(
                pname=place['pname'],
                defaults=place
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Place {obj.pname} created")) 
            else:
                self.stdout.write(self.style.SUCCESS(f"Place {obj.pname} updated"))

        tours_data = [
            #need to fill with data
            {
                'tname': 'Edinburgh Castle Guided Tour',
                'place':  Place.objects.get(pname='Edinburgh Castle'),
                'information': 'Guided tour of Edinburgh Castle',
                'picture': 'assets/Landscape/AdobeStock_168532350_Preview.jpeg',
                'address': 'Castlehill, Edinburgh EH1 2NG, United Kingdom',
                'price': 25,
            }  
        ]

        for tour in tours_data:
            obj, created = Tour.objects.update_or_create(
                tname=tour['tname'],
                defaults=tour
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Tour {obj.tname} created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Tour {obj.tname} updated"))
