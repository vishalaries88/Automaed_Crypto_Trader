import json
import os

class AutimatedTradingClient():
    #config_data{}
    def __call__(self, *args, **kwargs):
        return self
    
    def show_graph(self):
        return

    def cancel_order(self,order_id):
        return

    def create_buy_order(self,pair_name):
        return

    def create_sell_order(self,pair_name):
        return

    def show_predicted_value(self,pair_name):
        return

    def stay_alive(self):
        #This function responds to the server's ping in case of no activity and keep the connection alive
        return
    
    def create_session(self):
        return
        
    def parse_config_json(self,json_config_path):
        print("Trying to read "+json_config_path)
        with open(json_config_path,'r') as json_file:
            temp_data = json_file.read()
        
        config_data = json.loads(temp_data)
        #print(config_data)
        return



if __name__ == '__main__':

    print("Running Main()")
    json_config_path = os.getcwd() + "/config.json"
    print(os.getcwd())
    client = AutimatedTradingClient()
    client.parse_config_json(json_config_path)
