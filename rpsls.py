#coding:gbk
"""
程序目的：新编一程序， 完成RPSLS游戏
程序作者：植产5班黄石红
"""
import random  #0 - 石头，1 - 史波克，2 - 纸，3 - 蜥蜴，4 - 剪刀
def name_to_number(name):
    if name=="石头":
           name1=0
    elif name=="史波克":
           name1==1
    elif name=="纸":
           name1=2
    elif name=="蜥蜴":
           name1=3
    elif name=="剪刀":
           name1=4
    else:
        print("Error: No Correct Name") 
    return name1
def number_to_name(number):
    if number==0:
             number1="石头"
    elif number==1:
		       number1="史波克"
    elif number==2:
		       number1="纸"
    elif number==3:
		       number1="蜥蜴"
    elif number==4:
		       number1="剪刀"
    return number1  # 使用语句将不同的整数对应到游戏的不同对象
def rpsls(player_choice):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    print("你的选择为:",player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=str(number_to_name(comp_number))
    print("计算机的选择为：%s"%comp_choice)
    if player_choice_number==0:
       if comp_number==4:
          print("你赢了！")
       if comp_number==3:
          print("你赢了！")
       elif player_choice_number==comp_number:
          print("你和计算机出的一样呢")
       else:
          print("机器赢了")
    elif player_choice_number==1:
       if comp_number==4 or 0:
          print("你赢了！")
       elif player_choice_number==comp_number:
          print("你和计算机出的一样呢")
       else:
          print("机器赢了")
    elif player_choice_number==2:
       if comp_number==1 or 0:
          print("你赢了！")
       elif player_choice_number==comp_number:
          print("你和计算机出的一样呢")
       else:
          print("机器赢了")
    elif player_choice_number==3:
       if comp_number==1 or 2:
          print("你赢了！")
       elif player_choice_number==comp_number:
          print("你和计算机出的一样呢")
       else:
          print("机器赢了")
    elif player_choice_number==4:
       if comp_number==2 or 3:
          print("你赢了！")
       elif player_choice_number==comp_number:
          print("你和计算机出的一样呢")
       else:
          print("机器赢了") # 输出"-------- "进行分割并对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
#print("计算机的选择为：",comp_choice)
player_choice=input()
"""player_choice_number=name_to_number(player_choice)
comp_number=random.randrange(0,5)
comp_choice=number_to_name(comp_number)"""
rpsls(player_choice)#输出结果
