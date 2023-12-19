#! usr/bin/env python


import rospy
from plumbing_server_client.srv import *
import sys
""" 
    客户端：组织并提交请求 ，处理服务端响应
        1 导包
        2 初始化ros节点
        3 创建 客户端对象
        4 组织请求数据，并发送请求
        5 处理响应

 """



if __name__ == "__main__":

    # 判参数长度
    if len(sys.argv) != 3 :
        rospy.logerr("传入个数不对")
        sys.exit(1)

    # 2 初始化ros节点
    rospy.init_node("erHei")

    # 3 创建 客户端对象
    client = rospy.ServiceProxy("addInts", AddInts)
    # 解析传入的参数
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    client.wait_for_service()

    # 4 组织请求数据，并发送请求
    response = client.call(num1,num2)
    # 5 处理响应
    rospy.loginfo("响应的数据：%d", response.sum)

    pass