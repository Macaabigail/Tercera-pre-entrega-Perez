from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from App.models import Conductor
from users.utilities.utility import return_today, return_month, return_year 
from datetime import datetime as dt



class TestUtilities(TestCase):

    
    def test_day(self):


        hoy = dt.now()

 
        self.assertEqual(hoy.day , return_today() )
    
    def test_return_year(self):
       
        hoy = dt.now()  
        self.assertEqual(return_year(), hoy.year)

class EliminarConductorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.conductor = Conductor.objects.create(
            nombre="Juan",
            apellido="Perez",
            
        )
        self.url = reverse("Delete", args=[self.conductor.id])

    def test_eliminar_conductor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "App/conductor_confirm_delete.html")
        self.client.post(self.url)
        self.assertQuerysetEqual(Conductor.objects.all(), [])
