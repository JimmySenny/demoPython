"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""

from abc import  ABCMeta, abstractmethod

class Employee( metaclass = ABCMeta ):
    # 员工抽象类
    def __init__(self, name):
        self._name = name;

    @property
    def name(self):
        return self._name;

    @abstractmethod
    def get_salary(self):
        # 结算月薪（抽象方法）
        pass;

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name);

    def get_salary(self):
        return 15000.00;

class Programmer(Employee):
    def __init__(self, name, working_hour = 0):
        self._working_hour = working_hour;
        super().__init__(name);

    def get_salary(self):
        return 200.00 * self._working_hour;

class Salesman(Employee):

    def __init__(self, name, sales = 0.0 ):
        self._sales = sales;
        super().__init__(name);

    def get_salary(self):
        return 1800.00 + self._sales * 0.05;

class EmployeeFactory():
    """
    员工的工厂
    """
    def create(emp_type, *args, **kwargs):
        _emp_type = emp_type.upper();
        _emp = None;

        if ( _emp_type == 'M' ):
            emp = Manager(*args, **kwargs);
        elif ( _emp_type == 'P' ):
            emp = Programmer(*args, **kwargs);
        elif ( _emp_type == 'S' ):
            emp = Salesman(*args, **kwargs);

        return emp;

def main():
    emps = [
            EmployeeFactory.create('M', '张三' ),
            EmployeeFactory.create('P', '李四', 120 ),
            EmployeeFactory.create('P', '王五', 85 ),
            EmployeeFactory.create('S', '小黑', 123000 ), ];
    for emp in emps:
        print('%s:%.2f' % (emp.name, emp.get_salary()));

if __name__ == '__main__':
    main();


