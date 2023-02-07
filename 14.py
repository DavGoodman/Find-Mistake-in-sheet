import ezsheets
# Find mistake in sheet
ss = ezsheets.Spreadsheet('GOOGLE SHEETS CODE')
rows = ss[0].getRows()
sheet = ss[0]
mistake = []
for i in range(2, sheet.rowCount):
    if rows[i][0] == "":
        break
    elif int(rows[i][0]) * int(rows[i][1]) == int(rows[i][2]):
        continue
    else:
        print("print mistake found in row " + str(i) + ":")
        mistake.append(rows[i])
print(mistake)
