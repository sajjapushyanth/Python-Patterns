
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#############################################################


# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#####################################################################
# * * * * *
# * * * *
# * * *
# * *
# *
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


#####################################################################
 #     *
 #    **
 #   ***
 #  ****
 # *****
#
# n=5
#
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


#####################################################################
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# n=5
# for i in range(n):
#
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

#####################################################################
  #         *
  #       * * *
  #     * * * * *
  #   * * * * * * *
  # * * * * * * * * *

# n=4
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


#####################################################################

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
#################################################################
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n=5
#
# for i in range(n):
#     for j in range(i,n):
#         print(end=" ")
#
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
###################################################################
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# * * * *
#   * * * *
#     * * * *
#       * * * *
# n=4
# for i in range(n):
#     for j in range(i,n):
#         print(end=" ")
#     for j in range(n):
#         print("*",end=" ")
#     print()



##########################################################################
#    *
#   * *
#  *   *
# *******
# row = 4
#
# for i in range(row):
#     for j in range(i+1,row):
#         # prints left space in the same row
#         print(' ', end='')
#
#     for j in range(2 * i + 1):
#
#         # printing the left boundary of triangle
#         if j == 0 or j == 2 * i or i == row - 1:
#             print('*', end='')
#
#         # printing spaces in the middle of the triangle
#         else:
#             print(' ', end='')
#
#     print()
#####################################3
# 10 9 8 7
# 6 5 4
# 3 2
# 1
#
# n=4
# p=10
# for i in range(n):
#     for j in range(i,n):
#         print(p,end=" ")
#
#
#         p-=1
#     print()
############################################################################3

# 1 * 2 * 3 * 4
# 5 * 6 * 7 * 8
# 9 * 10 * 11 * 12
# 13 * 14 * 15 * 16
# n=4
# p=0
# for i in range(n):
#
#
#     for j in range(n):
#         p+=1
#         if j==n-1:
#             print(p,end=" ")
#
#         else:
#             print(p,"*",end=" ")
#
#     print()
###############################################################################
# 1
# 2 3 2
# 3 4 5 4 3
# 4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5
# n=5
# for i in range(n):
#     x=i+1
#     for j in range(2*n-1):
#         if(i+j<n-1 or i+j>=n+2*i):
#             print(" ",end=" ")
#         else:
#             print(x,end=" ")
#             if(j<n-1):
#                 x+=1
#             else:
#                 x-=1
#     print()
########################################################################################
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()