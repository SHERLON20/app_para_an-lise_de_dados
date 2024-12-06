import random 
from django.core.management.base import BaseCommand
from faker import Faker
from sales.models import sale

class Command(BaseCommand):
    help = 'popula o banco de dados com dados de vendas ficticios'
    
    def handle(self, *args, **kwargs):
        faker = Faker()
        products = [
            'produto A', 'produto B', 'produto C', 
            'produto D', 'produto E', 'produto F',
            'produto G','produto H', 'produto I','produto J'
         ]
        sales = []
         
        for _ in range(300):
            sala=sale(
                data = faker.date_this_year(),
                produto = random.choice(products),
                quantidade = random.randint(1,100),
                price = round(random.uniform(10.0,500.0),2)
                
            )
            sales.append(sala)
        sale.objects.bulk_create(sales)
        
        self.stdout.write(self.style.SUCCESS(
            'banco de dados foi populado com 300 vendas '
        ))