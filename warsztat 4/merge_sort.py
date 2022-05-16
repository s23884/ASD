def merge_sort(BBB):

    if len(BBB) > 1:

        C = len(BBB)//2
        

        left = BBB[:C]

        right = BBB[C:]

        

        merge_sort(left)

        merge_sort(right)
        

        b = c = d = 0

        while b < len(left) and c < len(right):

            if left[b] < right[c]:

                BBB[d] = left[b]

                b += 1

            else:

                BBB[d] = right[c]

                c += 1

            d += 1

        while b < len(left):

            BBB[d] = left[b]

            b += 1

            d += 1

        while c < len(right):

            BBB[d] = right[c]

            c += 1

            d += 1
            

if __name__ == '__main__':

    tabela1 = [0,1,3,5,7,9,2,4,6,8]
    tabela2 = [6,7,22,34,55,60,5,40,55,1,3]

    merge_sort(tabela1)
    merge_sort(tabela2)
    print(tabela1)
    print(tabela2)


            
