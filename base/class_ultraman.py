"""
奥特曼打小怪兽
"""

from abc import ABCMeta, abstractmethod
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):
    __slot__ = ('_name', '_hp');
    def __init__(self,name,hp):
        self._name = name;
        self._hp = hp;

    @property
    def name(self):
        return self._name;

    @property
    def hp(self):
        return self._hp;

    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp > 0 else 0;

    @property
    def alive(self):
        """
        if(self._hp>0):
            return True;
        else:
            return False;
        """
        return self._hp > 0;

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slot__ = ('_name','_hp','_mp');

    def __init__(self,name,hp,mp):
        super().__init__(name,hp);
        self._mp = mp;

    def attack(self,other):
        other.hp -= randint(15,25);

    #会心一击 究极必杀技(打掉对方至少50点或四分之三的血)
    def huge_attack(self, other):
        if(self._mp >= 50 ):
            self._mp -= 50;
            injury = other.hp * 3//4;
            injury = injury if injury >= 50 else 50;
            other.hp -= injury;
            return True;
        else:
            self.attack(other);
            return False;

    def magic_attack(self, others):
        if(self._mp >= 20):
            self._mp -= 20;
            for tmp in others:
                if tmp.alive>0:  # ??? alive 是方法，怎么不能加()
                    tmp.hp -= randint(10,20);
            return True;
        else:
                return False;

    #魔法恢复
    def resume(self):
        incr_point = randint(1,10);
        self._mp += incr_point;
        return incr_point;

    def __str__(self):
        return '奥特曼-%s\n'% self._name + '生命值[%d]\t魔法值[%d]\n'%(self._hp, self._mp);

class Monster(Fighter):
    __slot__ = ('_name', '_hp');

    def attack(self, other):
        other.hp -= randint(5, 15);

    def __str__(self):
        return '小怪兽-%s\n'% self._name + '生命值[%d]\n' % self._hp;


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive>0:
            return True;
    return False;

def select_alive_one(monsters):
    monsters_len = len(monsters);
    while True:
        index = randrange(monsters_len);
        monster = monsters[index];
        if (monster.alive>0 ):
            return monster;


def display_info(ultraman, monsters):
    print(ultraman);
    for monster in monsters:
        print(monster, end='\t');

def main():
    u = Ultraman('奥特曼X',100,100);
    m1 = Monster('小怪兽1', 100);
    m2 = Monster('小怪兽2', 100);
    m3 = Monster('小怪兽3', 100);

    ms = [m1, m2, m3];

    print("====战斗开始====");

    fight_round = 1;
    while u.alive>0 and is_any_alive(ms):
        print('=====第%04d回合====' % fight_round);
        m = select_alive_one(ms);
        skill = randint(1, 19);
        if (skill <= 6): #60% 普通攻击
            print('%s attack %s'% (u.name, m.name ));
            u.attack(m);
            print('魔法值恢复了[%d]' % u.resume() );
        elif ( skill <= 9 ): #30% 魔法攻击
            if(u.magic_attack(ms)):
                print('%s magic_attack' % u.name );
            else:
                print('魔法值不足');
                print('%s huge_attack %s' % (u.name, m.name));
                u.resume();
        else: #10% 会心一击
            if (u.huge_attack(m)):
                print('%s huge_attack %s' % (u.name, m.name));
            else:
                print('%s attack %s' % (u.name, m.name));
                print('魔法值恢复了[%d]' % u.resume() );
        if (m.alive>0 ):
            print('%s re attack %s' %(m.name, u.name));
            m.attack(u);
        display_info(u,ms);
        fight_round += 1;
    print('====战斗结束,共[%d]回合====' % (fight_round-1));
    if (u.alive>0 ):
        print('奥特曼胜利');
    else:
        print('小怪兽胜利');

if __name__ == '__main__':
    main();




