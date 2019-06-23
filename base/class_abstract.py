
from abc import ABCMeta, abstractmethod;
from random import randit,randrange;

class Fighter(Object, metaclass = ABCMeta):
    __slot__ = ('_name', '_hp');
    def __init__(self, name, hp):
        self._name = name;
        self._hp = hp;

    @property
    def name(self):
        return self._name;

    @property
    def hp(self):
        return self._hp;

    @hp.setter
    def hp(self, hp ):
        self._hp = hp;

    @property
    def alive(self):
        return self._hp > 0;

    @abstractmethod
    def attack(self, other ):
        pass

class Ultraman(Fighter):
    __slot__ = ('_name','_hp', '_mp' );

    def __init__(self, name, hp, mp):
        super().__init__(name, hp );
        self._mp = mp;

    def attack(self, other ):
        other.hp -= randint(15,25);
        
    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50;
            injury = other.hp * 3 // 4;
            injury = injury if injury >= 50 else 50;
            other.hp -= injury;
            return True;
        else:
            self.attack(other);
            return False;
    def magic_attack(self, other):
        """魔法攻击

        :param others: 被攻击的群体

        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

        
class Monster(Fighter):
    """小怪兽"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

