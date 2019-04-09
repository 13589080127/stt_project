coding: utf-8
# -*- coding: utf-8 -*-

#变量和命名  （上半部为变量，下半部为对变量的引用）

cars = 100  #汽车100
space_in_a_car = 4.0  #车的空间为4.0人（载客量4人）
drivers = 30  #驾驶员30人
passengers = 90  #旅客90人
cars_not_driven = cars - drivers  #没有驾驶的车辆=汽车数-驾驶员
cars_driven = drivers  #驾驶的车辆=驾驶员数
carpool_capacity = cars_driven * space_in_a_car  #拼车最大限度=驾驶的车辆*车的空间（即4.0）
average_passengers_per_car = passengers / cars_driven  #每个车的平均旅客数=旅客数/驾驶员数

#average_passengers_per_car = car_pool_capcity / passengers  
#此行报错如下：（）
# TracebackTraceback (most recent call last):File "Xt4.py", line 12, in <module>
# average_passengers_per_car = car_pool_capcity / passengers  #每个车的平均旅客数=旅客数/驾驶员数
# NameError: name 'car_pool_capcity' is not defined（car_pool_capcity字段没有定义）

print "There are", cars, "cars available."   #这里可获得的汽车有100辆
print "There are only", drivers, "drivers available."  #这里只有30个驾驶员
print "There will be", cars_not_driven,"empty cars today."  #这里将有70辆没有被驾驶的车辆
print "We can transport", carpool_capacity, "people today."  #我们今天最多可运输120人
print "We have", passengers, "to carpool today."  #我们今天有90个旅客需要拼车
print "We need to put about", average_passengers_per_car, "in each car."  #我们需要使每个汽车3个旅客