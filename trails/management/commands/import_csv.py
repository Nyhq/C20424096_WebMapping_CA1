from django.core.management.base import BaseCommand
from django.contrib.gis.geos import LineString
from trails.models import Trail
import csv


class Command(BaseCommand):
    help = 'Import trails from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_filepath', type=str, help='The CSV file path')

    def handle(self, *args, **options):
        csv_filepath = options['csv_filepath']

        with open(csv_filepath, 'r') as file:
            reader = csv.DictReader(file)
            trail_coords = []
            for row in reader:
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
                trail_coords.append((longitude, latitude))  # Longitude first, then latitude

            # Ensure the trail forms a loop
            if trail_coords[0] != trail_coords[-1]:
                trail_coords.append(trail_coords[0])

            trail_linestring = LineString(trail_coords)
            trail = Trail.objects.create(
                name="Glen of the Downs Loop",
                description="Description here",
                difficulty="Medium",
                path=trail_linestring
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully imported trail "{trail.name}"'))
