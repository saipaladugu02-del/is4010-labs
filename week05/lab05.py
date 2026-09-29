def calculate_average_age(users):
    """Return the average of valid numeric ages, or 0.0 if there are none.

    Users whose age is missing or not a number (for example "unknown")
    are skipped.
    """
    ages = []
    for user in users:
        age = user.get("age")
        if isinstance(age, (int, float)):
            ages.append(age)
    try:
        return sum(ages) / len(ages)
    except ZeroDivisionError:
        return 0.0

def get_active_user_emails(users):
    """Return the email addresses of users who are active.

    A user is included only when "is_active" is truthy and an "email"
    key exists.
    """
    emails = []
    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])
    return emails
