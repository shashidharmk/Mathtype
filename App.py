from tkinter import *
from tkinter import filedialog
import pyperclip

#Create XML line
def line(s):
 h="<p>"
 t="</p>"
 return (h+s+t)
 
#Create math type numbers
def mat(n):
    h='''<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>'''
    t="</mn></math>"
    return (h+str(n)+t)

#Create math type
def matt(s):
    h='''<math xmlns="http://www.w3.org/1998/Math/MathML">'''
    t="</math>"
    return (h+s+t)
    
#Create continuous math type.
def newmat(k):
 l=[]
 for alpha in k:
  l.append(alpha)
 final=[]
 dig=[]
 for let in l:
  if str.isdigit(let):
   dig.append(let)
  elif issign(let):
   final.append("".join(dig))
   dig.clear()
   final.append(let)
  else:
   dig.append(let)
 final.append("".join(dig))
 math=[]
 for d in final:
  if issign(d):
   if d=="/":
    math.append("<mo>"+"&#247;"+"</mo>")
   elif d=="*":
    math.append("<mo>"+"&#215;"+"</mo>")
   elif d==">":
    math.append("<mo>"+"&#62;"+"</mo>")
    #math.append('''<mo>&#160;</mo><menclose notation="box"><mo>&#160;</mo><mo>&#160;</mo><mo>&#62;</mo><mo>&#160;</mo></menclose><mo>&#160;</mo>''')
   elif d=="<":
    math.append("<mo>"+"&#60;"+"</mo>")
    #math.append('''<mo>&#160;</mo><menclose notation="box"><mo>&#160;</mo><mo>&#160;</mo><mo>&#60;</mo><mo>&#160;</mo></menclose><mo>&#160;</mo>''')
   elif d=="$":
    math.append('''<mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><menclose notation="box"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></menclose><mo>&#160;</mo><mo>&#160;</mo>''')
   else:
    math.append("<mo>"+d+"</mo>")
  else:
   math.append("<mn>"+d+"</mn>")
 return matt("".join(math))

#Create mathsigns
def maathsign(sign):
    if sign=="*" :
      return ('''<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#215;</mo></math>''')
    elif sign=="/" :
      return ('''<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#247;</mo></math>''')
    elif sign=="@" :
      return ('''<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#8730;</mo></math>''')
    elif sign=="$" :
      return ""
      #return ('''<math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="bottom"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></menclose></math>''')  
      #return('''<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#160;</mo><mo>&#160;</mo><menclose notation="box"><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo><mo>&#160;</mo></menclose><mo>&#160;</mo><mo>&#160;</mo></math>''')
    elif sign==">" :
      return ('''<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#62;</mo></math>''')
    elif sign=="<" :
      return ('''<math xmlns="http://www.w3.org/1998/Math/MathML"><mo>&#60;</mo></math>''')
    else:
      h='''<math xmlns="http://www.w3.org/1998/Math/MathML">'''
      m="<mo>"
      t="</mo></math>"
      return (h+m+str(sign)+t)

#Check if char is sign.
def issign(sign):
    if sign=="=" :
       return True
    elif sign=="?" :
       return True
    elif sign=="+" :
       return True
    elif sign=="-" :
       return True
    elif sign=="*" :
       return True
    elif sign=="/" :
       return True
    elif sign=="(" :
       return True
    elif sign==")" :
       return True
    elif sign=="@" :
       return True
    elif sign=="$" :
       return True
    elif sign=="<" :
       return True
    elif sign==">" :
       return True
    else:
       return False
	
#Check if char is flot.
def isfloat(n):
	try:
		float(n)
		return True
	except:
		return False

#Create the mathunit.
def mathunit(k):
 l=[]
 previouslet=""
 for alpha in k:
  if (alpha=="[")or(alpha=="]"):
   pass
  else:
   l.append(alpha)
 final=[]
 dig=[]
 for let in l:
  if str.isdigit(let):
   dig.append(let)
  else:
   if str.isdigit(previouslet):
    final.append("".join(dig))
    dig.clear()
   dig.append(let)
  previouslet=let
 final.append("".join(dig))
 math=[]
 for d in final:
  if str.isdigit(d):
   math.append("<mn>"+d+"</mn>")
  else:
   if d=="." or d==",":
    math.append("<mi>"+d+"</mi>")
   else:
    if d=="*":
     math.append("<mo>"+"&#215;"+"</mo>")
    elif d=="/":
     math.append("<mo>"+"&#247;"+"</mo>")
    elif d==">":
     math.append("<mo>"+"&#62;"+"</mo>")
    elif d=="<":
     math.append("<mo>"+"&#60;"+"</mo>")
    else:
     math.append("<mo>&#160;</mo>")
     math.append("<mi>"+d+"</mi>")
     math.append("<mo>&#160;</mo>")
 return matt("".join(math))

#Create the circle.
def circle(k):
 l=[]
 previouslet=""
 for alpha in k:
  if (alpha=="[")or(alpha=="]")or(alpha==","):
   pass
  else:
   l.append(alpha)
 h='''<math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="circle"><mn>'''
 t='''</mn></menclose></math>'''
 return h+"".join(l)+t
 
#Save
def saveas():

    global text

    t = text.get("1.0", "end-1c")

    savelocation=filedialog.asksaveasfilename()

    file1=open(savelocation, "w+")

    file1.write(t)

    file1.close()

#mathtype
def mathtype():
    global text
    t = text.get("1.0", "end-1c")
    data=t.splitlines()
    mathlines=[]
    for i in data:
     s="".join(i)
     l=s.split(" ")
     final=[]
     for k in l:
       try:
           if str.isdigit(k):
            final.append(mat(k))
           elif isfloat(k):
            final.append(mat(k))
           elif issign(k):
            final.append(maathsign(k))
           elif ((ord(k[0])>=48)and((ord(k[0])<=57)))or((ord(k[0])==45)or(ord(k[0])==43)or(ord(k[0])==61)or(ord(k[0])==36)):
            final.append(newmat(k))
           elif (ord(k[0])==91):
            final.append(mathunit(k))
           else:
            final.append(k)
       except:
            final.append(k)
     mathlines.append(line(" ".join(final))) 
    pyperclip.copy("\n".join(mathlines))

#Start editor
def editor():
    global text
    root=Tk("Text Editor")
    root.title("Mathtype")
    text=Text(root) 
    text.grid()
    b=Button(root,text="convert",command=mathtype)
    b.place(relx=0.45, rely=0.95, anchor=CENTER)
    s=Button(root,text="Save",command=saveas)
    s.place(relx=0.55, rely=0.95, anchor=CENTER)
    root.mainloop()

#Start editor
if __name__=='__main__':
 editor()
