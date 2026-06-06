def dedupe_emails(emails):

    seen = set()
    unique = []

    for email in emails:

        if email.email not in seen:

            seen.add(email.email)
            unique.append(email)

    return unique