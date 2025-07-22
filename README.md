📄 RPA Challenge: Invoice Generator
This project is an RPA (Robotic Process Automation) solution designed to automate the generation of invoices for international commercial transactions.

The robot:
✅ Reads data from an Excel spreadsheet
✅ Fills out an online invoice generation platform
✅ Generates invoices in PDF format
✅ Consolidates payment information into a .txt file
✅ Performs currency conversion when needed
✅ Creates a problem log for invoices with invalid data
✅ Generates analytics charts for better insights

🎯 Objective
The main goal of this project is to provide hands-on experience with RPA concepts learned during training sessions by automating a realistic invoicing process while producing valuable analytics.

🔄 Process Cycle
Each cycle lasts 5 minutes and follows these steps:

Read the input spreadsheet

Validate and adjust data

Log problematic invoices into a separate spreadsheet

Fill in invoice details on the online platform

Generate and save PDF invoices

Create a text file with consolidated totals

Perform currency conversion if necessary

Generate 3 analytics charts for reporting

Send email notifications with attachments

🗂️ Systems & File Types
The robot interacts with the following:

Invoice Generator Platform: https://invoice-generator.com/

Exchange Rate Service: https://www.x-rates.com/

Files:

Excel (.xlsx)

Text files (.txt)

PDF files (.pdf)

ZIP archives (.zip)

PNG charts (.png)

📝 Workflow Details
1️⃣ Spreadsheet Preparation
Rename the input file:
Purchase_plan.xlsx → Purchase_data_[day][month][year].xlsx

Create a problem log:
Generate a new Excel file named invoice_problem_data_[day][month][year].xlsx with the same headers as the input file plus an extra column Problem.

Adjust headers:
Ensure correct order:

pgsql
Copiar
Editar
Invoice | Who | Bill To | Ship To | Date | Payment Terms | Due Date | PO Number | Items | Quantity | Rate | National?
2️⃣ Data Validation & Adjustment
Ship To (Location):

Remove special characters.

If blank, set as “Roma – SEDE”.

Date:

If earlier than today → move to the problem log.

If blank → also move to the problem log.

Payment Terms:

Remove special characters.

If blank → move to the problem log.

Due Date:

If earlier than today → move to the problem log.

If blank → set to the last business day of the year.

PO Number:

Remove special characters.

If value is 0 → replace with 123456.

Items:

Ignore blank items (log as a problem).

Remove special characters.

⚠ The problem log spreadsheet cannot contain any blank cells.

3️⃣ Invoice Creation
Only invoices not listed in the problem log will be created.

Access invoice-generator.com

Select Brazilian currency (BRL)

Upload logoTCS.png as the invoice logo

Populate all invoice fields with validated data

Notes Section:

If Importado? = Yes → “Will be delivered within 90 days”

If Importado? = No → “Will be delivered within 30 days”

Terms Section:

Total < 10,000 → “Will be delivered by car”

10,000 ≤ Total ≤ 30,000 → “Will be delivered by boat”

Total > 30,000 → “Will be delivered by plane”

Tax Calculation:

Delivery	Imported	Tax
Car	No	0%
Boat	No	2%
Plane	No	4%
Car	Yes	10%
Boat	Yes	13%
Plane	Yes	20%

Download the invoice as PDF → Save to invoice_created folder as [Invoice Number].pdf.

4️⃣ Data Consolidation
Create total_invoices.txt:

Sum the “Amount Paid” of all created invoices.

Convert the total BRL value to USD, EUR, and GBP using exchange rates from x-rates.com.

Add all values to the .txt file.

5️⃣ Analytics & Reporting
At the end of each cycle, the robot generates 3 analytics charts:

National vs. International Products

Most Purchased Products

Top Problems Found in Invoices

Charts are saved as .png files for reporting and can be attached to the completion email.

6️⃣ Email Notification
Send an email with:

Subject: Invoice Generator Completion – [day]/[month]/[year]

Body: Summary of total invoices and currency conversions

Attachments:

invoice_problem_data_[day][month][year].xlsx

Invoices_Created_[day][month][year].zip (with all PDFs)

The 3 generated charts

Large files handling:

If ZIP exceeds 5MB, split into multiple emails with a counter in the subject:

e.g. “Invoice Generator Completion – 1/3”

📊 Example Output
yaml
Copiar
Editar
Total invoices generated: 15
Total amount in BRL: R$ 152,350.00
Equivalent in USD: $28,970.00
Equivalent in EUR: €26,500.00
Equivalent in GBP: £22,100.00
And 3 charts:
✅ National vs International Products
✅ Most Purchased Products
✅ Main Problems Found

