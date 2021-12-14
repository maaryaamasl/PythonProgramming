def computepay(h, r):
   pay=0
   if h <= 40:
      pay = h * r
   else:
      pay = 40*r + (h-40)*1.50*r
   return pay

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rates:")
rate = float(rate)

p = computepay(hrs, rate)
print("Pay", p)
