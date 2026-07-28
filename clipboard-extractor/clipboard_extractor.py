import re
import pyperclip


class ClipboardScanner:
    def __init__(self):
        self.phone_regex = re.compile(r'''
            (?:\+\d{2}\s?|0)\d{10}
        ''', re.VERBOSE)

        self.email_regex = re.compile(r'''
            [a-zA-Z0-9._%+-]+
            @
            [a-zA-Z0-9.-]+
            \.[a-zA-Z]{2,}
        ''', re.VERBOSE)

        self.url_regex = re.compile(r'''
            https?://\S+
        ''', re.VERBOSE)

    def find_matches(self, text):
        matches = []
        for regex in (self.phone_regex, self.email_regex, self.url_regex):
            matches.extend(regex.findall(text))
        return matches

    def copy_matches(self):
        text = pyperclip.paste()
        matches = self.find_matches(text)

        if matches:
            result = '\n'.join(matches)
            pyperclip.copy(result)
            print('Copied to clipboard:')
            print(result)
        else:
            print('No phone numbers, email addresses, or URLs found.')


if __name__ == "__main__":
    scanner = ClipboardScanner()
    scanner.copy_matches()
