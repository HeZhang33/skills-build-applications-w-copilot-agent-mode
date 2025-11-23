from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(email='a@b.com', name='A', team=team, is_superhero=True)
        self.assertEqual(str(user), 'a@b.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(email='b@b.com', name='B', team=team, is_superhero=False)
        activity = Activity.objects.create(user=user, type='Run', duration=10, date='2025-01-01')
        self.assertEqual(str(activity), 'B - Run')

    def test_workout_creation(self):
        team = Team.objects.create(name='T3', description='d3')
        workout = Workout.objects.create(name='W', description='desc')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'W')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='T4', description='d4')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(str(leaderboard), 'T4 - 50 pts')
