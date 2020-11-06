import csv
import re

name = input("File Name:")
filename = name + ".csv"

with open(filename, 'r') as csvfile: 
    full_dict = {}
    reader = csv.DictReader(csvfile)
    full_dict = next(reader)

full_dict = { x.translate({32:None, 39:None, 40:None, 41:None, 43:None, 45:None, 47:None, 63:None}) : y for x, y in full_dict.items()}

keys = []
valuesInit = []
values = []

for i in full_dict:
    keys.append(i)

valuesInit.append(full_dict.values())
for i in valuesInit[0]:
    values.append(i)


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

reservesList = [[re.sub('[^0-9a-zA-Z]+', '', x) for x in l] for l in reservesList]
immediatesList = [[re.sub('[^0-9a-zA-Z]+', '', x) for x in l] for l in immediatesList]


import xml.etree.ElementTree as ET


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
c1.text = values[3]
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

problematicValues = values[67:86]
problematicKeys = keys[67:86]

for zz in range(0, len(problematicValues)):
    if problematicValues[zz] != "No":
        category = ET.Element(problematicKeys[zz])
        category.text = problematicValues[zz]
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
    elem1 = ET.Element(immediatesList[i][5].replace(" ", "").replace(",", ""))
    immediateTree.append(elem1)
    elem2 = ET.SubElement(elem1, "CapitalItemAction")
    elem2.text = "IM"
    elem3 = ET.SubElement(elem1, "ImmediateRepairCost")
    elem3.text = immediatesList[i][6]


siteComponents = ET.Element("SiteComponents")
m10.append (siteComponents)

for i in range(0, len(reservesList)):
    if "Site" in reservesList[i][7]:
        elem4 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        siteComponents.append (elem4)

        CapitalItemBasicElements = ET.Element("CapitalItemBasicElements")
        elem4.append (CapitalItemBasicElements)

        elem5 = ET.SubElement(CapitalItemBasicElements, "capitalItemRemainingUsefulLife")
        elem5.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements.append (capitalItemAction)

        CapitalItem15YearProjection = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements.append (CapitalItem15YearProjection)

        elem6 = ET.SubElement(CapitalItem15YearProjection, "capitalItemTotalCost")
        elem6.text = reservesList[i][9]

        if "Site" in reservesList[i][7] and len(reservesList[i][11]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection, "capitalYearOne")
            elem7.text = reservesList[i][11]

        if "Site" in reservesList[i][7] and len(reservesList[i][12]) >= 1:
            elem8 = ET.SubElement(CapitalItem15YearProjection, "capitalYearTwo")
            elem8.text = reservesList[i][12]

        if "Site" in reservesList[i][7] and len(reservesList[i][13]) >= 1:
            elem9 = ET.SubElement(CapitalItem15YearProjection, "capitalYearThree")
            elem9.text = reservesList[i][13]

        if "Site" in reservesList[i][7] and len(reservesList[i][14]) >= 1:
            elem10 = ET.SubElement(CapitalItem15YearProjection, "capitalYearFour")
            elem10.text = reservesList[i][14]

        if "Site" in reservesList[i][7] and len(reservesList[i][15]) >= 1:
            elem11 = ET.SubElement(CapitalItem15YearProjection, "capitalYearFive")
            elem11.text = reservesList[i][15]

        if "Site" in reservesList[i][7] and len(reservesList[i][16]) >= 1:
            elem12 = ET.SubElement(CapitalItem15YearProjection, "capitalYearSix")
            elem12.text = reservesList[i][16]

        if "Site" in reservesList[i][7] and len(reservesList[i][17]) >= 1:
            elem13 = ET.SubElement(CapitalItem15YearProjection, "capitalYearSeven")
            elem13.text = reservesList[i][17]

        if "Site" in reservesList[i][7] and len(reservesList[i][18]) >= 1:
            elem14 = ET.SubElement(CapitalItem15YearProjection, "capitalYearEight")
            elem14.text = reservesList[i][18]

        if "Site" in reservesList[i][7] and len(reservesList[i][19]) >= 1:
            elem15 = ET.SubElement(CapitalItem15YearProjection, "capitalYearNine")
            elem15.text = reservesList[i][19]

        if "Site" in reservesList[i][7] and len(reservesList[i][20]) >= 1:
            elem16 = ET.SubElement(CapitalItem15YearProjection, "capitalYearTen")
            elem16.text = reservesList[i][20]

        if "Site" in reservesList[i][7] and len(reservesList[i][21]) >= 1:
            elem17 = ET.SubElement(CapitalItem15YearProjection, "capitalYearEleven")
            elem17.text = reservesList[i][21]

        if "Site" in reservesList[i][7] and len(reservesList[i][22]) >= 1:
            elem18 = ET.SubElement(CapitalItem15YearProjection, "capitalYearTwelve")
            elem18.text = reservesList[i][22]

structuralFrame = ET.Element("StructuralFrameAndBuildingEnvelopeArchitecturalComponents")
m10.append (structuralFrame)

for i in range(0, len(reservesList)):
    if "Architectural" in reservesList[i][7]:
        elem19 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        structuralFrame.append (elem19)

        CapitalItemBasicElements2 = ET.Element("CapitalItemBasicElements")
        elem19.append (CapitalItemBasicElements2)

        capitalItemRemainingUsefulLife2 = ET.SubElement(CapitalItemBasicElements2, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife2.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements2.append (capitalItemAction)

        CapitalItem15YearProjection2 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements2.append (CapitalItem15YearProjection2)

        elem20 = ET.SubElement(CapitalItem15YearProjection2, "capitalItemTotalCost")
        elem20.text = reservesList[i][9]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][11]) >= 1:
            elem21 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearOne")
            elem21.text = reservesList[i][11]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][12]) >= 1:
            elem22 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearTwo")
            elem22.text = reservesList[i][12]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][13]) >= 1:
            elem23 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearThree")
            elem23.text = reservesList[i][13]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][14]) >= 1:
            elem24 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearFour")
            elem24.text = reservesList[i][14]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][15]) >= 1:
            elem25 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearFive")
            elem25.text = reservesList[i][15]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][16]) >= 1:
            elem26 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearSix")
            elem26.text = reservesList[i][16]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][17]) >= 1:
            elem27 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearSeven")
            elem27.text = reservesList[i][17]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][18]) >= 1:
            elem28 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearEight")
            elem28.text = reservesList[i][18]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][19]) >= 1:
            elem29 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearNine")
            elem29.text = reservesList[i][19]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][20]) >= 1:
            elem30 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearTen")
            elem30.text = reservesList[i][20]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][21]) >= 1:
            elem31 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearEleven")
            elem31.text = reservesList[i][21]

        if "Architectural" in reservesList[i][7] and len(reservesList[i][22]) >= 1:
            elem32 = ET.SubElement(CapitalItem15YearProjection2, "capitalYearTwelve")
            elem32.text = reservesList[i][22]


mechanicalElectrical = ET.Element("MechanicalElectricalAndPlumbingSystems")
m10.append (mechanicalElectrical)

for i in range(0, len(reservesList)):
    if "Mechanical" in reservesList[i][7]:
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

        elem33 = ET.SubElement(CapitalItem15YearProjection3, "capitalItemTotalCost")
        elem33.text = reservesList[i][9]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][11]) >= 1:
            elem34 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearOne")
            elem34.text = reservesList[i][11]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][12]) >= 1:
            elem35 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearTwo")
            elem35.text = reservesList[i][12]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][13]) >= 1:
            elem36 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearThree")
            elem36.text = reservesList[i][13]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][14]) >= 1:
            elem37 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearFour")
            elem37.text = reservesList[i][14]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][15]) >= 1:
            elem38 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearFive")
            elem38.text = reservesList[i][15]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][16]) >= 1:
            elem39 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearSix")
            elem39.text = reservesList[i][16]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][17]) >= 1:
            elem40 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearSeven")
            elem40.text = reservesList[i][17]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][18]) >= 1:
            elem41 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearEight")
            elem41.text = reservesList[i][18]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][19]) >= 1:
            elem42 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearNine")
            elem42.text = reservesList[i][19]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][20]) >= 1:
            elem43 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearTen")
            elem43.text = reservesList[i][20]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][21]) >= 1:
            elem44 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearEleven")
            elem44.text = reservesList[i][21]

        if "Mechanical" in reservesList[i][7] and len(reservesList[i][22]) >= 1:
            elem45 = ET.SubElement(CapitalItem15YearProjection3, "capitalYearTwelve")
            elem45.text = reservesList[i][22]


for i in range(0, len(reservesList)):
    if "Vertical" in reservesList[i][7]:
        verticalTransportation = ET.Element("VerticalTransportation")
        m10.append (verticalTransportation)

for i in range(0, len(reservesList)):
    if "Vertical" in reservesList[i][7]:
        category4 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        verticalTransportation.append (category4)

        CapitalItemBasicElements4 = ET.Element("CapitalItemBasicElements")
        category4.append (CapitalItemBasicElements4)

        capitalItemRemainingUsefulLife4 = ET.SubElement(CapitalItemBasicElements4, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife4.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements4.append (capitalItemAction)

        CapitalItem15YearProjection4 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements4.append (CapitalItem15YearProjection4)

        elem46 = ET.SubElement(CapitalItem15YearProjection4, "capitalItemTotalCost")
        elem46.text = reservesList[i][9]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][11]) >= 1:
            elem47 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearOne")
            elem47.text = reservesList[i][11]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][12]) >= 1:
            elem48 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearTwo")
            elem48.text = reservesList[i][12]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][13]) >= 1:
            elem49 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearThree")
            elem49.text = reservesList[i][13]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][14]) >= 1:
            elem50 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearFour")
            elem50.text = reservesList[i][14]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][15]) >= 1:
            elem51 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearFive")
            elem51.text = reservesList[i][15]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][16]) >= 1:
            elem52 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearSix")
            elem52.text = reservesList[i][16]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][17]) >= 1:
            elem53 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearSeven")
            elem53.text = reservesList[i][17]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][18]) >= 1:
            elem54 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearEight")
            elem54.text = reservesList[i][18]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][19]) >= 1:
            elem55 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearNine")
            elem55.text = reservesList[i][19]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][20]) >= 1:
            elem56 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearTen")
            elem56.text = reservesList[i][20]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][21]) >= 1:
            elem57 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearEleven")
            elem57.text = reservesList[i][21]

        if "Vertical" in reservesList[i][7] and len(reservesList[i][22]) >= 1:
            elem58 = ET.SubElement(CapitalItem15YearProjection4, "capitalYearTwelve")
            elem58.text = reservesList[i][22]


for i in range(0, len(reservesList)):
    if "Safety" in reservesList[i][7]:
        lifeSafety = ET.Element("LifeSafetyFireProtection")
        m10.append (lifeSafety)

for i in range(0, len(reservesList)):
    if "Safety" in reservesList[i][7]:
        category5 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        lifeSafety.append (category5)

        CapitalItemBasicElements5 = ET.Element("CapitalItemBasicElements")
        category5.append (CapitalItemBasicElements5)

        capitalItemRemainingUsefulLife5 = ET.SubElement(CapitalItemBasicElements5, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife5.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements5.append (capitalItemAction)

        CapitalItem15YearProjection5 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements5.append (CapitalItem15YearProjection5)

        elem59 = ET.SubElement(CapitalItem15YearProjection5, "capitalItemTotalCost")
        elem59.text = reservesList[i][9]

        if "Safety" in reservesList[i][7] and len(reservesList[i][11]) >= 1:
            elem60 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearOne")
            elem60.text = reservesList[i][11]

        if "Safety" in reservesList[i][7] and len(reservesList[i][12]) >= 1:
            elem61 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearTwo")
            elem61.text = reservesList[i][12]

        if "Safety" in reservesList[i][7] and len(reservesList[i][13]) >= 1:
            elem62 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearThree")
            elem62.text = reservesList[i][13]

        if "Safety" in reservesList[i][7] and len(reservesList[i][14]) >= 1:
            elem63 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearFour")
            elem63.text = reservesList[i][14]

        if "Safety" in reservesList[i][7] and len(reservesList[i][15]) >= 1:
            elem64 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearFive")
            elem64.text = reservesList[i][15]

        if "Safety" in reservesList[i][7] and len(reservesList[i][16]) >= 1:
            elem65 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearSix")
            elem65.text = reservesList[i][16]

        if "Safety" in reservesList[i][7] and len(reservesList[i][17]) >= 1:
            elem66 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearSeven")
            elem66.text = reservesList[i][17]

        if "Safety" in reservesList[i][7] and len(reservesList[i][18]) >= 1:
            elem67 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearEight")
            elem67.text = reservesList[i][18]

        if "Safety" in reservesList[i][7] and len(reservesList[i][19]) >= 1:
            elem68 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearNine")
            elem68.text = reservesList[i][19]

        if "Safety" in reservesList[i][7] and len(reservesList[i][20]) >= 1:
            elem69 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearTen")
            elem69.text = reservesList[i][20]

        if "Safety" in reservesList[i][7] and len(reservesList[i][21]) >= 1:
            elem70 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearEleven")
            elem70.text = reservesList[i][21]

        if "Safety" in reservesList[i][7] and len(reservesList[i][22]) >= 1:
            elem71 = ET.SubElement(CapitalItem15YearProjection5, "capitalYearTwelve")
            elem71.text = reservesList[i][22]


interiorElements = ET.Element("InteriorElementsDwellingUnitsAndCommonAreas")
m10.append (interiorElements)

for i in range(0, len(reservesList)):
    if "Dwelling" in reservesList[i][7]:
        category6 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        interiorElements.append (category6)

        CapitalItemBasicElements6 = ET.Element("CapitalItemBasicElements")
        category6.append (CapitalItemBasicElements6)

        capitalItemRemainingUsefulLife6 = ET.SubElement(CapitalItemBasicElements6, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife6.text = reservesList[i][10]

        capitalItemAction = ET.Element("CapitalItemAction")
        capitalItemAction.text = ("RR")
        CapitalItemBasicElements6.append (capitalItemAction)

        CapitalItem15YearProjection6 = ET.Element("CapitalItem15YearProjection")
        CapitalItemBasicElements6.append (CapitalItem15YearProjection6)

        elem5 = ET.SubElement(CapitalItem15YearProjection6, "capitalItemTotalCost")
        elem5.text = reservesList[i][9]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][11]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearOne")
            elem5.text = reservesList[i][11]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][12]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearTwo")
            elem6.text = reservesList[i][12]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][13]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearThree")
            elem7.text = reservesList[i][13]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][14]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearFour")
            elem6.text = reservesList[i][14]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][15]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearFive")
            elem5.text = reservesList[i][15]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][16]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearSix")
            elem6.text = reservesList[i][16]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][17]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearSeven")
            elem7.text = reservesList[i][17]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][18]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearEight")
            elem6.text = reservesList[i][18]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][19]) >= 1:
            elem5 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearNine")
            elem5.text = reservesList[i][19]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][20]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearTen")
            elem6.text = reservesList[i][20]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][21]) >= 1:
            elem7 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearEleven")
            elem7.text = reservesList[i][21]

        if "Dwelling" in reservesList[i][7] and len(reservesList[i][22]) >= 1:
            elem6 = ET.SubElement(CapitalItem15YearProjection6, "capitalYearTwelve")
            elem6.text = reservesList[i][22]
        

m11 = ET.Element("OtherCapitalItems")
m10.append (m11)

j1 = ET.SubElement(m11, keys[87])
j1.text = values[87] 
j2 = ET.SubElement(m11, keys[88]) 
j2.text = values[88]
j3 = ET.SubElement(m11, keys[89])
j3.text = values[89]

saveName = name + ".xml"
tree = ET.ElementTree(top)
with open(saveName, "wb") as fh:
    tree.write(fh)
  

print("Success!")