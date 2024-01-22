from ThirdTusk import island_area
from firstTask import start_first_task
from SeconsTusk import ValidVeirfy

while True:
     print("Please choose Task 1, Task 2, Task 3, Exit 4")
     choise = int(input())
     if choise == 1:
         print("Choose sorting algorithm Insertion 1, Selection 2, Buble 3, Merge 4, Quick 5")
         n = int(input())
         start_first_task(n)
     if choise == 2:
         print("Enter string")
         n = input()
         ValidVeirfy(n)
     if choise == 3:
         island_area()
     if choise == 4:
        break
