a1 = [3,4,5,1,2,4,2]
a2 = [4,5,1,2,4,2,3]

# Array a2 is rotation of array a1 if it's sublist of a1+a1
def is_rotation(a1, a2):
   if len(a1) != len(a2):
       return False

   double_array = a1 + a1

   return check_sublist(double_array, a2)

def check_sublist(a1, a2):
   if len(a1) < len(a2):
       return False

   j = 0
   for i in range(len(a1)):
        if a1[i] == a2[j]:
              j += 1
        else:
              j = 0

        if j == len(a2):
              return True

   return j == len(a2)