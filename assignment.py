n = int(input())                  # Reading input from STDIN
maxMiss = 2
attendanceLog = [1] * (maxMiss+1)
attendanceLog[maxMiss] = 0

for i in range(1, n + 1):
    temp = [0] * (maxMiss+1)
    for j in range(maxMiss-1, -1, -1):
        temp[j] = attendanceLog[0] + attendanceLog[j + 1]

    temp, attendanceLog = attendanceLog, temp

validClass = attendanceLog[0]
lastDayMiss = temp[1]
print(validClass)
print(f"For {n} days: {lastDayMiss}/{validClass}")