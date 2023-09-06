class ContadorBase:
    def avanza_base(self, numero, base_1):
        
        base_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
        encoding = base_digits[:base_1]
    
        for num in range(int(str(numero), base=base_1) + 1):
            digits = []
            n = num
        
            while n:
                digits.append(encoding[n % base_1])
                n //= base_1
        
            if not digits:
                digits.append(encoding[0])
        
            numero_en_base = ''.join(reversed(digits))
            print(numero_en_base)

if __name__ == "__main__":
    a = ContadorBase()
    a.avanza_base(10, 2)

            
