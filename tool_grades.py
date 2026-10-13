def run():
  """ Input a list of grades and display the average, lowest, highest and mention"""
  input_grade = ' '
  grades = []
  while True:
    input_text = input("Enter a grade (empty to stop): ")
    if input_text == '':
      break
    try:
      input_grade = int(input_text)
    except ValueError:
      input_grade = -1
    if 0 <= input_grade <= 20:
      grades.append(input_grade)
    else:
      print('Please input a value between 0 and 20')

  if len(grades) > 0:
    print(f'{len(grades)} grades – average: {sum(grades)/len(grades):.1f} – lowest: {min(grades):.1f} – highest: {max(grades):.1f}\nMention: {get_mention(grades)}')
  else:
    print("No grades were entered.")

def get_mention(grades: list) -> str:
  """
  Get the mention of a list of grades

  :param grades: the list of grades
  :return: the resulting mention
  """
  
  average = sum(grades)/len(grades)
  if average > 15:
    return 'Very Good'
  if average > 13:
    return 'Good'
  if average > 9:
    return 'Pass'
  return 'Fail'

if __name__ == "__main__":
  run()