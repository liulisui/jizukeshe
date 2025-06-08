# filepath: c:\Users\liuli\Desktop\计组课设\2.py

def convert_binary_to_hex(binary_str):
    """
    将24位二进制字符串转换为6位十六进制
    """
    # 确保输入是24位
    binary_str = binary_str.strip()
    if len(binary_str) != 24:
        # 如果不是24位，补全或截取到24位
        if len(binary_str) < 24:
            binary_str = binary_str.zfill(24)  # 在左侧填充0
        else:
            binary_str = binary_str[:24]  # 截取前24位
    
    # 将二进制转换为整数，然后转换为十六进制（去掉前缀0x）
    decimal_value = int(binary_str, 2)
    hex_value = hex(decimal_value)[2:]
    
    # 确保十六进制结果是6位长
    hex_value = hex_value.zfill(6)  # 在左侧填充0，确保6位长度
    
    return hex_value.upper()  # 返回大写的十六进制字符串

def main():
    try:
        # 打开输入文件
        with open('in.txt', 'r') as infile:
            # 创建输出文件
            with open('out.txt', 'w') as outfile:
                # 逐行读取并处理
                for line in infile:
                    # 跳过空行
                    if not line.strip():
                        continue
                    
                    # 转换为十六进制
                    hex_value = convert_binary_to_hex(line)
                    
                    # 写入输出文件
                    outfile.write(hex_value + '\n')
        
        print("转换完成！结果已保存到out.txt")
    except FileNotFoundError:
        print("错误：找不到输入文件 in.txt")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()