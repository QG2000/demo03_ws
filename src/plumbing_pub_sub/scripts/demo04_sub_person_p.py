#! /usr/bin/env python
"""
    订阅方:
        订阅消息

"""
import rospy
from plumbing_pub_sub.msg import person

def doPerson(p):
    rospy.loginfo("小伙子的数据:%s, %d, %.2f",p.name, p.age, p.height)


if __name__ == "__main__":
    #1.初始化节点
    rospy.init_node("daYe")
    #2.创建订阅者对象
    sub = rospy.Subscriber("jiaoSheTou",person,doPerson,queue_size=10)
    rospy.spin() #4.循环
