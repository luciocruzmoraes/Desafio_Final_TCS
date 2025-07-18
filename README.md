RPA Challenge: Invoice Generator
This project is an RPA (Robotic Process Automation) solution designed to automate the process of generating invoices for international commercial transactions. The robot reads data from an Excel spreadsheet, populates an online invoice generation platform, creates PDF invoices, and consolidates payment information into a text file. It also handles currency conversion and manages invoices that cannot be generated due to data issues.

Objective
The main objective of this project is to provide practical experience with RPA concepts learned during training sessions.

Cycle Description
In each cycle, the robot performs the following steps:

Reads an input spreadsheet.

obtains the data.

fills in the data on the invoice generation platform.

Generates PDF invoice files.

Generates a 

.txt file with consolidated information.


Important: Currency conversion is performed when necessary. Each cycle duration is 5 minutes.


Systems and File Types Used
The following systems and file types are utilized:

Exchange Rate Brazilian 

Invoice Generator 

TXT files 

Excel files 

PDF files 

Steps
1. Spreadsheet Adjustment

Rename the input file: The Purchase_plan.xlx file must be renamed to Purchase_data_[day]_[month]_[year].


Create a problem log spreadsheet: Create a new Excel file named invoice_problem_data_[day]_[month]_[year]. This spreadsheet will store information about invoices that could not be generated. It must have the same headers as the input spreadsheet, plus an additional column named "Problem".



Adjust headers: Ensure the headers in the input spreadsheet are correctly named and ordered as follows: Invoice, Who, Bill To, Ship To, Date, Payment Terms, Due Date, PO Number, Itens, Quantity, Rate, National?.

2. Data Validation and Adjustment
Apply the following rules to the spreadsheet information:

Local (Ship To):

Handle special characters.

If blank, set to "Roma – SEDE".

Date:

If the date is earlier than the current date, record all invoice information in 

invoice_problem_data_[day]_[month]_[year], indicating the problem in the "Problem" column.

If blank, it must also be moved to the problem spreadsheet.

Terms (Payment Terms):

Handle special characters.

If blank, record the invoice information in 

invoice_problem_data_[day]_[month]_[year], indicating the problem.

Vencimento (Due Date):

If the date is earlier than the current date, record all invoice information in 

invoice_problem_data_[day]_[month]_[year], indicating the problem.

If blank, set to the last business day of the year.

Número PO (PO Number):

Remove special characters if they exist.

If the value is "0", replace it with "123456".

Item:

If blank, the item will not be considered for invoice creation.

Remove special characters if present.


Important: The invoice_problem_data_[day]_[month]_[year] spreadsheet cannot contain any blank cells.

3. Invoice Creation
Only invoices not listed in 

invoice_problem_data_[day]_[month]_[year] will be created.


Access the Invoice Generator: Navigate to https://invoice-generator.com/.


Select Brazilian Currency.


Add TCS Logo: Upload the logoTCS.png file as the logo.

Populate Invoice Fields:

Invoice number [column A] 

"Who is this from?" [column B] 

"Bill To" [column C] 

"Ship To" [column D] 

Date [column E] 

Payment Terms [column F] 

Due Date [column G] 

PO Number [column H] 


Add Items: For each item in the invoice, add the item name, quantity, and rate. If the item name is blank, it should not be included in the invoice and can be logged as a problem in the invoices with problems spreadsheet.


Notes Section:

If "Importado?" cite_start is "Sim" (Yes), set notes to "Será entregue em até 90 dias" (Will be delivered within 90 days).

If "Importado?" cite_start is "Não" (No), set notes to "Será entregue em até 30 dias" (Will be delivered within 30 days).

Terms Section:

If "Balance Due" (total) is less than $10,000, set terms to "Será entregue de carro" (Will be delivered by car).

If "Balance Due" (total) is between $10,000 and $30,000, set terms to "Será entregue de barco" (Will be delivered by boat).

If "Balance Due" (total) is greater than $30,000, set terms to "Será entregue de avião" (Will be delivered by plane).

Tax Calculation:

If delivered by car and not imported: 0% tax.

If delivered by boat and not imported: 2% tax.

If delivered by plane and not imported: 4% tax.

If delivered by car and imported: 10% tax.

If delivered by boat and imported: 13% tax.

If delivered by plane and imported: 20% tax.


Download Invoice: Download the invoice by choosing PDF.


Save Invoice: Save the PDF file in the invoice_created folder, named as [Invoice Number].pdf.


Record Amount Paid: Register the "Amount Paid" value for each created Invoice for use in item 2.3.

4. Data Consolidation and Return

Create Total Invoices TXT: Create a text file containing the total sum of the "Amount Paid" from the created invoices, named total_invoices.txt.


Currency Conversion: Access https://www.x-rates.com/table/?from=BRL&to=EUR&amount=1 (or similar converter by clicking the calculator icon ) and convert the total value (in Brazilian Reais) to USD, EUR, and GBP. Add these converted values to the 


total_invoices.txt file, along with the sum of the invoices in Reais.

5. Email Notification

Send Completion Email: Upon completion, send an email (the email address should be parameterizable) with the following details:


Subject: "Finalização do processamento – Robô Invoice Generator [day]/[month]/[year]".


Attachment: The Excel file invoice_problem_data_[day]_[month]_[year].


Email Body: The consolidated total of invoices from the total_invoices.txt file from the previous step.


Attachment: A ZIP file named Invoices_Criadas_[day]_[month]_[year].zip containing all created invoices.


Handle Large Attachments: If the generated file from item "4" (likely referring to the ZIP file) exceeds 5MB, partition the files and send them in more than one email.


Email Counter for Multiple Emails: In the subject line, insert an email counter (e.g., “Assunto Email - 1”, “Assunto Email – 2”, and so on).
