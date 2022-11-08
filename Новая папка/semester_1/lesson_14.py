def order_of_args(name,default,*args,sep="seperator",username,end = "\n",**kwargs):
    print(name,default,args,sep, username ,end,kwargs)

order_of_args("abbos",123,4,5,6, username="wsflo",end="not enter",email="dwfq@mail.ru",loot=[2,3])

def fun(*args, **kwargs):
    print(args, kwargs)
fun(2, 3, 4, [5], user={"name": "Ya"}, goal=("win fdkfk"))