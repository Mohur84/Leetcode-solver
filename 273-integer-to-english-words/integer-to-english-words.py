class Solution:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        below_20 = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        def convert(num):
            if num == 0:
                return ""
            if num < 20:
                return below_20[num]
            if num < 100:
                return tens[num // 10] + (
                    " " + below_20[num % 10] if num % 10 else ""
                )
            return (
                below_20[num // 100]
                + " Hundred"
                + (" " + convert(num % 100) if num % 100 else "")
            )
        result = []
        groups = [
            (1000000000, "Billion"),
            (1000000, "Million"),
            (1000, "Thousand"),
            (1, "")
        ]
        for value, name in groups:
            if num >= value:
                group = num // value
                num %= value
                result.append(convert(group))
                if name:
                    result.append(name)
        return " ".join(result)