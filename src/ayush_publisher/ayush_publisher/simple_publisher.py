import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class MyNode(Node):#inherit from the node class
    def __init__(self):
        super().__init__("simple_publisher") #initializw nde class
        #name of the topic is ayus_chatter and buffer is 10
        self.pub = self.create_publisher(String , "ayush_chatter" , 10 ) #this is defind whiton the node class

        #support variables

        self.counter_ = 0
        self.freq_ = 1

        self.get_logger().info("PUBLISHING AT %d Hz" %self.freq_)

        self.timer_ = self.create_timer(self.freq_ , self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = "HELLO AYUSH COUNT : %d" %self.counter_

        self.pub.publish(msg) #this will publish the msg
        self.counter_ += 1

def main():
    rclpy.init()  #a  interface of ros
    simple_publisher = MyNode()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__' :
    main()





