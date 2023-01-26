from  SQLconnecion import Targil1
if __name__ == '__main__':
    fileLog= open("logSQL.txt",'w')
    fileLog.write('this is Log file\n')
    name_input = input("Enter your name:")
    t=Targil1()
    try:
        ID=t.returnID("name_input")
        order=t.returnOrder(ID)
        t.returnSum(order)
    except ValueError:
        t.writetoLog()
  

       
        
       
