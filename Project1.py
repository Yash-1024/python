# Task 1
radius = int(input("Input the radius of the circle: "))
print(f"The area of the circle with radius {radius} is: {3.14*radius**2}")


# Task 2
file_Name = input("Input the Filename: ")
extentions = {".DOC": "doctype",".DOCX": "doctype",".HTML" : "hyper text markup language",".HTM" : "hyper text markup language",".ODT" : "OpenOffice Document file",".PDF" : "Portable Document Format",".XLS" : "Excel Binary File Format",".XLSX" : "Excel Workbook",".ODS" : "OpenDocument Spreadsheet",".PPT" : "PowerPoint file",".PPTX" : "default presentation file format",".TXT" : "text file",".py" : "python file",".java" : "java file",".c" : "c language file",".css" : "Cascading Style Sheets",".json" : "JavaScript Object Notation"}
with open('extension_list.txt', 'r') as f:     #  A file with name extention_list.txt exists with name of all above extension in it 
    for i in range(17):
        text = f.readline()
        text = text.replace("\n","")
        # print(text)
        if (file_Name.find(text) != -1):
            print(f"The extension of the file {file_Name} is : {extentions.get(text)}")
            break
    else:
        print("!!!---Extension not recorgised---!!!")


