def main():
    # 接收十六进制输入
    hex_input = input("请输入一个两位十六进制数（例如：3F）：")
    
    # 将十六进制转换为整数
    decimal_value = int(hex_input, 16)
    
    # 将整数转换为8位二进制，去掉'0b'前缀
    binary_a = format(decimal_value, '08b')
    
    print(f"输入的十六进制数 {hex_input} 转换为二进制A为: {binary_a}")
    
    # 检查A的高二位是否都是1
    if binary_a[0:2] == "11":
        # B的高四位固定为0011
        # B的低四位：1-2位来自A的3-4位，3-4位为1
        binary_b = "0011" + binary_a[2:4] + "11"
    else:
        # B的高四位固定为0011
        # B的低四位是A的高四位
        binary_b = "0011" + binary_a[0:4]
    
    print(f"生成的二进制数B为: {binary_b}")
    
    # 将B转换回十六进制以便查看
    hex_b = format(int(binary_b, 2), 'X')
    print(f"B对应的十六进制表示: {hex_b}")

if __name__ == "__main__":
    main()