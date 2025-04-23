# Analyse the DUT verilog files
# 1> generate rfuzz harness to fuzzing method
# 2> generate explicit signal prompt to LLM method

from __future__ import absolute_import, print_function

import json
import os
import sys

# the next line can be removed after installation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import pyverilog
# from pyverilog.dataflow.dataflow_analyzer import VerilogDataflowAnalyzer


def main():

    test_file = "testbench.json"
    datas = []
    try:
        with open(test_file, "r") as f:
            # 尝试读取整个文件作为一个JSON对象
            datas = json.load(f)
    except json.JSONDecodeError:
        try:
            # 如果上面失败，尝试按行读取JSON
            with open(test_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:  # 跳过空行
                        data = json.loads(line)
                        datas.append(data)
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return

    ###############################################
    # Generate Harness with JSON testbench
    ###############################################
    cpp_code = """
#include "rfuzz-harness.h"
#include <vector>
#include <string>
#include <memory>
#include <iostream>
#include <verilated.h>
#include "Vtop_module.h"

int fuzz_poke() {
    VerilatedContext* contextp;
    Vtop_module* top;
"""

    for name, value in datas[0]["input variable"][0].items():

        if name == "clock cycles":
            continue
        else:
            if len(value[0]) > 16:
                # print("input",name,value)
                # 对于大数值，使用 VL_WORDS_I 处理
                cpp_code += (
                    f"""   VlWide<{int(((len(value)/4) + 7) // 8)}> {name}_wide;\n"""
                )
    context_idx = 0
    for name, value in datas[0]["output variable"][0].items():

        if name == "clock cycles":
            continue
        else:

            if len(value[0]) > 16:
                #print("output", name, value)
                # 对于大数值，使用 VL_WORDS_I 处理
                cpp_code += (
                    f"""   VlWide<{int(((len(value)/4) + 7) // 8)}> {name}_wide;\n"""
                )
    cpp_code += f"""        int unpass = 0;\n"""
    for data in datas:
        cpp_code += f"""       ////////////////////////////scenario {data['scenario']}////////////////////////////\n"""

        stimulus = data["input variable"]
        expected = data["output variable"]


        cpp_code += f"""        unpass = 0;\n"""
        
        for i, input in enumerate(stimulus):
            clock_cycles = input["clock cycles"]
            # Create a new VerilatedContext for each top
            cpp_code += """    const std::unique_ptr<VerilatedContext> contextp_%d {new VerilatedContext};\n""" % (context_idx)
            cpp_code += """    contextp = contextp_%d.get();\n""" % (context_idx)
            context_idx += 1
            # 单独使用DUT
            # if(i == 0):
            #     cpp_code += f"""    Vtop_module* top = new Vtop_module;\n"""
            # else:
            cpp_code += f"""    top = new Vtop_module;\n"""
            cpp_code += f"""    top->clk = 0;\n"""
            
            # 将top中的output变量全部清空  ----------------------------
            for name, value in expected[i].items():
                if name == "clock cycles":
                    continue
                else:
                    if isinstance(value[0], str) and len(value[0]) > 16:
                        cpp_code += f"""        for (int word_idx = 0; word_idx < {int(((len(value[0])/4) + 7) // 8)}; word_idx++) {{
                                    {name}_wide[word_idx] = 0x0;
                                }}
                                top->{name} = {name}_wide;
                        """
                    else:
                        cpp_code += f"""        top->{name} = 0x0;\n"""
            # ------------------------------------------------


            cpp_code += f"""        top->clk = 1;\n"""
        
            

            # input 中除了clock cycles 之外的变量
            input_vars = {k: v for k, v in input.items() if k != "clock cycles"}
            check = """printf("input_vars:\\n");\n"""
            for name, value in input_vars.items():
                check += f"""printf("top->%s = 0x%x\\n", "{name}", top->{name});\n"""
            check += "\n"
            for j in range(clock_cycles):
                cpp_code += """        contextp->timeInc(1);  \n"""
            

                cpp_code += f"""        top->clk = !top->clk;\n"""
                cpp_code += """         top->eval();\n"""
                cpp_code += """         contextp->timeInc(1);\n"""
                cpp_code += f"""        top->clk = !top->clk;\n"""

                
                for name, value in input_vars.items():

                    temp = str(value[j])
                    hex_len = (len(temp) + 3) // 4  # 计算需要的十六进制位数
                    hex_value = hex(int(temp, 2))[2:].zfill(hex_len)
                    if len(str(value[j])) <= 32:
                        cpp_code += f"""        top->{name} = 0x{hex_value};\n"""
                    else:

                        
                        #print("hex_value",hex_value)
                        
                        for m in range(0, len(hex_value), 8):
                                segment = hex_value[
                                    max(0, len(hex_value) - m - 8) : len(hex_value) - m
                                ]
                                if segment:
                                    cpp_code += f"""        {name}_wide[{m//8}] = 0x{segment};\n"""

                
                
                cpp_code += """        top->eval();\n"""
                for name, value in expected[i].items():
                    if name == "clock cycles":
                        continue
                    else:
                        
                        temp = str(value[j])
                        hex_len = (len(temp) + 3) // 4  # 计算需要的十六进制位数
                        hex_value = hex(int(temp, 2))[2:].zfill(hex_len)
                        if len(str(value[j])) <= 32:
                            #print("value",str(value[j]))
                            
                            cpp_code += f"""        if (top->{name} != 0x{hex_value}) {{
            unpass++;\n"""
                            #cpp_code += f"""        if (1) {{
            #unpass++;\n"""
                            cpp_code += check
                            cpp_code += f"""            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\\n", {j},{clock_cycles}, "{name}", top->{name}, 0x{hex_value});\n"""
                            cpp_code += f"""        }}\n"""

                        else:
                            
                            temp = str(value[j])
                            hex_len = (len(temp) + 3) // 4  # 计算需要的十六进制位数
                            hex_value = hex(int(temp, 2))[2:].zfill(hex_len)
                            
                            for m in range(0, len(hex_value), 8):
                                segment = hex_value[
                                    max(0, len(hex_value) - m - 8) : len(hex_value) - m
                                ]
                                if segment:
                                    cpp_code += f"""        {name}_wide[{m//8}] = 0x{segment};\n"""
                            
                            cpp_code += f"""        if (top->{name} != {name}_wide) {{
            unpass++;
            {check}
            printf("At %d clock cycle of %d, wide value mismatch for %s\\n", {j}, {clock_cycles}, "{name}");
        }}\n"""

            

            #cpp_code += f"""        top->final();"""
            #cpp_code += f"""        top = new Vtop_module;"""
                
                
                

        cpp_code += f"""

        if (unpass == 0) {{
            std::cout << "Test passed for scenario {data['scenario']}" << std::endl;
        }} else {{
            std::cout << "Test failed,unpass = " << unpass << " for scenario {data['scenario']}" << std::endl;
        }}
"""

    cpp_code += """
    return unpass;
}
"""

    with open("rfuzz-harness.cpp", "w") as file:
        file.write(cpp_code)


if __name__ == "__main__":
    main()
