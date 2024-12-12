# Django-
19 module dz


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
