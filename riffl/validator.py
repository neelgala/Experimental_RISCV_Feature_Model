"""
  Validation functions for input yaml file
"""

from cerberus import Validator
import oyaml as yaml
import sys
import os
import re
import logging

logger= logging.getLogger(__name__)

def specific_checks(foo):

  if foo['MISA_D']:
    if not foo['MISA_F']:
      logger.error('MISA_D set without setting MISA_F')
      sys.exit(0)

def load_and_validate(foo, schema):
  
    """
      Read the input foo (yaml file) and validate with schema for feature values
      and constraints
    """
    inputfile=open(foo,'r')
    schemafile=open(schema,'r')
    # Load input YAML file
    logger.info('Loading input file: '+str(foo))
    inp_yaml=yaml.safe_load(inputfile)


    # instantiate validator
    logger.info('Load Schema '+str(schema))
    schema_yaml=yaml.safe_load(schemafile)
    validator=Validator(schema_yaml)
    validator.allow_unknown = True
    normalized=validator.normalized(inp_yaml,schema_yaml)

    # Perform Validation
    logger.info('Initiating Validation')
    valid=validator.validate(inp_yaml)
    # Print out errors
    if valid:
      logger.info('Input file has no errors. :)')
    else:
      logger.error(validator.errors)
      sys.exit(0)

    
    specific_checks(normalized)

    logger.info('Dumping out Normalized Checked YAML')
    file_name_split=foo.split('.')
    outfile=open(file_name_split[0]+'_checked.'+file_name_split[1],'w')
    yaml.dump(normalized, outfile, default_flow_style=False, allow_unicode=True)
