import re

# Email regex pattern (matches most common email formats)
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

# Function to find all emails in text
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)

# Function to validate a single email
def is_valid_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None


# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    
    text = """
    Contact us at support@example.com
    or sales.team@company.co.in
    Invalid ones: @missing.com, user@.com
    """

    # Find emails
    emails = find_emails(text)
    print("Found Emails:")
    for e in emails:
        print(e)

    # Validate example
    test_email = "john.doe@gmail.com"
    print("\nIs valid email?", is_valid_email(test_email))