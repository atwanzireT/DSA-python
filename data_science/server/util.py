import json
import pickle

__locations = None
__modal = None
__data_columns = None


def get_location_names():
    return __locations


def load_saved_antifacts():
    print("Printing saved antifacts ... start")
    global __data_columns
    global __locations
    with open("./antifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./antifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Loading finished ...")

if __name__ == "__main__":
    load_saved_antifacts()
    print(get_location_names())
