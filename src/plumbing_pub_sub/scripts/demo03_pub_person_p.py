#!  /usr/bin/env python

import rospy
from plumbing_pub_sub.msg import person
""" 
    发布方：发布人的消息
        1、导包
        2、初始化ros节点
        3、创建发布者对象
        4、组织发布逻辑 并 发布数据



 """

if __name__ == "__main__":
    rospy.init_node("dama")

    pub = rospy.Publisher("jiaoSheTou", person, queue_size=10)
    # 创建python数据
    p = person()
    p.name = "奥特曼"
    p.age = 8
    p.height = 1.85
    # 创建rate对象
    rate = rospy.Rate(1)
    # 循环发布数据
    while not rospy.is_shutdown():
        pub.publish(p)
        rospy.loginfo("发布的消息：%s,%d,%.2f",p.name, p.age, p.height)
        rate.sleep()


    pass
