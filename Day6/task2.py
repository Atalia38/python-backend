

name, price, qty = "Keyboard", 129.9, 3
print(f"{name}: ${price:.2f} x {qty} = ${price*qty:.2f}")     
print(f"{qty:03d}")                                           
print("{:>10}".format("right"))                               
pi = 3.1415926535
print(f"pi≈{pi:.3f}")                                        
debug = {"user":"Atalia","role":"admin"}
print(f"{debug!r}")                                           
