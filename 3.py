def hex_to_binary(hex_str):
    """将两位十六进制字符串转换为8位二进制字符串"""
    decimal_value = int(hex_str, 16)
    binary_str = format(decimal_value, '08b')
    return binary_str

def process_code_file(input_file, output_file):
    """处理code.txt文件并输出到code_out.txt"""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    # 去除行末换行符但保留原始格式
                    original_line = line.rstrip('\n')
                    
                    # 如果是空行或以分号开头的注释行，直接输出
                    if not original_line.strip() or original_line.strip().startswith(';'):
                        outfile.write(original_line + '\n')
                        continue
                    
                    # 处理包含十六进制数据的行
                    parts = original_line.split()
                    if len(parts) >= 2:
                        # 获取前两个十六进制字符
                        hex1 = parts[0]
                        hex2 = parts[1]
                        
                        # 转换为二进制
                        try:
                            binary1 = hex_to_binary(hex1)
                            binary2 = hex_to_binary(hex2)
                            
                            # 获取剩余内容（从第二个空格之后开始）
                            remaining_content = ""
                            if len(parts) > 2:
                                # 找到第二个十六进制数之后的内容
                                first_hex_end = original_line.find(hex1) + len(hex1)
                                second_hex_start = original_line.find(hex2, first_hex_end)
                                second_hex_end = second_hex_start + len(hex2)
                                remaining_content = original_line[second_hex_end:]
                            
                            # 合并输出：两个8位二进制 + 剩余内容
                            output_line = binary1 + binary2 + remaining_content
                            outfile.write(output_line + '\n')
                            
                        except ValueError:
                            # 如果转换失败，输出原始行
                            outfile.write(original_line + '\n')
                    else:
                        # 如果格式不符合预期，输出原始行
                        outfile.write(original_line + '\n')
                        
        print(f"处理完成！结果已保存到 {output_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}")
    except Exception as e:
        print(f"处理过程中出现错误：{e}")

if __name__ == "__main__":
    input_filename = "code.txt"
    output_filename = "code_out.txt"
    
    print("开始处理code.txt文件...")
    process_code_file(input_filename, output_filename)