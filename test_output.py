try:
  import sys, json
  # Function to calculate the sum of an array
  def arraysum(arr):
    return sum(arr)

  # Get CLI arguments and parse to json
  data = json.loads(sys.argv[1])

  # Get required field from data
  array = data['array']

  # Calculate result
  result = arraysum(array)

  # Print data in stringified to parse in node server
  newdata = {'sum': result}
  print(json.dumps(newdata))
except Exception as e:
  print(e)