import math
import itertools
import re

def solve(exp):
    # Hàm kiểm tra biểu thức có hợp lệ hay không
    # eval() để tính giá trị của biểu thức dạng string trả về int
    # nếu eval() trả về lỗi thì return None
    def check_expression(expr):
        try:
            return eval(expr)
        except:
            return None

    # Phân tách biểu thức thành 2 phía    
    lExp, rExp = exp.split("=")
    rExp = int(rExp.strip())

    # Tìm tất cả các vị trí có dấu "?"
    possiblePos = [i for i, c in enumerate(exp) if c == "?"]

    # Tạo tất cả các kết hợp có thể từ 0-9 +-*/ cho các vị trí "?"
    for combination in itertools.product("0123456789+-*/", repeat=len(possiblePos)):
        

def main():
    for _ in range(int(input())):
        s = input()
        print(solve(s))

if __name__ == "__main__":
    main()