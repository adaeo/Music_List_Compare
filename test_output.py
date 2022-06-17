try:
  import sys, json
  if (sys.argv[1] == "-s"):
    # Function to calculate the sum of an array
    def arraysum(arr):
      return sum(arr)

    # Get CLI arguments and parse to json
    data = json.loads(sys.argv[2])

    # Get required field from data
    array = data['array']

    # Calculate result
    result = arraysum(array)

    # Print data in stringified to parse in node server
    newdata = {'sum': result}
    print(json.dumps(newdata))
  elif (sys.argv[1] == '-f'):
    # newdata = {'path': sys.argv[2]}
    # print(json.dumps(newdata))
    import pandas as pd

    path = sys.argv[2]
    dtf = pd.read_csv(path, header=None, sep='\t')

    newdata = {'path': path, 'dtf':dtf.to_csv(sep="\t")}
    print(json.dumps(newdata))
except Exception as e:
  print(e)