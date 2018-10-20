import logging
import riffl.validator
import riffl.utils
    
def main():
    # Set up the parser
    parser=riffl.utils.cmdline_args()
    args=parser.parse_args()

    # Set up the logger 
    riffl.utils.setup_logging(args.verbose)
    logger=logging.getLogger()
    logger.handlers = []
    ch=logging.StreamHandler()
    ch.setFormatter(riffl.utils.ColoredFormatter())
    logger.addHandler(ch)

    logger.info('Running RIFFL Checker on Input file')

    # Initiate check
    riffl.validator.load_and_validate(args.input, args.schema)

if __name__ == '__main__':
  main()
