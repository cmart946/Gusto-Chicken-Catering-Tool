


#function for converting cooked pounds of chicken into uncooked (raw)
def cooked_to_raw(total_cooked):
      return total_cooked / .75 # 1.25 is the conversion factor from cooked to raw chicken pounds


#function for adding total raw pounds of chicken and then return number of cases.
def total_cases_needed(total_cooked):
      yield_percent = 0.75
      pounds_per_case = 40 

      total_raw = total_cooked / yield_percent 
      cases_needed = total_raw / pounds_per_case
      return cases_needed

