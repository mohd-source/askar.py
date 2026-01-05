code = "PRD2025-BT77-CAT-S-XL-M-XXL-L"

cat = code.split("-")[-6]
batch = code[3:7]
year = code[9:12]
size = code.split("-")[-5:]


print("Size: ",size, " \nYear:",year, " \nBatch: ",batch, " \nCategory ", cat)










data = "BP:120/80 HR=72% Temp=38.9C Sugar-155mg Chol=109mg HDL=45mg LDL=110mg"




bp = data[data.index("BP:") + 3 : data.index(" HR")].strip()
systolic, diastolic = map(int, bp.split("/"))
hr = int(data[data.index("HR=") + 3 : data.index("%")])
temp = float(data[data.index("Temp=") + 5 : data.index("C")])
sugar = int(data[data.index("Sugar-") + 6 : data.index("mg")])
chol = int(data[data.index("Chol=") + 5 : data.index("mg", data.index("Chol="))])
hdl = int(data[data.index("HDL=") + 4 : data.index("mg", data.index("HDL="))])
ldl = int(data[data.index("LDL=") + 4 : data.index("mg", data.index("LDL="))])






sugar_mmol = sugar * 0.0555
chol_mmol = chol * 0.0259
hdl_mmol = hdl * 0.0259
ldl_mmol = ldl * 0.0259






r_s = round(sugar_mmol, 3)
c_s = round(chol_mmol, 3)
h_s = round(hdl_mmol, 3)
l_s = round(ldl_mmol, 3)






print(
    "\nSystolic:", systolic,
    "\nDiastolic:", diastolic,
    "\nHR:", hr,
    "\nTemp:", temp,
    "\nSugar (mmol/L):", r_s,
    "\nChol (mmol/L):", c_s,
    "\nHDL (mmol/L):", h_s,
    "\nLDL (mmol/L):", l_s
)



# print("\nSystolic:", systolic,"\nDiastolic:", diastolic,"\nHR:", hr,"\nTemp:", temp,"\nSuger:", r_s,"\nChol:", c_s,"\nHDL", h_s,"\nLDL:", l_s)
