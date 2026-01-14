#!/usr/bin/env python
# WhatsApp Expense Approval Bot - DEMO VERSION
# Simulates: WhatsApp → Expense Request → Manager Approval → Google Sheets

import pandas as pd
import json
from datetime import datetime

print("WhatsApp Expense Approval Bot Starting...")

# SIMULATE WhatsApp messages (Real bot receives these via webhook)
whatsapp_messages = [
    {"from": "employee_john", "message": "1500 Travel Delhi meeting", "timestamp": "2026-01-14 18:30"},
    {"from": "employee_jane", "message": "800 Meals client dinner", "timestamp": "2026-01-14 19:15"},
    {"from": "manager_boss", "message": "approve 1500", "timestamp": "2026-01-14 19:45"},
    {"from": "manager_boss", "message": "reject 800", "timestamp": "2026-01-14 20:00"}
]

# PARSE expense from WhatsApp message
def parse_expense(whatsapp_msg):
    parts = whatsapp_msg.split()
    amount = float(parts)
    category = parts
    details = " ".join(parts[2:])
    return {"amount": amount, "category": category, "details": details}

# PROCESS messages
expenses = []
for msg in whatsapp_messages:
    if "approve" in msg['message'] or "reject" in msg['message']:
        # Manager approval/reject
        amount = float(msg['message'].split())
        status = msg['message'].split()
        # Find matching expense
        for exp in expenses:
            if exp['amount'] == amount and exp['status'] == 'Pending':
                exp['status'] = status.title()
                exp['approved_by'] = msg['from']
                exp['approved_at'] = msg['timestamp']
    else:
        # Employee expense request
        expense = parse_expense(msg['message'])
        expense.update({
            'employee': msg['from'],
            'request_time': msg['timestamp'],
            'status': 'Pending'
        })
        expenses.append(expense)

# SAVE to "Google Sheets" (CSV demo)
df = pd.DataFrame(expenses)
df.to_csv('expense_approvals.csv', index=False)

print(f" rocessed {len(df)} expenses")
print("\n STATUS SUMMARY:")
print(df.groupby('status').size())
print("\n APPROVALS:")
print(df[df['status'] != 'Pending'][['employee', 'amount', 'category', 'status']])
