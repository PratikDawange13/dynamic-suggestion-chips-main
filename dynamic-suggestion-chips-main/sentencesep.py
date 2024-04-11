from chipgenrator import chipgenerator

def separator(res):
  chip1, chip2, chip3= str.split(res,",")
  #chip_parts = str.split(res, "\n")
  '''chip1 = chip_parts[0] if len(chip_parts) > 0 else ""
  chip2 = chip_parts[1] if len(chip_parts) > 1 else ""
  chip3 = chip_parts[2] if len(chip_parts) > 2 else ""
'''

  return chip1, chip2, chip3

