

s = "  Hello, World!  "


print(s.strip())            
print(s.lower().strip())     


print(s.find("World"))       
print(s.replace("World", "Atalia").strip())  
words = "red,blue, green".replace(" ", "").split(",")
print(words)                 
print("-".join(words))       

t = "abracadabra"
print("cada" in t)          
print(t[:4], t[-4:])         


print(t.count("a"))          
print("12345".isdigit())     
print("Ahmad5".isalnum())  
