import time
import random
class Tournament:
    def battle(self,c1,c2):
        print(c1.name + ':', c1.HP)
        for i in range(4):
            print(c1.enhancement[i])
        print(c2.name, ':', c2.HP)
        for i in range(4):
            print(c2.enhancement[i])
        time.sleep(8)
        while c1.HP > 0 and c2.HP > 0:
            selection = c1.enhancement[random.randint(0, 3)]
            accuracy = random.randint(1, 20)
            print(c1.name,'used', selection['name'])

            time.sleep(0.75)

            rng = random.randint(1, 4)

            if rng == 1 and c1.status == 'PAR':
                print(c1.name, 'is paralysed and unable to move')

            elif selection['TYPE'] == 'recovery':              
                if c1.HP >= c1.MAX_HP:
                    print('But it failed!')
                else:
                    c1.HP += selection['power']
                    if c1.HP > c1.MAX_HP:
                        c1.HP = c1.MAX_HP
                    print(c1.name +':', str(c1.HP )+ '/' + str(c1.MAX_HP))

            elif accuracy > selection['accuracy']:
                print('The attack missed!')
            elif selection['TYPE'] == 'damage':
                critical = random.randint(1, 12)
                if critical == 12:
                    c2.HP -= selection['power']
                    print('A critical hit!')
                    time.sleep(0.25)
                c2.HP -= selection['power']
                print(c2.name +':', str(c2.HP) + '/' + str(c2.MAX_HP))
                if selection['effect'] == 'burn':
                    rng = random.randint(1, 6)
                    if rng == 3:
                        print(c2.name, 'is burned!')
                        c2.status = 'burn'
                if selection['effect'] == 'PAR':
                    rng = random.randint(1, 6)
                    if rng == 3:
                        print(c2.name, 'is paralysed!')
                        c2.status = 'PAR'
            
            if c1.status == 'burn':
                c1.HP -= 3
                print(c1.name, 'was hurt by burn')
                print(c1.name +':', str(c1.HP )+ '/' + str(c1.MAX_HP))
            time.sleep(0.75)
            

            
            selection = c2.enhancement[random.randint(0, 3)]
            accuracy = random.randint(1, 20)
            print(c2.name,'used', selection['name'])

            time.sleep(0.75)
            rng = random.randint(1, 4)

            if rng == 1 and c2.status == 'PAR':
                print(c2.name, 'is paralysed and unable to move')


            elif selection['TYPE'] == 'recovery':
                if c2.HP >= c2.MAX_HP:
                    print('But it failed!')
                else:
                    c2.HP += selection['power']
                    if c2.HP > c2.MAX_HP:
                        c2.HP = c2.MAX_HP
                    print(c2.name +':', str(c2.HP) + '/' + str(c2.MAX_HP))

            elif accuracy > selection['accuracy']:
                print('The attack missed!')
            elif selection['TYPE'] == 'damage':
                critical = random.randint(1, 12)
                if critical == 12:
                    c1.HP -= selection['power']
                    print('A critical hit!')
                    time.sleep(0.25)
                c1.HP -= selection['power']
                print(c1.name +':', str(c1.HP )+ '/' + str(c1.MAX_HP))
                if selection['effect'] == 'burn':
                    rng = random.randint(1, 6)
                    if rng == 1:
                        print(c1.name, 'is burned!')
                        c1.status = 'burn'
                if selection['effect'] == 'PAR':
                    rng = random.randint(1, 6)
                    if rng == 3:
                        print(c1.name, 'is paralysed!')
                        c1.status = 'PAR'
            if c2.status == 'burn':
                time.sleep(0.5)
                c2.HP -= 3
                print(c2.name, 'was hurt by burn')
                print(c2.name +':', str(c2.HP )+ '/' + str(c2.MAX_HP))
            
            time.sleep(0.75)
        
        if c1.HP > c2.HP:
            print(c1.name, 'wins!')
            c1.HP = c1.MAX_HP
            c1.status = None
            return 1
        else:
            print(c2.name, 'wins!')
            c2.HP = c2.MAX_HP
            c2.status = None
            return 2
        

    def Tbattle(self,c1,c2):
        while c1.HP > 0 and c2.HP > 0:
            selection = c1.enhancement[random.randint(0, 3)]
            accuracy = random.randint(1, 20)
            

            

            rng = random.randint(1, 4)

            if rng == 1 and c1.status == 'PAR':
                pass

            elif selection['TYPE'] == 'recovery':              
                if c1.HP >= c1.MAX_HP:
                    pass
                else:
                    c1.HP += selection['power']
                    if c1.HP > c1.MAX_HP:
                        c1.HP = c1.MAX_HP
                    

            elif accuracy > selection['accuracy']:
                pass
            elif selection['TYPE'] == 'damage':
                critical = random.randint(1, 12)
                if critical == 12:
                    c2.HP -= selection['power']
                    
                    
                c2.HP -= selection['power']
                
                if selection['effect'] == 'burn':
                    rng = random.randint(1, 6)
                    if rng == 3:
                        
                        c2.status = 'burn'
                if selection['effect'] == 'PAR':
                    rng = random.randint(1, 6)
                    if rng == 3:
                        
                        c2.status = 'PAR'
            
            if c1.status == 'burn':
                c1.HP -= 3
                
            

            
            selection = c2.enhancement[random.randint(0, 3)]
            accuracy = random.randint(1, 20)
            

            
            rng = random.randint(1, 4)

            if rng == 1 and c2.status == 'PAR':
                pass


            elif selection['TYPE'] == 'recovery':
                if c2.HP >= c2.MAX_HP:
                    pass
                else:
                    c2.HP += selection['power']
                    if c2.HP > c2.MAX_HP:
                        c2.HP = c2.MAX_HP
                    

            elif accuracy > selection['accuracy']:
                pass
            elif selection['TYPE'] == 'damage':
                critical = random.randint(1, 12)
                if critical == 12:
                    c1.HP -= selection['power']
                    
                    
                c1.HP -= selection['power']
                
                if selection['effect'] == 'burn':
                    rng = random.randint(1, 6)
                    if rng == 1:
                        
                        c1.status = 'burn'
                if selection['effect'] == 'PAR':
                    rng = random.randint(1, 6)
                    if rng == 3:
                        
                        c1.status = 'PAR'
            if c2.status == 'burn':
                
                c2.HP -= 3
                
        
        if c1.HP > c2.HP:
            
            c1.HP = c1.MAX_HP
            c1.status = None
            return 1
        else:
            
            c2.HP = c2.MAX_HP
            c2.status = None
            return 2

