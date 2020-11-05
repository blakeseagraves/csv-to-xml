import csv

# # print('hello world')


# # # csv file name 
# # filename = "12345_PCA.csv"
  
# # with open(filename, 'r') as csvfile: 
# #     full_dict = {}
# #     reader = csv.DictReader(csvfile)
# #     full_dict = next(reader)
    
# # full_dict = { x.translate({32:None, 39:None, 40:None, 41:None, 63:None}) : y for x, y in full_dict.items()}


# # print("-----------------")
# # print(full_dict)
# # print("-----------------")
# # print(len(full_dict))



# csv file name 
filename = "12345_PCA.csv"
  
with open(filename, 'r') as csvfile:
    csvLists = [] 
    reader = csv.reader(csvfile)
    for row in reader:
        csvLists.append(row)

immediatesList = []
for list in csvLists:
    if list[3] == "IM":
        print(list[:7])
        immediatesList.append(list[:7])

print("---------------------")
print(len(immediatesList))

reservesList = []
for list in csvLists:
    if list[3] == "RR":
        print(list[:23])
        reservesList.append(list[:23])

print("---------------------")
print(len(reservesList))

yearOne = []
for i in range(0, len(reservesList)):
    yearOne.append(reservesList[i][11])
print(yearOne)



x = ["apple", "banana", "orange", "grape", "lemon"]
numberX = len(x)

import xml.etree.ElementTree as ET

# data = ET.Element('chess')
top = ET.Element('root')

immediateTree = ET.Element("immediates")
top.append (immediateTree)

for i in range(0, len(immediatesList)):
    # count = 1
    elem1 = ET.SubElement(immediateTree, "immediateRepair")
    elem1.text = immediatesList[i][5]
    # count += 1 
    # print(count)

# reserveTree = ET.Element("reserves")
# top.append (reserveTree)

# for i in range(0, len(reservesList)):
#     elem2 = ET.SubElement(reserveTree, "reserveRepair")
#     elem2.text = reservesList[i][8]

siteComponents = ET.Element("siteComponents")
top.append (siteComponents)

# x = str(reservesList[5][8].replace(" ", ""))
# xy = ET.Element(x)
# print(x)
# siteComponents.append (xy)

for i in range(0, len(reservesList)):
    if reservesList[i][7] == "Site Components":
        elem3 = ET.Element((reservesList[i][8].replace(" ", "")))
        siteComponents.append (elem3)

        CapitalItemBasicElements = ET.Element("CapitalItemBasicElements")
        elem3.append (CapitalItemBasicElements)

        elem4 = ET.SubElement(CapitalItemBasicElements, "capitalItemRemainingUsefulLife")
        elem4.text = reservesList[i][10]

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
top.append (structuralFrame)

for i in range(0, len(reservesList)):
    if reservesList[i][7] == "Structural Frame And Building Envelope Architectural Components":
        category2 = ET.Element((reservesList[i][8].replace(" ", "").replace(",", "")))
        structuralFrame.append (category2)

        CapitalItemBasicElements2 = ET.Element("CapitalItemBasicElements")
        category2.append (CapitalItemBasicElements2)

        capitalItemRemainingUsefulLife2 = ET.SubElement(CapitalItemBasicElements2, "capitalItemRemainingUsefulLife")
        capitalItemRemainingUsefulLife2.text = reservesList[i][10]

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