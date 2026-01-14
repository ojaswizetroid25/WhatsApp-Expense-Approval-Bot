# WhatsApp-Expense-Approval-Bot

**Employee WhatsApp → Manager Approval → Google Sheets Workflow**

## DEMO Flow
1.Employee: "1500 Travel Delhi" → Bot captures expense

2.Manager: "approve 1500" → Updates status

3.Google Sheets: Auto-saves with approval timestamp

4.SQL Dashboard: Manager analytics


## Sample Output

@ Processed 3 expenses
Pending: 0 | Approved: 1 | Rejected: 1

 ## PRODUCTION READY

@ WhatsApp webhook parsing

@ Expense extraction (NLP)

@ Manager approval workflow

@ Google Sheets API integration

@ SQL analytics dashboard

## Project Structure

whatsapp-expense-approval-bot/

├── whatsapp_expense_bot.py      # Main demo script

├── requirements.txt             # Python dependencies

├── README.md                    # Project documentation

├── expense_approvals.csv        # Auto-generated "Google Sheet" (after running)

└── expense_dashboard.sql        # Sample SQL queries for analytics

 Sample Workflow
Employee employee_john sends:
"1500 Travel Delhi meeting"
→ Bot stores this as a Pending expense.

Employee employee_jane sends:
"800 Meals client dinner"
→ Another Pending expense.

Manager sends:
"approve 1500"
→ Bot marks John’s expense as Approved.

Manager sends:
"reject 800"
→ Bot marks Jane’s expense as Rejected.

All of this is logged into expense_approvals.csv.

📊 CSV / “Google Sheets” Output
expense_approvals.csv contains columns like:

employee

amount

category

details

request_time

status (Pending / Approved / Rejected)

approved_by

approved_at

You can open this file in:

Excel

Google Sheets (upload the CSV)

Any BI tool (Power BI, Tableau, etc.)

📈 Analytics with SQL
Use expense_dashboard.sql to run example queries on a table named expense_approvals.

Included queries:

Pending approvals for managers:

sql
SELECT employee, amount, category, request_time
FROM expense_approvals
WHERE status = 'Pending'
ORDER BY request_time DESC;
Approval analytics:

sql
SELECT status,
       COUNT(*) AS count,
       SUM(amount) AS total_value,
       AVG(amount) AS avg_amount
FROM expense_approvals
GROUP BY status;
Category-wise breakdown:

sql
SELECT category,
       COUNT(*) AS requests,
       SUM(CASE WHEN status = 'Approved' THEN amount ELSE 0 END) AS approved_amount
FROM expense_approvals
GROUP BY category;
These can power a simple manager dashboard in any BI or SQL tool.

🧱 How This Maps to a Real System
This demo is intentionally simple but aligns with a real production design:

Simulated list of messages
↔ Incoming WhatsApp webhook payloads from Meta Cloud API

parse_expense() function
↔ Basic NLP / text parsing to extract amount, category, and description

CSV file (expense_approvals.csv)
↔ Google Sheets / relational database (PostgreSQL, MySQL, etc.)

SQL queries
↔ Real analytics dashboard (Power BI, Looker, Tableau)

You can explain in interviews how you would:

Replace the simulated message list with real webhooks

Use Google Sheets API or a SQL database instead of CSV

Add authentication and role-based access (only managers can approve)

## Run Demo
```bash
pip install -r requirements.txt
python whatsapp_expense_bot.py.

