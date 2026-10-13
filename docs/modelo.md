## users 
- user_id (INTEGER) PK
- full_name (TEXT)
- email (TEXT)
- created_at (TIMESTAMP)

## pools
- pool_id (INTEGER) PK
- owner_id (INTEGER) FK -> users.user_id
- pool_name (TEXT)
- goal_cents (INTEGER)
- status (TEXT)
- created_at (TIMESTAMP)
- due_at (TIMESTAMP)

## contributions
- contribution_id (INTEGER) PK
- user_id (INTEGER) FK -> users.user_id
- amount_cents (INTEGER)
- pool_id (INTEGER) FK -> pools.pool_id
- status (TEXT) --PENDING, COMPLETED, FAILED
- created_at (TIMESTAMP)

## payouts
- payout_id (INTEGER) PK
- pool_id (INTEGER) FK -> pools.pool_id
- recipient_id (INTEGER) FK -> users.user_id
- amount_cents (INTEGER)
- status (TEXT) -- PENDING, COMPLETED, FAILED
- created_at (TIMESTAMP)
- due_at (TIMESTAMP)
- paid_at (TIMESTAMP)