
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
        int unpass = 0;
       ////////////////////////////scenario NormalCounting////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_0 {new VerilatedContext};
    contextp = contextp_0.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,20, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,20, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,20, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,20, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,20, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,20, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,20, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,20, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,20, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,20, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,20, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,20, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,20, "q", top->q, 0x0012);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0013) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,20, "q", top->q, 0x0013);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0014) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,20, "q", top->q, 0x0014);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0015) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,20, "q", top->q, 0x0015);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0016) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,20, "q", top->q, 0x0016);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0017) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,20, "q", top->q, 0x0017);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0018) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,20, "q", top->q, 0x0018);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,20, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0019) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,20, "q", top->q, 0x0019);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,20, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0020) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,20, "q", top->q, 0x0020);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario NormalCounting" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario NormalCounting" << std::endl;
        }
       ////////////////////////////scenario ResetBehavior////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_1 {new VerilatedContext};
    contextp = contextp_1.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,15, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,15, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,15, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,15, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,15, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,15, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,15, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,15, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,15, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,15, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,15, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,15, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,15, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,15, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,15, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,15, "q", top->q, 0x0009);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario ResetBehavior" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario ResetBehavior" << std::endl;
        }
       ////////////////////////////scenario DigitRollover////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_2 {new VerilatedContext};
    contextp = contextp_2.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,12, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,12, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,12, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,12, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,12, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,12, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,12, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,12, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,12, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,12, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,12, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,12, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,12, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,12, "q", top->q, 0x0012);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario DigitRollover" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario DigitRollover" << std::endl;
        }
       ////////////////////////////scenario MultipleResets////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_3 {new VerilatedContext};
    contextp = contextp_3.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,25, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,25, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,25, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,25, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,25, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,25, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,25, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,25, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,25, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,25, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,25, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,25, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,25, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,25, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,25, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,25, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,25, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,25, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,25, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,25, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,25, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,25, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,25, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,25, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,25, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,25, "q", top->q, 0x0010);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario MultipleResets" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario MultipleResets" << std::endl;
        }
       ////////////////////////////scenario RandomTest0////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_4 {new VerilatedContext};
    contextp = contextp_4.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,22, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,22, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,22, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,22, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,22, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,22, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,22, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,22, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,22, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,22, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,22, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,22, "q", top->q, 0x0012);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0013) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,22, "q", top->q, 0x0013);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0014) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,22, "q", top->q, 0x0014);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0015) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,22, "q", top->q, 0x0015);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0016) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,22, "q", top->q, 0x0016);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0017) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,22, "q", top->q, 0x0017);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0018) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,22, "q", top->q, 0x0018);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,22, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,22, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,22, "q", top->q, 0x0002);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest0" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest0" << std::endl;
        }
       ////////////////////////////scenario RandomTest1////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_5 {new VerilatedContext};
    contextp = contextp_5.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,25, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,25, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,25, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,25, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,25, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,25, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,25, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,25, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,25, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,25, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,25, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,25, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,25, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,25, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,25, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,25, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,25, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,25, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,25, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,25, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,25, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,25, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,25, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,25, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,25, "q", top->q, 0x0012);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0013) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,25, "q", top->q, 0x0013);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,25, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0014) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,25, "q", top->q, 0x0014);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest1" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest1" << std::endl;
        }
       ////////////////////////////scenario RandomTest2////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_6 {new VerilatedContext};
    contextp = contextp_6.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,17, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,17, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,17, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,17, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,17, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,17, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,17, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,17, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,17, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,17, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,17, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,17, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,17, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,17, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,17, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,17, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,17, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,17, "q", top->q, 0x0001);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest2" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest2" << std::endl;
        }
       ////////////////////////////scenario RandomTest3////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_7 {new VerilatedContext};
    contextp = contextp_7.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,22, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,22, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,22, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,22, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,22, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,22, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,22, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,22, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,22, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,22, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,22, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,22, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,22, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,22, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,22, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,22, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,22, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,22, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,22, "q", top->q, 0x0002);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest3" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest3" << std::endl;
        }
       ////////////////////////////scenario RandomTest4////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_8 {new VerilatedContext};
    contextp = contextp_8.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,27, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,27, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,27, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,27, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,27, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,27, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,27, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,27, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,27, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,27, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,27, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,27, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,27, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,27, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,27, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,27, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,27, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,27, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,27, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,27, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,27, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,27, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,27, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,27, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,27, "q", top->q, 0x0012);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0013) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,27, "q", top->q, 0x0013);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0014) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,27, "q", top->q, 0x0014);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 25,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 25,27, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 26,27, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 26,27, "q", top->q, 0x0001);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest4" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest4" << std::endl;
        }
       ////////////////////////////scenario RandomTest5////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_9 {new VerilatedContext};
    contextp = contextp_9.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,21, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,21, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,21, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,21, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,21, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,21, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,21, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,21, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,21, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,21, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,21, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,21, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,21, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,21, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,21, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,21, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,21, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,21, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,21, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,21, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,21, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,21, "q", top->q, 0x0007);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest5" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest5" << std::endl;
        }
       ////////////////////////////scenario RandomTest6////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_10 {new VerilatedContext};
    contextp = contextp_10.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,28, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,28, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,28, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,28, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,28, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,28, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,28, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,28, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,28, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,28, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,28, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,28, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,28, "q", top->q, 0x0012);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,28, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,28, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,28, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,28, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,28, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,28, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,28, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,28, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,28, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,28, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,28, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,28, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,28, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 25,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 25,28, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 26,28, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 26,28, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 27,28, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 27,28, "q", top->q, 0x0010);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest6" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest6" << std::endl;
        }
       ////////////////////////////scenario RandomTest7////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_11 {new VerilatedContext};
    contextp = contextp_11.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,18, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,18, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,18, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,18, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,18, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,18, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,18, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,18, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,18, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,18, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,18, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,18, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,18, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,18, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,18, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,18, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,18, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,18, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,18, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,18, "q", top->q, 0x0011);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest7" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest7" << std::endl;
        }
       ////////////////////////////scenario RandomTest8////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_12 {new VerilatedContext};
    contextp = contextp_12.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,22, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,22, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,22, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,22, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,22, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,22, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,22, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,22, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,22, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,22, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,22, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,22, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,22, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,22, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x1) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,22, "ena", top->ena, 0x1);
        }
        if (top->q != 0x0010) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,22, "q", top->q, 0x0010);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0011) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,22, "q", top->q, 0x0011);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0012) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,22, "q", top->q, 0x0012);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0013) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,22, "q", top->q, 0x0013);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0014) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,22, "q", top->q, 0x0014);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,22, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0015) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,22, "q", top->q, 0x0015);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest8" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest8" << std::endl;
        }
       ////////////////////////////scenario RandomTest9////////////////////////////
        unpass = 0;
    const std::unique_ptr<VerilatedContext> contextp_13 {new VerilatedContext};
    contextp = contextp_13.get();
    top = new Vtop_module;
    top->clk = 0;
        top->ena = 0x0;
        top->q = 0x0;
        top->clk = 1;
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 0,26, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 1,26, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 2,26, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 3,26, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 4,26, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 5,26, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 6,26, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 7,26, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0009) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 8,26, "q", top->q, 0x0009);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 9,26, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 10,26, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 11,26, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 12,26, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 13,26, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 14,26, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 15,26, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 16,26, "q", top->q, 0x0007);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0008) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 17,26, "q", top->q, 0x0008);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x1;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0000) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 18,26, "q", top->q, 0x0000);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0001) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 19,26, "q", top->q, 0x0001);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0002) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 20,26, "q", top->q, 0x0002);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0003) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 21,26, "q", top->q, 0x0003);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0004) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 22,26, "q", top->q, 0x0004);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0005) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 23,26, "q", top->q, 0x0005);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0006) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 24,26, "q", top->q, 0x0006);
        }
        contextp->timeInc(1);  
        top->clk = !top->clk;
         top->eval();
         contextp->timeInc(1);
        top->clk = !top->clk;
        top->reset = 0x0;
        top->eval();
        if (top->ena != 0x0) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 25,26, "ena", top->ena, 0x0);
        }
        if (top->q != 0x0007) {
            unpass++;
printf("input_vars:\n");
printf("top->%s = 0x%x\n", "reset", top->reset);

            printf("At %d clock cycle of %d, top->%s = 0x%x, expected = 0x%x\n", 25,26, "q", top->q, 0x0007);
        }


        if (unpass == 0) {
            std::cout << "Test passed for scenario RandomTest9" << std::endl;
        } else {
            std::cout << "Test failed,unpass = " << unpass << " for scenario RandomTest9" << std::endl;
        }

    return unpass;
}
