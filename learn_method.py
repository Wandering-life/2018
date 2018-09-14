#方法
#普通方法、静态方法和类方法。
#普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；
#类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；
#静态方法：由类调用；无默认参数；
class person:
      #定义普通方法
      def hello(self):
          print('普通方法')

      #定义类方法
      @classmethod
      def haha(cls):
          print('类方法')

      #定义静态方法
      @staticmethod
      def hehe():
          print('静态方法')

weng = person()
weng.hello() #调用普通方法
person.haha() #调用类方法
person.hehe() #调用静态方法

#https://www.cnblogs.com/yunguoxiaoqiao/p/7625722.html
