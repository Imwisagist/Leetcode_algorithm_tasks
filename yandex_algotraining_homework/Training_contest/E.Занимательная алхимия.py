# https://contest.yandex.ru/contest/50668/enter
# 14 Тест падает RE
# import os

# def canICraftPotions(path):
#     with open(path, 'r') as f:
#         firstLine = f.readline()
#         numberOfReceipts = int(firstLine) - 2 # bcz 1 - A, 2 - B

#         receipts = [[0], [1], [2]]

#         for _ in range(numberOfReceipts):
#             parts = f.readline().split()
#             temp = []
#             for i in range(1, len(parts)):
#                 temp.append(int(parts[i]))
#             receipts.append(temp)

#         secondLine = f.readline()
#         countOfQuestions = int(secondLine)

#         questions = []
#         for _ in range(countOfQuestions):
#             parts = f.readline().split()
#             temp = []
#             for i in range(len(parts)):
#                 temp.append(int(parts[i]))
#             questions.append(temp)

#     for i in range(3, len(receipts)):
#         current = receipts[i]
#         converted = convert(i, current, receipts)
#         if 0 in converted:
#             converted = [0]
#         receipts[i] = converted

#     return checkIngredients(receipts, questions)

# def checkIngredients(receipts, questions):
#     sb = ""
#     for i in range(len(questions)):
#         currentQuestion = questions[i]
#         potionNumber = currentQuestion[2]
#         requestedReceipt = receipts[potionNumber]
#         if 0 in requestedReceipt:
#             sb += "0"
#         else:
#             countA = currentQuestion[0]
#             countB = currentQuestion[1]
#             receiptRequest = compact(receipts[potionNumber])
#             if countA >= receiptRequest[0] and countB >= receiptRequest[1]:
#                 sb += "1"
#             else:
#                 sb += "0"
#     return sb

# def compact(integers):
#     sumA = 0
#     sumB = 0
#     for i in integers:
#         if i % 2 == 0:
#             sumB += 1
#         else:
#             sumA += 1
#     return [sumA, sumB]

# def convert(i, current, receipts):
#     if 0 in current:
#         return [0]
#     result = []
#     for j in range(len(current)):
#         cur = current[j]
#         if cur < 3:
#             result.append(cur)
#         else:
#             toCall = receipts[cur]
#             if i in toCall or 0 in toCall:
#                 return [0]
#             else:
#                 result += convert(cur, receipts[cur], receipts)
#     return result

# path = os.path.join(os.getcwd(), "input.txt")
# print(canICraftPotions(path))
