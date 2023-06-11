# visitormanagement
Setting the Visitor Appointment
1. The System will be accessible by All Employees via WebPage
2. Host will initiate the Visitor Appointment through the Webpage
• The Host must enter the following details and create an Appointment Number.
i. Name
ii. email ID
iii. Contact Number
iv. purpose of Visit
v. Appointment date
• The host must be able to edit the above details using the Appointment Number.
3. The system will send the Email notification for the Approval of the Host’s Manager.
4. The Host’s Manager has to approve the Visitor’s Appointment.
5. Once the Host’s Manager has approved, the System will generate a Google form with the 
below details and the Google form link will be mailed to the Visitor
• Company*
• Country*
• Image *
• Vehicle details
• Device Details (Laptops/HW benches)
i. Device type
ii. Requires Wi-fi Access.
iii. Device Serial Number.
6. Visitor upon receiving the Email with Google form Link, must enter all valid details and 
submit the form.
7. Once all the data has been updated in the system, the System will generate a QR Code for all 
the data related to the Visitor and email the QR code along with do & donts inside office 
premise information’s to the Visitor. (QR code must be saved in the system for further 
verification)
Process when visitor enters the Premises
1. The system will contain all the information related to the Visitor in the DB along with the QR 
code.
2. Visitor must show the QR code when he enters the premises.
3. Once the visitor shows the QR code, the Security should be able to scan the QR code and 
check for validity.
4. Once the Security has confirmed the valid QR code, the system must initiate an Email 
notification to the host that the Visitor has entered the premises.
5. This system must be accessible at the Security at Gate, Receptionist and Security at 1st Floor 
so that at all these places the generated QR code must be validated.
Software Requirements:
1. Data Base
2. Web Engine 
3. Python (or any other server-side scripting language), JS(React, Angular, plain) , HTML, CSS
4. Web browser
Hardware Requirement:
1. Webcam
2. Laptop/Desktop
3. Server to host the Web application (Provided by EB)
Data Handling:
1. When the Host creates the Appointment Request the system must insert the visitor’s data 
into the DB and provide a unique Appointment Number and update the status column of the 
entry as New. Hostname must be entered to the database for traceability.
2. When the host’s Manager has approved the Visitor’s Appointment the status of the entry 
must be updated as Approved.
3. When all the data has been imported from the Google form, the data must be updated to 
the existing entry in DB against the appointment number and update the status column 
AddedInfo.
4. Once the System generates the QR code the QR code must be saved in the system and 
expiry date must be set (Expiry time will be 11:59pm of the appointment date).
5. Once the visitor has provided all the information via Google form, the status column must be 
updated as Valid.
6. When a QR code is scanned at any security, only the appointment numbers with status as 
Valid/Entered and matching date must be provided access to the premises.
7. Last scanned location is saved in the database every time visitor scans.
8. Once the system time is 11:59 pm the status of visitor entries of that day must be updated 
as closed.
9. At all the security must be able to update the status column of any valid/entered visitor as 
closed.
Dashboard Requirements:
1. Host
a. Login Page
i. The employee must be able to enter Username and Password
ii. The login must be LDAP compatible. 
b. Home page
i. Active appointments: Appointments that are created by the host that are 
not closed.
ii. Today’s visitor information
c. Create New
i. Create a new Appointment for the visitor.
d. Pending Appointments (Approver
e. My appointments
i. all the appointments created by the user would be shown in this page.
2. Security/receptionist
a. Login Page
i. The employee must be able to enter Username and Password
ii. The login must be LDAP compatible. 
b. Home page.
i. Total Count
1. Today’s visitors (on click should show visitor details)
2. Expected visitors.
3. Checked in visitors.
ii. Quick links to child pages
1. Scan QR code
c. Appointment Details page
i. All appointments are filtered with a date.
1. All the details of the appointments (ie: approved?, filled Forms? 
Images?)
2. Should be able to edit the status of the appointment
3. Search for specific appointment by appointment id, visitor name, 
hostname
4. Manual override option for security if needed.
d. Scan QR code.
i. Use webcam to scan for the QR code and validate access & changes state to 
visited.
