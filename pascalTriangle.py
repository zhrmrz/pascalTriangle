class sol:
    def pascalTriangle(self,numRows):
        list=[[1]]
        row=[1]
        for i in range(numRows):
            row=[1]+[row[i]+row[i+1] for i in range(len(row)-1)]+[1]
            list.append(row)
        print(list)
p1=sol()
p1.pascalTriangle(4)
