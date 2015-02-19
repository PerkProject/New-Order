__author__ = "Nick Demyanchuk"

import sys

import logging
import itertools

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ALLOWED_CHARS = ("1", "2", "X")

def main(filename):
    already_processed = list()

    with open(filepath) as f:
        with open('output.txt', 'w') as result_fp:
            for line in f:
                # Get latest element - our digits set
                maybe_number = line.split('|')[-1].strip()
                # Remove semicolons
                maybe_number = maybe_number.replace(';', '')

                if not len(maybe_number) == 14:
                    continue

                if any(itertools.imap(lambda n: n not in ALLOWED_CHARS, maybe_number)):
                    # Unknown character detected
                    continue

                if not maybe_number in already_processed:
                    already_processed.append(maybe_number)
                    result_fp.write(maybe_number + "\n")

if __name__ == "__main__":
    filepath = len(sys.argv) > 1 and sys.argv[1] or "2748373.txt"
    main(filepath)