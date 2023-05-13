#PARKING LOT tracler application

from datetime import datetime

class ParkingLot:
    def __init__(self):
        """
        Initializes the ParkingLot object with 2 levels A and B and each level can take 20 spots
        """
        self.levels = {
            "A": [{"spot": i, "vehicle_number_plate": None, "status": "vacant"} for i in range(1,21)],
            "B": [{"spot": i, "vehicle_number_plate": None, "status": "vacant"} for i in range(21,41)]
        }

    def assign_spot(self, vehicle):
        """
        Assigns a vacant parking spot to the vehicle passed as argument
        """
        if (any(d['vehicle_number_plate'] == vehicle.vehicle_number_plate for d in self.levels["A"]) or any(d['vehicle_number_plate'] == vehicle.vehicle_number_plate for d in self.levels["B"]))==False:
            for level, spots in self.levels.items():
                for spot in spots:
                    if not spot["vehicle_number_plate"]==vehicle.vehicle_number_plate:
                        if spot["status"] == "vacant":
                            spot["vehicle_number_plate"] = vehicle.vehicle_number_plate
                            spot["status"] = "occupied"
                            vehicle.time_entered=datetime.now()
                            print(f"Parking spot level:- {level} - spot:- {spot['spot']} assigned to vehicle with number plate {vehicle.vehicle_number_plate}")
                            return
                    else:
                        print(f"This vehicle with vehicle number plate is already parked on ",self.get_spot(vehicle))

            print("Sorry,the parking lot is full, Please try after sometime or try any other parking.")
        else:
            print(f"This vehicle with vehicle number plate {vehicle.vehicle_number_plate} is already parked on ",self.get_spot(vehicle))
    
    def get_spot(self, vehicle):
        """
        Returns the parking spot number and level of the vehicle passed as argument
        """
        for level, spots in self.levels.items():
            for spot in spots:
                if spot["vehicle_number_plate"] == vehicle.vehicle_number_plate:
                    return {"level": level, "spot": spot["spot"]}
        print(f"Vehicle {vehicle.vehicle_number_plate} is not in the parking lot.")

    def free_spot(self,vehicle,spot=None):
        """
        Frees the spot after the vehicle unpark the parking lot
        """
        if (any(d['vehicle_number_plate'] == vehicle for d in self.levels["A"]) or any(d['vehicle_number_plate'] == vehicle for d in self.levels["B"]))==True:
            for level, spots in self.levels.items():
                for spot in spots:
                    if spot["vehicle_number_plate"] == vehicle:
                        spot["vehicle_number_plate"]=None
                        spot["status"]="vacant"
                        print(f"Vehicle {vehicle} is unparked and the level- {level} and spot- {spot['spot']} is free now.")
                        return
        else:
            print(f"Vehicle {vehicle} is not in the parking lot.")
            


class Vehicle:
    def __init__(self,vehicle_number_plate,):
        """
        Initializes the Vehicle object with its number plate, 
        size and time of entry.
        """
        self.vehicle_number_plate = vehicle_number_plate
        self.time_entered = None 
        self.time_exited=None #datetime.now()



# Main function to run the application
def main_function():
    """
    A function to run the program for the parking lot tracker app.
    """
    park_obj = ParkingLot()
    while True:
        try:
            print("Enter 1 to assign a parking spot, 2 to retrieve a parking spot,3 to unpark the vehicle and 0 to exit.")
            choice = int(input())
            if choice == 0:
                print("Exiting...")
                break
            elif choice == 1:
                vehicle_number = input("Enter vehicle number plate: ")
                vehicle=Vehicle(vehicle_number)
                park_obj.assign_spot(vehicle)
            elif choice == 2:
                vehicle_number = input("Enter vehicle number plate: ")
                vehicle=Vehicle(vehicle_number)
                print(park_obj.get_spot(vehicle))
                
            elif choice == 3:
                vehicle_number = input("Enter vehicle number plate: ")
                park_obj.free_spot(vehicle_number)
            
        except Exception as err:
            print("Invalid Input, Please insert proper input")
        

if __name__ == "__main__":
    main_function()