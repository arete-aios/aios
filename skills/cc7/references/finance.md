# Finance · a private financial snapshot

Parent: [CC7 Command Center](command-center.md). Portable workspace recipe,
2026-11-13. The public Nora example uses invented EUR figures only.

Use the owner's approved accounting exports or existing reports as authority.
Agree which aggregates may appear and who can see the page. If the constitution
excludes financial data from dashboards, retain that boundary and show only a
link to the private accounting report until the owner approves a different view.

Keep periods and concepts distinct:

- Cash collected and cash paid cover the same explicitly stated period.
- Net cash flow = cash collected minus cash paid; it is not accounting profit.
- Unpaid invoices and ageing use a separately stated as-of date; an invoice is
  not a cash receipt. Use agreed due dates to determine overdue status.
- A forecast is a proposal, separate from observed data. Missing data is unknown,
  not zero; label partial periods and incomplete exports.

Reconcile totals to the source before drawing charts. Show the period, currency,
refresh/check date and source. For invoices prefer aggregate ageing buckets and
one owner-approved next action; raw bank/account details and individual records
stay in their authoritative private system. Never add account connections,
payments, filings or automated chasing while building a view.

Test with synthetic figures: collected 12,400, paid 7,300, net 5,100; unpaid
invoices 3,800 = 3,200 within terms + 600 overdue. Verify that an absent export
shows unknown and does not produce a misleading green status. Read the saved
page back and check one source link before calling it ready.

Design reference: ERPNext's Payments dashboard separates incoming/outgoing
payments and receivable/payable ageing:
https://github.com/frappe/erpnext/blob/develop/erpnext/accounts/accounts_dashboard/payments/payments.json
This is a layout reference; no ERPNext code, connector or account is installed.
