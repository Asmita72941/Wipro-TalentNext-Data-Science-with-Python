'''
Tech Module: Exception Handling
Project: 1
You had saved the items and their price details in a text file,which you 
purchased yesterday from a nearby super market. You need to know:

1.How many items did you purchase?
2.How many itemsarefree?
3.What is the total amount you had to pay?
4.What is the discount amount?
5.What is the final amount did you payafter the discount?

Help yourself by writing a python code to do this.Include necessary code 
to handle the possible exceptions.

note:
* Data is stored in a text file Purchase-1.txt.
* Each line contains one items details.
* Item name and price isseparated by a space.
* You have to enter the file name during run time.

Sample input1:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50(blank line)
Discount  5

Sample output 1:
Enter the file name:Purchase-1
No of items purchased:3
No of free items:0
Amount to pay:135
Discount given:5
Final amount paid: 130

Sample input2:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250(blank line)
Perfume Free Soup Free(blank line)
Discount 80

Sample output 2:
Enter the file name:Purchase-1
No of items purchased:5
No of free items:2
Amount to pay:485
Discount given:80
Final amount paid: 405
'''


def process_purchase_file(file_name):
    try:
        with open(file_name + ".txt", 'r') as file:
            lines = file.readlines()

        num_items = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue 

            parts = line.split()

            if parts[0].lower() == "discount":
                try:
                    discount = int(parts[1])
                except:
                    print("Warning: Discount value is invalid or missing. Assuming 0.")
                    discount = 0
                continue

            for i in range(0, len(parts), 2):
                item = parts[i]
                price = parts[i+1] if i+1 < len(parts) else ""

                if price.lower() == "free":
                    free_items += 1
                else:
                    try:
                        total_amount += int(price)
                        num_items += 1
                    except ValueError:
                        print(f"Warning: Invalid price for item '{item}'. Skipping.")

        final_amount = total_amount - discount

        print(f"No of items purchased: {num_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found. Please check the file name.")
    except Exception as e:
        print("An unexpected error occurred:", e)

file_input = input("Enter the file name (without .txt): ")
process_purchase_file(file_input)


