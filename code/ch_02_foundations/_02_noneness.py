import _02_noneness_support_file as db
def find_accounts(search_text):
    # perform search...
    if not db.is_available:
        return None

    # returns a list of account IDs
    return db.search(search_text)

accounts = find_accounts('python')
if accounts is None:
    print("Error: DB not available")
else:
    print("Accounts found: Would list them here...")
























