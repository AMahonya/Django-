# Django-
19 module dz

15,12,2024 
список использованных запросов Django ORM для тестирования базы данных.
>>> from task1.models import Game, Category, Order, Buyer
>>> category1 = Category.objects.create(category_name='RPG')
>>> category2 = Category.objects.create(category_name='Sandbox')
>>> category3 = Category.objects.create(category_name="Action")
>>> buyer1 = Buyer(name="Antonio", balance="1800", age="28")                     
>>> buyer2 = Buyer(name="Serhio", balance="0", age="15")     
>>> buyer3 = Buyer(name="Serejha", balance="120", age="35") 
>>> print(buyer1) 
Antonio
>>> buyer1.save()
>>> buyer2.save() 
>>> buyer3.save() 
>>> game1 = Game.objects.create(title='The Witcher 3', cost=('39.99'), size=('50.000'), description='крутая RPG', age_limited=True)        
>>> game2 = Game.objects.create(title='Minecraft', cost=('29.99'), size=('1.000'), description='Песочница', age_limited=False)               
>>> game3 = Game.objects.create(title="GTA 5", cost=('49.99'), size=('60.000'), description='Игра с открытым миром', age_limited=True)  
>>> game1.buyer.add(buyer1)
>>> game2.buyer.add(buyer2)
>>> game3.buyer.add(buyer1, buyer2)
>>> order1 = Order.objects.create(game=game1, quantity=1, order_date=('2024-05-26'), status='Отправлен') 
>>> order2 = Order.objects.create(game=game3, quantity=4, order_date=('2020-01-23'), status='в стадии оформления') 
>>> all_games = Game.objects.all()
>>> print("Все игры:", list(all_games))
Все игры: [<Game: The Witcher 3>, <Game: Minecraft>, <Game: GTA 5>]
>>> game_by_id = Game.objects.get(id=1)
>>> print("Игра с id 1:", game_by_id)
Игра с id 1: The Witcher 3
>>> adult_games = Game.objects.filter(age_limited=True)
>>> print("Игры с ограничением:", list(adult_games))
Игры с ограничением: [<Game: The Witcher 3>, <Game: GTA 5>]
>>> new_category = Category.objects.create(category_name='Strategy')
>>> print("category:", new_category)       
category: Strategy
>>> deleted_category_id = new_category.id
>>> new_category.delete()
(1, {'task1.Category': 1})
>>> total_orders = len(Order.objects.all())
>>> print("Общее кол-во заказов:", total_orders)
Общее кол-во заказов: 3
>>> total_adult_games = len(Game.objects.filter(age_limited=True))
>>> print(f"Кол-во игр для взрослых: {total_adult_games}")
Кол-во игр для взрослых: 2
>>> all_categories = Category.objects.all()
>>> print("Все категории:", list(all_categories))
Все категории: [<Category: RPG>, <Category: Sandbox>, <Category: Action>]
>>> all_orders = Order.objects.all()
>>> print("Все заказы:", list(all_orders))
Все заказы: [<Order: Order for The Witcher 3 x 1>, <Order: Order for The Witcher 3 x 1>, <Order: Order for GTA 5 x 4>]
>>>


13.12.2024 22:52
добавил в админку следующее:
GameAdmin - админ-класс модели Game:
Фильтрацию по полям size и cost.
Отображение полей title, cost и size при отображении всех полей списком.
Поиск по полю title.
Ограничение кол-ва записей до 20.
BuyerAdmin - админ-класс модели Buyer:
Фильтрацию по полям balance и age.
Отображение полей name, balance и age при отображении всех полей списком.
Поиск по полю name.
Ограничение кол-ва записей до 30.
Доступным только для чтения поле balance.

13.12.2024
Переделал 4 и 5 задание из 18 модуля, там у меня был сайт маникюрного салона, тут же я его переделал в интернет магазин + исправлена регистрация, теперь всё подкрепелно к базе данных 

12.12.2024
>>> from task1.models import Buyer   
>>> buy = Buyer.objects.all()
>>> print(buy) 
<QuerySet []>
>>> new_buyer = Buyer(name="Antonio", balance="1800", age="28") 
>>> new_buyer.save()                                           
>>> new_buyer = Buyer(name="Serhio", balance="800.34", age="8")  
>>> new_buyer.save()                                            
>>> new_buyer = Buyer(name="Alyosha", balance="42.45", age="58") 
>>> new_buyer.save()                                             
>>> from task1.models import Game                               
>>> game = Game.objects.all()                                    
>>> print(game) 
>>> new_game = Game(title="Dont Starve", cost="567.99", size="16.34", description="очень классная игра про выживание", age_limited="False") 
>>> new_game.save()                                                                                                                         
>>> new_game = Game(title="Terraria", cost="67.99", size="6.64", description="очень классная песочница", age_limited="True")           
>>> new_game.save()
>>> new_game = Game(title="Dota 2", cost="9.99", size="66.4", description="стратежка на любителя", age_limited="False")
>>> new_game.save()
>>> Game.objects.filter(title="Dota 2").update(age_limited="True")
1
 >>> buyer = Buyer.objects.get(id=1) 
>>> game = Game.objects.get(id=1)   
>>> game2 = Game.objects.get(id=2) 
>>> game3 = Game.objects.get(id=3) 
>>> buyer.games.add(game, game2, game3) 
>>> buyer2 = Buyer.objects.get(id=2)    
>>> buyer2.games.add(game)              
>>> buyer3 = Buyer.objects.get(id=3) 
>>> buyer3.games.add(game, game3)
