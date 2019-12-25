import openpyxl
wb = openpyxl.load_workbook('fitness.xlsx')
sheet = wb.get_sheet_by_name('FitnessTracker')
sheet['C2'] = 55
wb.save('fitness.xlsx')
