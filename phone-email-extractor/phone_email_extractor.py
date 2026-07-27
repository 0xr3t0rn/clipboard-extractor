import pyperclip
import re

# Phone number regex. (e.g +10 9123456789 or 09123456789)
phone_regex = re.compile(r'''(
    (\+\d{2}\s?|0)                         # Country code
    \d{10}                                 # Last 10 digits
)''', re.VERBOSE)

# Email address regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                      # username
    @                                      # @ symbol
    [a-zA-Z0-9.-]+                         # domain name
    (\.[a-zA-Z]{2,4})                      # dot-something (e.g .com)
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    matches.append(groups[0])
for groups in email_regex.findall(text):
    matches.append(groups[0])
    
# Copy result to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')