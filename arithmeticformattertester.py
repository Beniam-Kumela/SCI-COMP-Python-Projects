def arithmetic_arranger(problems, solve = False):
  line1 = ''
  line2 = ''
  line3 = ''
  dashes = ''
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    firstnum = problem.split()[0]
    operand = problem.split()[1]
    secondnum = problem.split()[2]
    if len(firstnum) > 4 or len(secondnum) > 4 :
      return "Error: Numbers cannot be more than four digits."
    if firstnum.isnumeric() is False or secondnum.isnumeric() is False:
      return "Error: Numbers must only contain digits."
    if operand == "+":
      sumnum = str(int(firstnum)+int(secondnum))
    if operand == "-":
      sumnum = str(int(firstnum)-int(secondnum))
    if operand not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    if len(firstnum) > len(secondnum):
        length = 2 + len(firstnum)
    if len(firstnum) == len(secondnum):
        length = 2 + len(firstnum)
    if len(firstnum) < len(secondnum):
        length = 2 + len(secondnum)
    firstline = firstnum.rjust(length)
    secondline = operand + secondnum.rjust(length - 1)
    thirdline = ('-'*length)
    fourthline = sumnum.rjust(length)
    if problem != problems[-1]:
      line1 += firstline + "    "
      line2 += secondline + "    "
      dashes += thirdline + "    "
      line3 += fourthline + "    "
    else:
      line1 += firstline
      line2 += secondline
      dashes += thirdline
      line3 += fourthline
  line1.rstrip()
  line2.rstrip()
  dashes.rstrip()
  line3.rstrip()
  if solve:
    arranged_problems = line1 + "\n" + line2 + "\n" + dashes + "\n" + line3
  else:
    arranged_problems = line1 + "\n" + line2 + "\n" + dashes
  return arranged_problems
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
