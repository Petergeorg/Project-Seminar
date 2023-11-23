import rclpy
from std_msgs.msg import String
import speech_recognition as sr

class ASRNode:

    def __init__(self):
        self.node = rclpy.create_node('asr_node')
        self.publisher = self.node.create_publisher(String, 'asr_command', 10)
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Sag etwas...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="en-US")
            print("Recognized Text:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand")
            return None
        except sr.RequestError as e:
            print(f"Fehler bei der Spracherkennung: {e}")
            return None

    def publish_command(self, command):
        msg = String()
        msg.data = command
        self.publisher.publish(msg)
        print(f"Published command: {command}")

    def main(self):
        while rclpy.ok():
            command = self.recognize_speech()

            if command:
                self.publish_command(command)

def main():
    rclpy.init()
    asr_node = ASRNode()
    asr_node.main()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
