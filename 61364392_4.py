import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
fruit_txt = os.path.join(THIS_FOLDER, 'fruit.txt')
result_txt = os.path.join(THIS_FOLDER, 'result.txt')

f = open(fruit_txt,"r") 
dataMap = {}
for line in f:
    column = line.split(" ") # แยก column โดยใช้ spacebar
    fruit_name = column[0] # fruit name
    pricePerKG = column[1] # price
    dataMap.update({fruit_name:float(pricePerKG)})
f.close()

priceTotal = 0
sortedPrice = {}
userInput = input("Enter a fruit do you want: ")
while (userInput != "Quit"):
    weight = float(input("How many grams you want to buy?: "))
    fruitSelected = dataMap[userInput] # เข้าถึงข้อมูลใน dict
    price = float(fruitSelected * (weight/1000)) # คำนวณราคาของผลไม้แต่ละชนิด
    priceTotal += price # คำนวณราคาทั้งหมดที่ต้องจ่าย (รวมผลไม้ทั้งชนิด)
    sortedPrice.update({userInput:float(price)}) # เป็น  dict
    MostExpensive = sorted(sortedPrice, key=sortedPrice.__getitem__, reverse = True) # เป็น list เพราะทำการ sorted/ sorted ปกติจะเรียงตามตัวอักษร แต่อันนี้จะเรียงตามราคา
    userInput = input("Enter a fruit do you want: ")


# TODO: พบปัญหาเรียงตามอักษร -- Solved! -- sorted(sortedPrice, key=sortedPrice.__getitem__, reverse = True)

print(MostExpensive[0], "is the most expensive!") # แสดงว่าซื้ออะไรแพงที่สุด
print(f"Customer has to pay {priceTotal:.2f} baht.") # แสดงราคาทั้งหมด

fw = open(result_txt,"w+") # แสดงผลลัพธ์ไปยัง result.txt 
fw.write("%s is the most expensive!\nCustomer has to pay %.1f baht." % (MostExpensive[0], priceTotal))
fw.close()

'''
เว็บที่ใช้หาข้อมูล
http://code.activestate.com/recipes/577444-get-columns-of-data-from-text-files/
https://www.101computing.net/python-reading-a-text-file/
https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

'''
