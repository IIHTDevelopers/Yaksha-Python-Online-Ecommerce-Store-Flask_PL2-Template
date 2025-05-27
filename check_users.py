import sqlite3

conn = sqlite3.connect('store.db')
conn.row_factory = sqlite3.Row

print("All users in database:")
cursor = conn.execute('SELECT * FROM users')
users = cursor.fetchall()

for user in users:
    print(f"ID: {user['id']}, Username: '{user['username']}', Password: '{user['password']}'")

print(f"\nTotal users: {len(users)}")

conn.close()
