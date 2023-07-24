def CountMonth(idCards):
        d={}
        for sid in idCards:
                month=int(sid[10:12:1])
                if month in d:
                        d[month]+=1
                else:
                        d[month]=1
        L=list(tuple(items for items in d.items()))
        L.sort(key=lambda x:x[0])

        return L
def main():
        IDS=['310107199401231242','31010719940502913X','310107199702012190','310107199104016896',
     '310107199909029846','310107199608013285','310107199612122345','310107199908017384',
     '31010719930302774X','310107199703030489','310107199306030821','310107199703018594']

        Lcount=CountMonth(IDS)
        for month,count in Lcount:
                print("{}月\t{}人".format(month,count))

main()
