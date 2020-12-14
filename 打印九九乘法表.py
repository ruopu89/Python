# for i in range(1, 10):
#     for j in range(i, 10):
#         # if i <= 1:
#         print("{}*{}={}\t".format(i,j,i*j), end=' ')
#     print("")

# for i in range(1, 10):
#     for j in range(1, 10):
#         if i <= j:
#             print("{}*{}={}\t".format(i,j,i*j), end=" ")
#     print("")
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}\t".format(j,i,i*j), end=" ")
    print(" ")
