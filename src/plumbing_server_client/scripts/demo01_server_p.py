#! usr/bin/env python


import rospy
from plumbing_server_client.srv import *

""" 
    服务端：解析客户端请求 ，产生响应
        1 导包
        2 初始化 ros 节点
        3 创建服务端对象
        4 处理逻辑(回调函数)
        5 spin()

 """
def doNum(request):
    #解析提交的请求
    num1 = request.num1
    num2 = request.num2
    #求和
    sum = num1 + num2
    #将结果封装进响应
    response = AddIntsResponse()
    response.sum = sum 
    rospy.loginfo("服务器解析数据 num1=%d, num2=%d, 结果是 sum = %d!!!!", num1, num2, sum)
    return response


if __name__ == "__main__":
    # 2 初始化 ros 节点
    rospy.init_node("heiShui")
    # 3 创建服务端对象
    server = rospy.Service("addInts",AddInts, doNum)
    rospy.loginfo("服务器启动了")
    # 4 处理逻辑(回调函数)

    # 5 spin()
    rospy.spin()

    pass