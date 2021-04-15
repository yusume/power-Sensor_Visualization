    
# apps.py

from django.apps import AppConfig
from threading import Thread



class TestThread(Thread):

    def run(self):
        print('Thread running')



class StackConfig(AppConfig):
    name = 'stack'

    def ready(self):
        TestThread().start()


    #def datachange_notification(self, node, val, data):
     #   print("Python: New data change event", node, val)

    #def event_notification(self, event):
    #    print("Python: New event", event)

   # opc = Client("opc.tcp://10.8.0.14:4840")
   # temp=opc.connect()
  #  print("Client Connected")

    # try:
    #     client.connect()

    #     root = client.get_root_node()
    #     # Temperature = Temp.get_value()
    #     print(root)
    #         # print(Temp)
    # finally:
    #     client.disconnect()

