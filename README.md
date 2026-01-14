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

Project Structure
text
whatsapp-expense-approval-bot/
├── whatsapp_expense_bot.py      # Main demo script

├── requirements.txt             # Python dependencies

├── README.md                    # Project documentation

├── expense_approvals.csv        # Auto-generated "Google Sheet" (after running)

└── expense_dashboard.sql        # Sample SQL queries for analytics

## Run Demo
```bash
pip install -r requirements.txt
python whatsapp_expense_bot.py.

