from django.apps import AppConfig
from threading import Thread

from opcua import Client
from opcua import ua

class TestThread(Thread):

    def run(self):
        print('Thread running')
        url = "opc.tcp://10.8.0.14:4840"

        client = Client(url)

        client.connect()
        print("Client Connected")
        
        client.load_type_definitions() 

        #while True:
        root = client.get_root_node()
        print("Root 노드: ", root)
        objects = client.get_objects_node()
        print("오브젝트: ", objects)

        print("Children of root are: ", objects.get_children())
        #Temperature = Temp.get_value()
        #    print(Temperature)
        #    print("test")


class GetdataConfig(AppConfig):
    name = 'getData'

    def ready(self):
        TestThread().start()