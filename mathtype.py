import pyperclip
import docx
doc=docx.Document("text.docx")
data=[]
mathlines=[]

for para in doc.paragraphs:
 data.append(str(para.text))
 
def line(s):
 h="<p>"
 t="</p>"
 return (h+s+t)
 
def mat(n):
    h='''<math xmlns="http://www.w3.org/1998/Math/MathML"><mn>'''
    t="</mn></math>"
    return (h+str(n)+t)

def matt(s):
    h='''<math xmlns="http://www.w3.org/1998/Math/MathML">'''
    t="</math>"
    return (h+s+t)
    
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
	
def isfloat(n):
	try:
		float(n)
		return True
	except:
		return False

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