class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        i=0
        ans=[]
        var=[]
        
        # temp=str(products[0])
        # print(temp[:2])
        
        while(i<len(searchWord)):
            var=[]
            for j in products:
                
                temp=str(j)
                # print(temp)
                if(temp[:i+1]==searchWord[:i+1]):
                    if(len(var)<3):
                        var.append(j)
                        # print(var)
                    else:
                        break
            ans.append(var)
            # print(ans)
            
            i+=1
        return ans

            