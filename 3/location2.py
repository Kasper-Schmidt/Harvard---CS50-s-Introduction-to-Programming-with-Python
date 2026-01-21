import sys

def main():
    coordinate_tuple = (42.376, -71.115) 
    coordinate_list = [42.376, -71.115] 
 
    print(f"{sys.getsizeof(coordinate_tuple)} bytes") # 56 bytes
    print(f"{sys.getsizeof(coordinate_list)} bytes") # 72 bytes

# Så hvis man ved ens værdier ikke skifter, så er tuple bedre, 
# men værdier for en tuple kan ikke ændres


main()