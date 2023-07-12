from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.

class Car(models.Model):
    
    def __str__(self):
        return self.car_title
    
    car_title = models.CharField(max_length=255)
    province_choice = (
        ("PH-ABR", "Abra"),
        ("PH-AGN", "Agusan del Norte[i]"),
        ("PH-AGS", "Agusan del Sur"),
        ("PH-AKL", "Aklan"),
        ("PH-ALB", "Albay"),
        ("PH-ANT", "Antique"),
        ("PH-APA", "Apayao"),
        ("PH-AUR", "Aurora"),
        ("PH-BAS", "Basilan[iv]"),
        ("PH-BAN", "Bataan"),
        ("PH-BTN", "Batanes"),
        ("PH-BTG", "Batangas"),
        ("PH-BEN", "Benguet[vi]"),
        ("PH-BIL", "Biliran"),
        ("PH-BOH", "Bohol"),
        ("PH-BUK", "Bukidnon"),
        ("PH-BUL", "Bulacan"),
        ("PH-CAG", "Cagayan"),
        ("PH-CAN", "Camarines Norte"),
        ("PH-CAS", "Camarines Sur[vii]"),
        ("PH-CAM", "Camiguin"),
        ("PH-CAP", "Capiz"),
        ("PH-CAT", "Catanduanes"),
        ("PH-CAV", "Cavite"),
        ("PH-CEB", "Cebu[viii]"),
        ("PH-NCO", "Cotabato"),
        ("PH-COM", "Davao de Oro"),
        ("PH-DAV", "Davao del Norte"),
        ("PH-DAS", "Davao del Sur[ix]"),
        ("PH-DVO", "Davao Occidental"),
        ("PH-DAO", "Davao Oriental"),
        ("PH-DIN", "Dinagat Islands"),
        ("PH-EAS", "Eastern Samar"),
        ("PH-GUI", "Guimaras"),
        ("PH-IFU", "Ifugao"),
        ("PH-ILN", "Ilocos Norte"),
        ("PH-ILS", "Ilocos Sur"),
        ("PH-ILI", "Iloilo[x]"),
        ("PH-ISA", "Isabela[xi]"),
        ("PH-KAL", "Kalinga"),
        ("PH-LUN", "La Union"),
        ("PH-LAG", "Laguna"),
        ("PH-LAN", "Lanao del Norte[xii]"),
        ("PH-LAS", "Lanao del Sur"),
        ("PH-LEY", "Leyte[xiii]"),
        ("PH-MDN", "Maguindanao del Norte[xiv]"),
        ("PH-MDS", "Maguindanao del Sur"),
        ("PH-MAD", "Marinduque"),
        ("PH-MAS", "Masbate"),
        ("PH-MSC", "Misamis Occidental"),
        ("PH-MSR", "Misamis Oriental[xv]"),
        ("PH-MOU", "Mountain Province"),
        ("PH-NEC", "Negros Occidental[xvi]"),
        ("PH-NER", "Negros Oriental"),
        ("PH-NSA", "Northern Samar"),
        ("PH-NUE", "Nueva Ecija"),
        ("PH-NUV", "Nueva Vizcaya"),
        ("PH-MDC", "Occidental Mindoro"),
        ("PH-MDR", "Oriental Mindoro"),
        ("PH-PLW", "Palawan[xviii]"),
        ("PH-PAM", "Pampanga[xix]"),
        ("PH-PAN", "Pangasinan[xx]"),
        ("PH-QUE", "Quezon[xxi]"),
        ("PH-QUI", "Quirino"),
        ("PH-RIZ", "Rizal"),
        ("PH-ROM", "Romblon"),
        ("PH-WSA", "Samar"),
        ("PH-SAR", "Sarangani"),
        ("PH-SIG", "Siquijor"),
        ("PH-SOR", "Sorsogon"),
        ("PH-SCO", "South Cotabato[xxii]"),
        ("PH-SLE", "Southern Leyte"),
        ("PH-SUK", "Sultan Kudarat"),
        ("PH-SLU", "Sulu"),
        ("PH-SUN", "Surigao del Norte"),
        ("PH-SUR", "Surigao del Sur"),
        ("PH-TAR", "Tarlac"),
        ("PH-TAW", "Tawi-Tawi"),
        ("PH-ZMB", "Zambales[xxiii]"),
        ("PH-ZAN", "Zamboanga del Norte"),
        ("PH-ZAS", "Zamboanga del Sur[xxiv]"),
        ("PH-ZSI", "Zamboanga Sibugay"),
        ("PH-00", "Metro Manila"),

        
        
    )
    
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))
        
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    ) 
    
    door_choices = (
       ('2', '2'),
       ('3', '3'),
       ('4', '4'),
       ('5', '5'),
       ('6', '6'),
   )
    
    car_title = models.CharField(max_length=255)
    province = models.CharField(choices=province_choice, max_length=100)
    city =  models.CharField(max_length=100)
    color =  models.CharField(max_length=100)
    model =  models.CharField(max_length=100)    
    year =  models.IntegerField(('year'), choices=year_choice)
    condition =  models.CharField(max_length=100)
    price =  models.IntegerField()
    description =  RichTextField()
    car_photo = models.ImageField(upload_to='photos/%m/%d/%Y/')
    car_photo1 = models.ImageField(upload_to='photos/%m/%d/%Y/', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%m/%d/%Y/', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%m/%d/%Y/', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%m/%d/%Y/', blank=True)
    features =  MultiSelectField(choices=features_choices, max_choices=len(features_choices), max_length=250)
    body_style =  models.CharField(max_length=100)
    engine =  models.CharField(max_length=100)
    transmission =  models.CharField(max_length=100)
    interior =  models.CharField(max_length=100)
    miles =  models.IntegerField()
    doors =  models.CharField(choices=door_choices, max_length=10)
    passengers =  models.IntegerField()
    vim_no =  models.CharField(max_length=100)
    milage =  models.IntegerField()
    fuel_type =  models.CharField(max_length=50)
    no_of_owners =  models.CharField(max_length=100)
    is_featured =  models.BooleanField(default=False)
    created_date =  models.DateTimeField(default=datetime.now, blank=True)
    
