import sqlite3

def login_vulnerable(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # VULNERABLE: Direct string interpolation bypasses query structure
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    cursor.execute(query)
    return cursor.fetchone()
print "finished"
print "another check"
print "another check2"
print "another check3"