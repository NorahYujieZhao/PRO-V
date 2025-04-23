
#include "rfuzz-harness.h"
#include <vector>
#include <string>
#include <memory>
#include <iostream>
#include <verilated.h>
#include "Vtop_module.h"
#include <sstream>

int fuzz_poke() {
    int unpass = 0;
    VerilatedContext* contextp;
    Vtop_module* top;

    // Scenario: CD_000
    const std::unique_ptr<VerilatedContext> contextp_0 {new VerilatedContext};
    contextp = contextp_0.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x1) {
        unpass++;
printf("===Scenario: CD_000=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "1");
    }
    // Scenario: CD_010
    const std::unique_ptr<VerilatedContext> contextp_1 {new VerilatedContext};
    contextp = contextp_1.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0x8) {
        unpass++;
printf("===Scenario: CD_010=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "8");
    }
    // Scenario: CD_110
    const std::unique_ptr<VerilatedContext> contextp_2 {new VerilatedContext};
    contextp = contextp_2.get();
    top = new Vtop_module;
    top->c = 0x1;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0xb) {
        unpass++;
printf("===Scenario: CD_110=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "1");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "b");
    }
    // Scenario: CD_100
    const std::unique_ptr<VerilatedContext> contextp_3 {new VerilatedContext};
    contextp = contextp_3.get();
    top = new Vtop_module;
    top->c = 0x1;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x9) {
        unpass++;
printf("===Scenario: CD_100=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "1");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "9");
    }
    // Scenario: ToggleC_KeepD00
    const std::unique_ptr<VerilatedContext> contextp_4 {new VerilatedContext};
    contextp = contextp_4.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x1) {
        unpass++;
printf("===Scenario: ToggleC_KeepD00=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "1");
    }
    // Scenario: ToggleC_KeepD01
    const std::unique_ptr<VerilatedContext> contextp_5 {new VerilatedContext};
    contextp = contextp_5.get();
    top = new Vtop_module;
    top->c = 0x1;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x9) {
        unpass++;
printf("===Scenario: ToggleC_KeepD01=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "1");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "9");
    }
    // Scenario: ToggleD_KeepC00
    const std::unique_ptr<VerilatedContext> contextp_6 {new VerilatedContext};
    contextp = contextp_6.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x1) {
        unpass++;
printf("===Scenario: ToggleD_KeepC00=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "1");
    }
    // Scenario: ToggleD_KeepC01
    const std::unique_ptr<VerilatedContext> contextp_7 {new VerilatedContext};
    contextp = contextp_7.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0x8) {
        unpass++;
printf("===Scenario: ToggleD_KeepC01=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "8");
    }
    // Scenario: ToggleC_KeepD10
    const std::unique_ptr<VerilatedContext> contextp_8 {new VerilatedContext};
    contextp = contextp_8.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0x8) {
        unpass++;
printf("===Scenario: ToggleC_KeepD10=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "8");
    }
    // Scenario: ToggleC_KeepD11
    const std::unique_ptr<VerilatedContext> contextp_9 {new VerilatedContext};
    contextp = contextp_9.get();
    top = new Vtop_module;
    top->c = 0x1;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0xb) {
        unpass++;
printf("===Scenario: ToggleC_KeepD11=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "1");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "b");
    }
    // Scenario: ComplexSequence0
    const std::unique_ptr<VerilatedContext> contextp_10 {new VerilatedContext};
    contextp = contextp_10.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x1) {
        unpass++;
printf("===Scenario: ComplexSequence0=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "1");
    }
    // Scenario: ComplexSequence1
    const std::unique_ptr<VerilatedContext> contextp_11 {new VerilatedContext};
    contextp = contextp_11.get();
    top = new Vtop_module;
    top->c = 0x0;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0x8) {
        unpass++;
printf("===Scenario: ComplexSequence1=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "0");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "8");
    }
    // Scenario: ComplexSequence2
    const std::unique_ptr<VerilatedContext> contextp_12 {new VerilatedContext};
    contextp = contextp_12.get();
    top = new Vtop_module;
    top->c = 0x1;
    top->d = 0x1;
    top->eval();
    if (top->mux_in != 0xb) {
        unpass++;
printf("===Scenario: ComplexSequence2=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "1");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "1");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "b");
    }
    // Scenario: ComplexSequence3
    const std::unique_ptr<VerilatedContext> contextp_13 {new VerilatedContext};
    contextp = contextp_13.get();
    top = new Vtop_module;
    top->c = 0x1;
    top->d = 0x0;
    top->eval();
    if (top->mux_in != 0x9) {
        unpass++;
printf("===Scenario: ComplexSequence3=====\n");
printf("input_vars:\n");
printf("top->%s = 0x%s\n", "c", "1");

printf("input_vars:\n");
printf("top->%s = 0x%s\n", "d", "0");

printf("%x\n",top->mux_in);

        printf("Mismatch at %s: expected 0x%s\n", "mux_in", "9");
    }

    if (unpass == 0) {
        std::cout << "All tests passed!" << std::endl;
    } else {
        std::cout << "Found " << unpass << " mismatches." << std::endl;
    }
    return unpass;
}
