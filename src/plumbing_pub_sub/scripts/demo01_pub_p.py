#! /usr/bin/env python

import rospy
from std_msgs.msg import String  #fabu xiaoxi  d leixing
import tools


""" 
shi yong python shixian xiaoxi  fabu 
    1, dao bao 
    2, chushihua ros jiedian
    3, chuangjian fabuzhe duixiang 
    4, bianxie fabu luoji bing fabu shuju 

 """

if __name__=="__main__":
    #   2, chushihua ros jiedian
    rospy.init_node("sanDai")
    rospy.loginfo("num = %d", tools.num)
    # 3, chuangjian fabuzhe duixiang 
    pub = rospy.Publisher("che",String,queue_size=10)


    # 4, bianxie fabu luoji bing fabu shuju 
    # 创建数据
    msg = String()
    # 使用循环发布数据
    # 制定发布频率
    rate = rospy.Rate(1)
    # 设置计数器
    count = 0 
    rospy.sleep(3) 
    
    while not rospy.is_shutdown():
        count += 1
        msg.data = "hello" + str(count)
        # 发布数据
        pub.publish(msg)
        rospy.loginfo("发布的数据:%s",msg.data)
        rate.sleep()



