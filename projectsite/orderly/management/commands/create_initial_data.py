# cardquest/management/commands/create_initial_data.py

from django.core.management.base import BaseCommand
from orderly.models import Category, Product, Review, Order, Customer

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating initial data...'))
        self.create_categories()
        self.create_products()
        self.create_reviews()
        self.create_orders()
        self.create_customers()

        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))

    def create_categories(self):
        Category.objects.create(name='Electronics')
        Category.objects.create(name='Clothing')
        Category.objects.create(name='Home and Furniture')

    def create_products(self):
        category1 = Category.objects.get(name='Electronics')
        category2 = Category.objects.get(name='Clothing')
        category3 = Category.objects.get(name='Home and Furniture')

        Product.objects.create(
            name='Laptop',
            description='A powerful laptop',
            category=category1,
            price=999.99,
            image='https://i.pinimg.com/564x/d7/f8/90/d7f8906c6347bd39718bf940d8475bb4.jpg'
        )
        Product.objects.create(
            name='T-shirt',
            description='A comfortable T-shirt',
            category=category2,
            price=19.99,
            image='https://i.pinimg.com/564x/f6/94/3f/f6943f7a1bf1ee3d383da61defe74341.jpg'
        )
        Product.objects.create(
            name='Sofa',
            description='A cozy sofa',
            category=category3,
            price=499.99,
            image='https://i.pinimg.com/564x/ba/4f/9b/ba4f9be752a700094d4d155134ec86ec.jpg'
        )

    def create_reviews(self):
        product1 = Product.objects.get(name='Laptop')
        product2 = Product.objects.get(name='T-shirt')
        product3 = Product.objects.get(name='Sofa')

        Review.objects.create(product=product1, author='John Doe', text='Great laptop!', rating=5)
        Review.objects.create(product=product2, author='Jane Smith', text='Comfortable T-shirt.', rating=4)
        Review.objects.create(product=product3, author='Alice Johnson', text='Love this sofa!', rating=5)

    def create_orders(self):
        product1 = Product.objects.get(name='Laptop')
        product2 = Product.objects.get(name='T-shirt')
        product3 = Product.objects.get(name='Sofa')

        order = Order.objects.create(date_ordered='2023-01-01', total_amount=1519.97)
        order.products.add(product1, product2, product3)

    def create_customers(self):
        Customer.objects.create(name='John Doe', email='john@example.com')
        Customer.objects.create(name='Jane Smith', email='jane@example.com')
        Customer.objects.create(name='Alice Johnson', email='alice@example.com')
