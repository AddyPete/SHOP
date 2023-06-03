import yaml

def multiply_buy_price(file_path, factor, quantity_factor):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

        # Iterate over the YAML data and multiply buyPrice values
        for key, value in yaml_data['buyblocks']['items'].items():
            #print ("KEY: {0} VALUE {0}".format(key,value))
            if 'buyPrice' in value:
                value['buyPrice'] *= factor
            if 'item' in value and 'quantity' in value['item']:
                value['item']['quantity'] *= quantity_factor

            

    with open(file_path, 'w') as file:
        yaml.dump(yaml_data, file)

# Provide the path to your YAML file
yaml_file_path = "C:/Users/adria/OneDrive/Desktop/JMC STUFFS/SHOP/buyblocks.yml"

# Specify the multiplication factor
multiplication_factor = 50.0  # Modify with your desired factor
quantity_factor = 16
# Multiply the buyPrice values in the YAML file
multiply_buy_price(yaml_file_path, multiplication_factor, quantity_factor)