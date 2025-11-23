from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel, is_superhero=True),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc, is_superhero=True),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc, is_superhero=True),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=users[0], type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=date.today())

        self.stdout.write('Creating workouts...')
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flyers')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        self.stdout.write('Creating leaderboards...')
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
