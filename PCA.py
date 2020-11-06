import csv

# # print('hello world')


# # csv file name 
# filename = "12345_PCA.csv"
  

# # print(len(full_dict))



# csv file name 
filename = "12345_PCA.csv"


with open(filename, 'r') as csvfile: 
    full_dict = {}
    reader = csv.DictReader(csvfile)
    full_dict = next(reader)

    
full_dict = { x.translate({32:None, 39:None, 40:None, 41:None, 45:None, 47:None, 63:None}) : y for x, y in full_dict.items()}

keys = []
valuess = []
values = []
for i in full_dict:
    keys.append(i)


valuess.append(full_dict.values())
for i in valuess[0]:
    values.append(i)
print("-----------------")
print(full_dict)
print("-----------------")
print(keys)
print("-----------------")
print(values)
print("--------------------------------------------------")
problematic = values[67:86]
problematicK = keys[67:86]
print(problematic)
print(problematicK)
print("-----------____________________-------------------")

for zz in range(0, len(problematic)):
    if problematic[zz] != "No":
        print(zz, problematic[zz], problematicK[zz])
    # print(str(problematic[zz].index(problematic)))
    # print(problematic.index(zz))












  
with open(filename, 'r') as csvfile:
    csvLists = [] 
    reader = csv.reader(csvfile)
    for row in reader:
        csvLists.append(row)

immediatesList = []
for list in csvLists:
    if list[3] == "IM":
        immediatesList.append(list[:7])




reservesList = []
for list in csvLists:
    if list[3] == "RR":
        reservesList.append(list[:23])

print("---------------------")
# key = next(full_dict.keys())
# keylist = list(full_dict)
# print(key)


import xml.etree.ElementTree as ET

# data = ET.Element('chess')
top = ET.Element('PCARecord')

    
m1 = ET.Element("FannieMaeIdentifiers") 
top.append (m1) 
    
b1 = ET.SubElement(m1, (keys[0])) 
b1.text = (values[0])
b2 = ET.SubElement(m1, keys[1]) 
b2.text = (values[1])
b3 = ET.SubElement(m1, keys[2]) 
b3.text = values[2]
    
m2 = ET.Element("LenderInformation") 
top.append (m2) 
    
c1 = ET.SubElement(m2, keys[3]) 
c1.text = values[2]
c2 = ET.SubElement(m2, keys[4]) 
c2.text = values[4]
    
m3 = ET.Element("ReportInformation") 
top.append (m3) 
    
d1 = ET.SubElement(m3, keys[5]) 
d1.text = values[5]
d2 = ET.SubElement(m3, keys[6]) 
d2.text = values[6]
d3 = ET.SubElement(m3, keys[7]) 
d3.text = values[7]
d4 = ET.SubElement(m3, keys[8]) 
d4.text = values[8]
d5 = ET.SubElement(m3, keys[9]) 
d5.text = values[9]
d6 = ET.SubElement(m3, keys[10]) 
d6.text = values[10]
d7 = ET.SubElement(m3, keys[11]) 
d7.text = values[11]
d8 = ET.SubElement(m3, keys[12])
d8.text = values[12]

m4 = ET.Element("PropertyLocation") 
top.append (m4) 
    
e1 = ET.SubElement(m4, keys[13])
e1.text = values[13]
e2 = ET.SubElement(m4, keys[14])
e2.text = values[14]
e3 = ET.SubElement(m4, keys[15]) 
e3.text = values[15]
e4 = ET.SubElement(m4, keys[16]) 
e4.text = values[16]

m5 = ET.Element("PropertyDetails") 
top.append (m5) 

f1 = ET.SubElement(m5, keys[17])
f1.text = values[17] 
f2 = ET.SubElement(m5, keys[18]) 
f2.text = values[18]
f3 = ET.SubElement(m5, keys[19])
f3.text = values[19]
f4 = ET.SubElement(m5, keys[20])
f4.text = values[20]
f5 = ET.SubElement(m5, keys[21])
f5.text = values[21]
f6 = ET.SubElement(m5, keys[22])
f6.text = values[22]
f7 = ET.SubElement(m5, keys[23])
f7.text = values[23]
f8 = ET.SubElement(m5, keys[24])
f8.text = values[24]
f9 = ET.SubElement(m5, keys[25])
f9.text = values[25] 
f10 = ET.SubElement(m5, keys[26]) 
f10.text = values[26]
f11 = ET.SubElement(m5, keys[27])
f11.text = values[27]
f12 = ET.SubElement(m5, keys[28])
f12.text = values[28]
f13 = ET.SubElement(m5, keys[29])
f13.text = values[29]
f14 = ET.SubElement(m5, keys[30])
f14.text = values[30]
f15 = ET.SubElement(m5, keys[31])
f15.text = values[31]
f16 = ET.SubElement(m5, keys[32])
f16.text = values[32]
f17 = ET.SubElement(m5, keys[33])
f17.text = values[33]

m6 = ET.Element("AssessmentDate") 
top.append (m6) 
    
g1 = ET.SubElement(m6, keys[34]) 
g1.text = values[34]

m7 = ET.Element("AssessmentDetails") 
top.append (m7) 

h1 = ET.SubElement(m7, keys[34])
h1.text = values[34] 
h2 = ET.SubElement(m7, keys[35]) 
h2.text = values[35]
h3 = ET.SubElement(m7, keys[36])
h3.text = values[36]
h4 = ET.SubElement(m7, keys[37])
h4.text = values[37]
h5 = ET.SubElement(m7, keys[38])
h5.text = values[38]
h6 = ET.SubElement(m7, keys[39])
h6.text = values[39]
h7 = ET.SubElement(m7, keys[40])
h7.text = values[40]
h8 = ET.SubElement(m7, keys[41])
h8.text = values[41]
h9 = ET.SubElement(m7, keys[42])
h9.text = values[42] 
h10 = ET.SubElement(m7, keys[43]) 
h10.text = values[43]
h11 = ET.SubElement(m7, keys[44])
h11.text = values[44]
h12 = ET.SubElement(m7, keys[45])
h12.text = values[45]
h13 = ET.SubElement(m7, keys[46])
h13.text = values[46]
h14 = ET.SubElement(m7, keys[47])
h14.text = values[47]
h15 = ET.SubElement(m7, keys[48])
h15.text = values[48]
h16 = ET.SubElement(m7, keys[49])
h16.text = values[49]
h17 = ET.SubElement(m7, keys[50])
h17.text = values[50]
h18 = ET.SubElement(m7, keys[51])
h18.text = values[51] 
h19 = ET.SubElement(m7, keys[52]) 
h19.text = values[52]
h20 = ET.SubElement(m7, keys[53])
h20.text = values[53]
h21 = ET.SubElement(m7, keys[54])
h21.text = values[54]
h22 = ET.SubElement(m7, keys[55])
h22.text = values[55]
h23 = ET.SubElement(m7, keys[56])
h23.text = values[56]
h24 = ET.SubElement(m7, keys[57])
h24.text = values[57]
h25 = ET.SubElement(m7, keys[58])
h25.text = values[58]
h26 = ET.SubElement(m7, keys[59])
h26.text = values[59] 
h27 = ET.SubElement(m7, keys[60]) 
h27.text = values[60]
h28 = ET.SubElement(m7, keys[61])
h28.text = values[61]
h29 = ET.SubElement(m7, keys[62])
h29.text = values[62]
h30 = ET.SubElement(m7, keys[63])
h30.text = values[63]
h31 = ET.SubElement(m7, keys[64])
h31.text = values[64]
h32 = ET.SubElement(m7, keys[65])
h32.text = values[65]
h33 = ET.SubElement(m7, keys[66])
h33.text = values[66]

m8 = ET.Element("KnownProblematicBuildingMaterials") 
top.append (m8) 

for zz in range(0, len(problematic)):
    if problematic[zz] != "No":
        category = ET.Element(problematicK[zz])
        category.text = problematic[zz]
        m8.append (category)

m9 = ET.Element("ImmediateRepairsEstimation") 
top.append (m9) 

i1 = ET.SubElement(m9, keys[86])
i1.text = values[86] 

m10 = ET.Element("CapitalItemCostEvaluation")
top.append (m10)

immediateTree = ET.Element("CriticalRepairs")
m10.append (immediateTree)

for i in range(0, len(immediatesList)):
    # count = 1
    elem1 = ET.Element(immediatesList[i][5].replace(" ", "").replace(",", ""))
    immediateTree.append(elem1)
    elem2 = ET.SubElement(elem1, "CapitalItemAction")
    elem2.text = "IM"
    elem3 = ET.SubElement(elem1, "ImmediateRepairCost")
    elem3.text = immediatesList[i][6]
    # count += 1 
    # print(count)

# reserveTree = ET.Element("reserves")
# top.append (reserveTree)

# for i in range(0, len(reservesList)):
#     elem2 = ET.SubElement(reserveTree, "reserveRepair")
#     elem2.text = reservesList[i][8]

siteComponents = ET.Element("siteComponents")
m10.append (siteComponents)

# x = str(reservesList[5][8].replace(" ", ""))
# xy = ET.Element(x)
# print(x)
# siteComponents.append (xy)

for i in range(0, len(reservesList)):
    if reservesList[i][7] == "Site Components":
        elem3 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        siteComponents.append (elem3)

        CapitalItemBasicElements = ET.Element("CapitalItemBasicElements")
        elem3.append (CapitalItemBasicElements)

        elem4 = ET.SubElement(CapitalItemBasicElements, "capitalItemRemainingUsefulLife")
        elem4.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements.append (capitalItemAction)

        CapitalItem15YearProjection = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements.append (CapitalItem15YearProjection)

        elem5 = ET.SubElement(CapitalItem15YearProjection, "capitalItemTotalCost")
        elem5.text = reservesList[i][9]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][11]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection, "capitalYearOne")
            elem5.text = reservesList[i][11]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][12]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalYearTwo")
            elem6.text = reservesList[i][12]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][13]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection, "capitalYearThree")
            elem7.text = reservesList[i][13]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][14]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalYearFour")
            elem6.text = reservesList[i][14]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][15]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection, "capitalYearFive")
            elem5.text = reservesList[i][15]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][16]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalYearSix")
            elem6.text = reservesList[i][16]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][17]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection, "capitalYearSeven")
            elem7.text = reservesList[i][17]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][18]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalYearEight")
            elem6.text = reservesList[i][18]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][19]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection, "capitalYearNine")
            elem5.text = reservesList[i][19]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][20]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalYearTen")
            elem6.text = reservesList[i][20]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][21]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection, "capitalYearEleven")
            elem7.text = reservesList[i][21]

        if reservesList[i][7] == "Site Components" and len(reservesList[i][22]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalYearTwelve")
            elem6.text = reservesList[i][22]

structuralFrame = ET.Element("StructuralFrameAndBuildingEnvelopeArchitecturalComponents")
m10.append (structuralFrame)

for i in range(0, len(reservesList)):
    if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components":
        category2 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        structuralFrame.append (category2)

        CapitalItemBasicElements2 = ET.Element("CapitalItemBasicElements")
        category2.append (CapitalItemBasicElements2)

        capitalItemRemainingUsefulLife2 = ET.SubElement(CapitalItemBasicElements2, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife2.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements2.append (capitalItemAction)

        CapitalItem15YearProjection2 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements2.append (CapitalItem15YearProjection2)

        elem5 = ET.SubElement(CapitalItem15YearProjection2, "capitalItemTotalCost")
        elem5.text = reservesList[i][9]

        if reservesList[i][7] =="Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][11]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearOne")
            elem5.text = reservesList[i][11]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][12]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearTwo")
            elem6.text = reservesList[i][12]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][13]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearThree")
            elem7.text = reservesList[i][13]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][14]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearFour")
            elem6.text = reservesList[i][14]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][15]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearFive")
            elem5.text = reservesList[i][15]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][16]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearSix")
            elem6.text = reservesList[i][16]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][17]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearSeven")
            elem7.text = reservesList[i][17]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][18]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearEight")
            elem6.text = reservesList[i][18]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][19]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearNine")
            elem5.text = reservesList[i][19]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][20]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearTen")
            elem6.text = reservesList[i][20]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][21]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearEleven")
            elem7.text = reservesList[i][21]

        if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components" and len(reservesList[i][22]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearTwelve")
            elem6.text = reservesList[i][22]

mechanicalElectrical = ET.Element("MechanicalElectricalAndPlumbingSystems")
m10.append (mechanicalElectrical)

for i in range(0, len(reservesList)):
    if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems":
        category3 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        mechanicalElectrical.append (category3)

        CapitalItemBasicElements3 = ET.Element("CapitalItemBasicElements")
        category3.append (CapitalItemBasicElements3)

        capitalItemRemainingUsefulLife3 = ET.SubElement(CapitalItemBasicElements3, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife3.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements3.append (capitalItemAction)

        CapitalItem15YearProjection3 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements3.append (CapitalItem15YearProjection3)

        elem5 = ET.SubElement(CapitalItem15YearProjection3, "capitalItemTotalCost")
        elem5.text = reservesList[i][9]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][11]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearOne")
            elem5.text = reservesList[i][11]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][12]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearTwo")
            elem6.text = reservesList[i][12]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][13]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearThree")
            elem7.text = reservesList[i][13]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][14]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearFour")
            elem6.text = reservesList[i][14]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][15]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearFive")
            elem5.text = reservesList[i][15]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][16]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearSix")
            elem6.text = reservesList[i][16]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][17]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearSeven")
            elem7.text = reservesList[i][17]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][18]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearEight")
            elem6.text = reservesList[i][18]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][19]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearNine")
            elem5.text = reservesList[i][19]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][20]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearTen")
            elem6.text = reservesList[i][20]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][21]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearEleven")
            elem7.text = reservesList[i][21]

        if reservesList[i][7] == "Mechanical Electrical And Plumbing Systems" and len(reservesList[i][22]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearTwelve")
            elem6.text = reservesList[i][22]

interiorElements = ET.Element("InteriorElementsDwellingUnitsAndCommonAreas")
m10.append (interiorElements)

for i in range(0, len(reservesList)):
    if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas":
        category4 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        interiorElements.append (category4)

        CapitalItemBasicElements4 = ET.Element("CapitalItemBasicElements")
        category4.append (CapitalItemBasicElements4)

        capitalItemRemainingUsefulLife3 = ET.SubElement(CapitalItemBasicElements4, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife3.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements4.append (capitalItemAction)

        CapitalItem15YearProjection4 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements4.append (CapitalItem15YearProjection4)

        elem5 = ET.SubElement(CapitalItem15YearProjection4, "capitalItemTotalCost")
        elem5.text = reservesList[i][9]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][11]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearOne")
            elem5.text = reservesList[i][11]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][12]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearTwo")
            elem6.text = reservesList[i][12]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][13]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearThree")
            elem7.text = reservesList[i][13]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][14]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearFour")
            elem6.text = reservesList[i][14]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][15]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearFive")
            elem5.text = reservesList[i][15]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][16]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearSix")
            elem6.text = reservesList[i][16]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][17]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearSeven")
            elem7.text = reservesList[i][17]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][18]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearEight")
            elem6.text = reservesList[i][18]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][19]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearNine")
            elem5.text = reservesList[i][19]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][20]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearTen")
            elem6.text = reservesList[i][20]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][21]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearEleven")
            elem7.text = reservesList[i][21]

        if reservesList[i][7] == "Interior Elements Dwelling Units And Common Areas" and len(reservesList[i][22]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearTwelve")
            elem6.text = reservesList[i][22]
        

m11 = ET.Element("OtherCapitalItems")
m10.append (m11)

j1 = ET.SubElement(m11, keys[87])
j1.text = values[87] 
j2 = ET.SubElement(m11, keys[88]) 
j2.text = values[88]
j3 = ET.SubElement(m11, keys[89])
j3.text = values[89]


tree = ET.ElementTree(top)
with open("employees.xml", "wb") as fh:
    tree.write(fh)
  








# # Adding a subtag named `Opening` 
# # inside our root tag 
# element1 = ET.SubElement(data, 'Opening') 
  
# # Adding subtags under the `Opening` 
# # subtag  
# # s_elem1 = ET.SubElement(element1, 'E4') 
# # s_elem2 = ET.SubElement(element1, 'D4') 
# makeNumber()
  
  
# # Adding text between the `E4` and `D5`  
# # subtag 
# makeNumber()
  
# # Converting the xml data to byte object, 
# # for allowing flushing data to file  
# # stream 
# b_xml = ET.tostring(data) 
  
# # Opening a file under the name `items2.xml`, 
# # with operation mode `wb` (write + binary) 
# with open("GFG.xml", "wb") as f: 
#     f.write(b_xml) 