// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop_module.h for the primary calling header

#include "Vtop_module__pch.h"
#include "Vtop_module__Syms.h"
#include "Vtop_module___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop_module___024root___dump_triggers__stl(Vtop_module___024root* vlSelf);
#endif  // VL_DEBUG

VL_ATTR_COLD void Vtop_module___024root___eval_triggers__stl(Vtop_module___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop_module__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop_module___024root___eval_triggers__stl\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VstlTriggered.set(0U, (IData)(vlSelfRef.__VstlFirstIteration));
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop_module___024root___dump_triggers__stl(vlSelf);
    }
#endif
}

VL_ATTR_COLD void Vtop_module___024root___configure_coverage(Vtop_module___024root* vlSelf, bool first) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop_module__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop_module___024root___configure_coverage\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    (void)first;  // Prevent unused variable warning
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[0]), first, "top_module.v", 13, 9, ".top_module", "v_branch/top_module", "if", "13-14");
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[1]), first, "top_module.v", 13, 10, ".top_module", "v_branch/top_module", "else", "");
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[2]), first, "top_module.v", 11, 4, ".top_module", "v_line/top_module", "elsif", "11-12");
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[3]), first, "top_module.v", 10, 3, ".top_module", "v_line/top_module", "block", "10");
    vlSelf->__vlCoverInsert(&(vlSymsp->__Vcoverage[4]), first, "top_module.v", 9, 2, ".top_module", "v_line/top_module", "block", "9-10");
}
