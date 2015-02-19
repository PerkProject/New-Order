__author__ = "Nick Demyanchuk"

import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ALLOWED_CHARS = ("1", "2", "X")

def main():
    already_processed = list()

    with open("2748373.txt") as f:
        with open('output.txt', 'w') as result_fp:
            for line in f:
                # Get latest element - our digits set
                maybe_number = line.split('|')[-1].strip()
                # Remove semicolons
                maybe_number = maybe_number.replace(';', '')

                if not len(maybe_number) == 14:
                    logger.info("Number length of {} is not 14 symbols".format(maybe_number))
                    continue

                if not all(map(lambda n: n in ALLOWED_CHARS, maybe_number)):
                    # Unknown character detected
                    logger.info("Unknown characters detected in {}".format(maybe_number))
                    continue

                if not maybe_number in already_processed:
                    already_processed.append(maybe_number)
                    result_fp.write(line)
                else:
                    logger.info('{} has already been processed'.format(maybe_number))


if __name__ == "__main__":
    main()