class Product:
    def __init__(self,pId,pName,pPrice,pCategory):
        self.pId=pId
        self.pName=pName
        self.pPrice=pPrice
        self.pCategory=pCategory

class ProductApp:
    def __init__(self):
        self.product=[]

    def addProduct(self,pro):
        self.product.append(pro)
        print("Product is added successfully")

    def updateProduct(self,pId,newName=None,newPrice=None,newCategory=None):
        for product in self.product:
            if product.pId==pId:
                if newName:
                    product.pName=newName
                if newPrice:
                    product.pPrice=newPrice
                if newCategory:
                    product.pCategory=newCategory
                print("Updated successfully....")
                return
        print("Product not found")

    def deleteProduct(self,pId):
        for i,product in enumerate(self.product):
            if product.pId==pId:
                del self.product[i]
                print("Product deleted")
                return
        print("Product not found")
    
    def getProductBypId(self,pid):
        for pro in self.product:
                if pro.pId==pid:           
                    return pro
        print("product not found")
        return None

    def getAllProduct(self):
        return self.product
    
    def getProductByCategory(self,category):
        p=[]
        for pro in self.product:
                if pro.pCategory==category:
                    p.append(pro)
        return p
        print("product not found")
        return None
    
    def getProductsBtwPrices(self,min,max):
        p=[]
        for q in self.product:
            if(min<=q.pPrice<=max):
                p.append(q)
        return p

if __name__=="__main__":
        
        flag=True
        obj=ProductApp()
        while(flag):
            
            print("choose any one of the operation")
            print("1.Add Product\n2.Update Product\n3.Delete Product\n4.Get Product by PId\n5.Get all products\n6.Get all products by category\n7.Get product between prices\n8.exit")
            n=int(input())
            if (n<=8 and n>=1):

                if n==1:
                    pName=input("enter product name:")
                    pPrice=int(input("enter price:"))
                    pCategory=input("enter the product category:")
                    pId=int(input("enter product Id:"))
                    p= Product(pId,pName,pPrice,pCategory)
                    obj.addProduct(p)
                    print("data entered successfully\n")
                if n==2:
                        id=int(input("enter product ID"))
                        nn=input("enter new name")
                        np=input("enter new price")
                        nc=input("enter new category")
                        obj.updateProduct(pId=id,newName=nn,newPrice=np,newCategory=nc)
                if n==3:
                    pId=int(input("enter the id:"))
                    obj.deleteProduct(pId)
                
                if n==4:
                    search=int(input("enter the id:"))
                    found=obj.getProductBypId(search)
                    if found:
                        print(f"product id: {found.pId}")
                        print(f"product name: {found.pName}")
                        print(f"product category: {found.pCategory}")
                        print(f"product price: {found.pPrice}")
                        print('\n')
                if n==5:
                    res=obj.getAllProduct()
                    print("total number of products:",len(res))
                    for found in res:
                        print('\n')
                        print(f"product id: {found.pId}")
                        print(f"product name: {found.pName}")
                        print(f"product category: {found.pCategory}")
                        print(f"product price: {found.pPrice}")
                if n==6:
                    category=input("enter the category")
                    found=obj.getProductByCategory(category)
                    for item in found:
                        print('\n')
                        print(f"product id: {item.pId}")
                        print(f"product name: {item.pName}")
                        print(f"product category: {item.pCategory}")
                        print(f"product price: {item.pPrice}")
                        print('\n')
                if n==7:
                    min=int(input("enter the min range"))
                    max=int(input("enter the max range"))
                    lis=obj.getProductsBtwPrices(min,max)
                    for l in lis:
                        print('\n')
                        print(f"product id: {l.pId}")
                        print(f"product name: {l.pName}")
                        print(f"product category: {l.pCategory}")
                        print(f"product price: {l.pPrice}")
                        print('\n')
                      
                if(n==8):
                    print("\nsee you again !!!")
                    flag=False
                else:

                    print("\nchoose valid number")  



