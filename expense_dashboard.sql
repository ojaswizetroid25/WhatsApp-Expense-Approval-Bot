-- WhatsApp Expense Approval Dashboard

-- 1. Manager Daily View (Pending Approvals)
SELECT employee, amount, category, request_time
FROM expense_approvals 
WHERE status = 'Pending'
ORDER BY request_time DESC;

-- 2. Approval Analytics
SELECT status, 
       COUNT(*) as count,
       SUM(amount) as total_value,
       AVG(amount) as avg_amount
FROM expense_approvals 
GROUP BY status;

-- 3. Category Breakdown
SELECT category,
       COUNT(*) as requests,
       SUM(CASE WHEN status='Approved' THEN amount ELSE 0 END) as approved_amount
FROM expense_approvals 
GROUP BY category;
