import csv

print('hello world')


# csv file name 
filename = "12345_ESA.csv"
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    full_dict = {}
    reader = csv.DictReader(csvfile)
    for row in reader:
        full_dict.update(row)

print("-----------------")
print(full_dict)
print("-----------------")
print(list(full_dict.keys())[0])

# full_dict = { x.translate({32:None}) : y for x, y in full_dict.items()}

# full_dict = { x.translate({39:None}) : y for x, y in full_dict.items()}

# full_dict = { x.translate({63:None}) : y for x, y in full_dict.items()}

full_dict = { x.translate({32:None, 39:None, 40:None, 41:None, 63:None}) : y for x, y in full_dict.items()}


print("-----------------")

print("new dictionary: ", full_dict)
print("-----------------")
print(str(list(full_dict.keys())[53]))
print(str(list(full_dict.values())[53])) 
print(len(full_dict.keys()))



import xml.etree.ElementTree as gfg  
  
  
def GenerateXML(fileName) : 
      
    root = gfg.Element("root") 
      
    m1 = gfg.Element("FannieMaeIdentifiers") 
    root.append (m1) 
      
    b1 = gfg.SubElement(m1, str(list(full_dict.keys())[0])) 
    b1.text = str(list(full_dict.values())[0])
    b2 = gfg.SubElement(m1, str(list(full_dict.keys())[1])) 
    b2.text = str(list(full_dict.values())[1])
      
    m2 = gfg.Element("LenderInformation") 
    root.append (m2) 
      
    c1 = gfg.SubElement(m2, str(list(full_dict.keys())[2])) 
    c1.text = str(list(full_dict.values())[2])
    c2 = gfg.SubElement(m2, str(list(full_dict.keys())[3])) 
    c2.text = str(list(full_dict.values())[3])
      
    m3 = gfg.Element("ReportInformation") 
    root.append (m3) 
      
    d1 = gfg.SubElement(m3, str(list(full_dict.keys())[4])) 
    d1.text = str(list(full_dict.values())[4])
    d2 = gfg.SubElement(m3, str(list(full_dict.keys())[5])) 
    d2.text = str(list(full_dict.values())[5])
    d3 = gfg.SubElement(m3, str(list(full_dict.keys())[6])) 
    d3.text = str(list(full_dict.values())[6])
    d4 = gfg.SubElement(m3, str(list(full_dict.keys())[7])) 
    d4.text = str(list(full_dict.values())[7])
    d5 = gfg.SubElement(m3, str(list(full_dict.keys())[8])) 
    d5.text = str(list(full_dict.values())[8])
    d6 = gfg.SubElement(m3, str(list(full_dict.keys())[9])) 
    d6.text = str(list(full_dict.values())[9])
    d7 = gfg.SubElement(m3, str(list(full_dict.keys())[10])) 
    d7.text = str(list(full_dict.values())[10])



    m4 = gfg.Element("PropertyLocation") 
    root.append (m4) 
      
    e1 = gfg.SubElement(m4, str(list(full_dict.keys())[11])) 
    e1.text = str(list(full_dict.values())[11])
    e2 = gfg.SubElement(m4, str(list(full_dict.keys())[12])) 
    e2.text = str(list(full_dict.values())[12])
    e3 = gfg.SubElement(m4, str(list(full_dict.keys())[13])) 
    e3.text = str(list(full_dict.values())[13])
    e4 = gfg.SubElement(m4, str(list(full_dict.keys())[14])) 
    e4.text = str(list(full_dict.values())[14])


    m5 = gfg.Element("PropertyDetails") 
    root.append (m5) 

    f1 = gfg.SubElement(m5, str(list(full_dict.keys())[15])) 
    f1.text = str(list(full_dict.values())[15])  
    f2 = gfg.SubElement(m5, str(list(full_dict.keys())[16])) 
    f2.text = str(list(full_dict.values())[16])
    f3 = gfg.SubElement(m5, str(list(full_dict.keys())[17])) 
    f3.text = str(list(full_dict.values())[17])
    f4 = gfg.SubElement(m5, str(list(full_dict.keys())[18]))
    f4.text = str(list(full_dict.values())[18])
    f5 = gfg.SubElement(m5, str(list(full_dict.keys())[19]))
    f5.text = str(list(full_dict.values())[19])
    f6 = gfg.SubElement(m5, str(list(full_dict.keys())[20])) 
    f6.text = str(list(full_dict.values())[20])
    f7 = gfg.SubElement(m5, str(list(full_dict.keys())[21])) 
    f7.text = str(list(full_dict.values())[21])
    f8 = gfg.SubElement(m5, str(list(full_dict.keys())[22])) 
    f8.text = str(list(full_dict.values())[22])


    m6 = gfg.Element("AssessmentDate") 
    root.append (m6) 
      
    g1 = gfg.SubElement(m6, str(list(full_dict.keys())[22])) 
    g1.text = str(list(full_dict.values())[22])

    m7 = gfg.Element("AssessmentDetails") 
    root.append (m7) 
      
    h1 = gfg.SubElement(m7, str(list(full_dict.keys())[23])) 
    h1.text = str(list(full_dict.values())[23])
    h2 = gfg.SubElement(m7, str(list(full_dict.keys())[24])) 
    h2.text = str(list(full_dict.values())[24])
    h3 = gfg.SubElement(m7, str(list(full_dict.keys())[25])) 
    h3.text = str(list(full_dict.values())[25])
    h4 = gfg.SubElement(m7, str(list(full_dict.keys())[26])) 
    h4.text = str(list(full_dict.values())[26])
    h5 = gfg.SubElement(m7, str(list(full_dict.keys())[27])) 
    h5.text = str(list(full_dict.values())[27])
    h6 = gfg.SubElement(m7, str(list(full_dict.keys())[28])) 
    h6.text = str(list(full_dict.values())[28])
    h7 = gfg.SubElement(m7, str(list(full_dict.keys())[29])) 
    h7.text = str(list(full_dict.values())[29])
    h8 = gfg.SubElement(m7, str(list(full_dict.keys())[30])) 
    h8.text = str(list(full_dict.values())[30])
    h9 = gfg.SubElement(m7, str(list(full_dict.keys())[31])) 
    h9.text = str(list(full_dict.values())[31])
    h10 = gfg.SubElement(m7, str(list(full_dict.keys())[32])) 
    h10.text = str(list(full_dict.values())[32])
    h11 = gfg.SubElement(m7, str(list(full_dict.keys())[33])) 
    h11.text = str(list(full_dict.values())[33])
    h12 = gfg.SubElement(m7, str(list(full_dict.keys())[34])) 
    h12.text = str(list(full_dict.values())[34])
    h13 = gfg.SubElement(m7, str(list(full_dict.keys())[35])) 
    h13.text = str(list(full_dict.values())[35])
    h14 = gfg.SubElement(m7, str(list(full_dict.keys())[36])) 
    h14.text = str(list(full_dict.values())[36])
    h15 = gfg.SubElement(m7, str(list(full_dict.keys())[37])) 
    h15.text = str(list(full_dict.values())[37])
    h16 = gfg.SubElement(m7, str(list(full_dict.keys())[38])) 
    h16.text = str(list(full_dict.values())[38])
    h17 = gfg.SubElement(m7, str(list(full_dict.keys())[39])) 
    h17.text = str(list(full_dict.values())[39])
    h18 = gfg.SubElement(m7, str(list(full_dict.keys())[40])) 
    h18.text = str(list(full_dict.values())[40])
    h19 = gfg.SubElement(m7, str(list(full_dict.keys())[41])) 
    h19.text = str(list(full_dict.values())[41])
    h20 = gfg.SubElement(m7, str(list(full_dict.keys())[42])) 
    h20.text = str(list(full_dict.values())[42])
    h21 = gfg.SubElement(m7, str(list(full_dict.keys())[43])) 
    h21.text = str(list(full_dict.values())[43])
    h22 = gfg.SubElement(m7, str(list(full_dict.keys())[44])) 
    h22.text = str(list(full_dict.values())[44])
    h23 = gfg.SubElement(m7, str(list(full_dict.keys())[45])) 
    h23.text = str(list(full_dict.values())[45])
    h24 = gfg.SubElement(m7, str(list(full_dict.keys())[46])) 
    h24.text = str(list(full_dict.values())[46])
    h25 = gfg.SubElement(m7, str(list(full_dict.keys())[47])) 
    h25.text = str(list(full_dict.values())[47])
    h26 = gfg.SubElement(m7, str(list(full_dict.keys())[48])) 
    h26.text = str(list(full_dict.values())[48])
    h27 = gfg.SubElement(m7, str(list(full_dict.keys())[49])) 
    h27.text = str(list(full_dict.values())[49])
    h28 = gfg.SubElement(m7, str(list(full_dict.keys())[50])) 
    h28.text = str(list(full_dict.values())[50])
    h29 = gfg.SubElement(m7, str(list(full_dict.keys())[51])) 
    h29.text = str(list(full_dict.values())[51])
    h30 = gfg.SubElement(m7, str(list(full_dict.keys())[52])) 
    h30.text = str(list(full_dict.values())[52])
    h31 = gfg.SubElement(m7, str(list(full_dict.keys())[53])) 
    h31.text = str(list(full_dict.values())[53])
    h32 = gfg.SubElement(m7, str(list(full_dict.keys())[54])) 
    h32.text = str(list(full_dict.values())[54])
    h33 = gfg.SubElement(m7, str(list(full_dict.keys())[55])) 
    h33.text = str(list(full_dict.values())[55])
    h34 = gfg.SubElement(m7, str(list(full_dict.keys())[56])) 
    h34.text = str(list(full_dict.values())[56])
    h35 = gfg.SubElement(m7, str(list(full_dict.keys())[57])) 
    h35.text = str(list(full_dict.values())[57])
    h36 = gfg.SubElement(m7, str(list(full_dict.keys())[58])) 
    h36.text = str(list(full_dict.values())[58])
    h37 = gfg.SubElement(m7, str(list(full_dict.keys())[59])) 
    h37.text = str(list(full_dict.values())[59])
    h38 = gfg.SubElement(m7, str(list(full_dict.keys())[60])) 
    h38.text = str(list(full_dict.values())[60])
    h39 = gfg.SubElement(m7, str(list(full_dict.keys())[61])) 
    h39.text = str(list(full_dict.values())[61])
    h40 = gfg.SubElement(m7, str(list(full_dict.keys())[62])) 
    h40.text = str(list(full_dict.values())[62])
    h41 = gfg.SubElement(m7, str(list(full_dict.keys())[63])) 
    h41.text = str(list(full_dict.values())[63])
    h42 = gfg.SubElement(m7, str(list(full_dict.keys())[64])) 
    h42.text = str(list(full_dict.values())[64])
    h43 = gfg.SubElement(m7, str(list(full_dict.keys())[65])) 
    h43.text = str(list(full_dict.values())[65])
 
      
    tree = gfg.ElementTree(root) 
      
    with open (fileName, "wb") as files : 
        tree.write(files) 
  
# Driver Code 
if __name__ == "__main__":  
    GenerateXML("test3.xml") 