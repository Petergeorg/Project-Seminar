import rclpy
from std_msgs.msg import String

class CommandSubscriberNode:

    def __init__(self):
        self.node = rclpy.create_node('command_subscriber')
        self.subscription = self.node.create_subscription(
            String,
            'asr_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):
        command = msg.data.lower()

        if "go" in command:
            print("Execute: Go")
        elif "stop" in command:
            print("Execute: Stop")
        elif "left" in command:
            print("Execute: Left")
        elif "right" in command:
            print("Execute: Right")
        elif "backwards" in command:
            print("Execute: Backwards")
        elif "faster" in command:
            print("Execute: Faster")
        elif "slower" in command:
            print("Execute: Slower")

def main():
    rclpy.init()
    command_subscriber_node = CommandSubscriberNode()
    rclpy.spin(command_subscriber_node.node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
