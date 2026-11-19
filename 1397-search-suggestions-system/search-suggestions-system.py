class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result=[]
        prefix=""
        for ch in searchWord:
            prefix+=ch
            suggestions=[]
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                if len(suggestions)==3:
                    break
            result.append(suggestions)
        return result