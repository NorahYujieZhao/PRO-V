// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop_module.h for the primary calling header

#include "Vtop_module__pch.h"
#include "Vtop_module__Syms.h"
#include "Vtop_module___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop_module___024root___dump_triggers__act(Vtop_module___024root* vlSelf);
#endif  // VL_DEBUG

void Vtop_module___024root___eval_triggers__act(Vtop_module___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop_module__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop_module___024root___eval_triggers__act\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VactTriggered.set(0U, ((IData)(vlSelfRef.clk) 
                                       & (~ (IData)(vlSelfRef.__Vtrigprevexpr___TOP__clk__0))));
    vlSelfRef.__Vtrigprevexpr___TOP__clk__0 = vlSelfRef.clk;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop_module___024root___dump_triggers__act(vlSelf);
    }
#endif
}

VL_INLINE_OPT void Vtop_module___024root___nba_sequent__TOP__0(Vtop_module___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    Vtop_module__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop_module___024root___nba_sequent__TOP__0\n"); );
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Init
    SData/*15:0*/ __Vdly__q;
    __Vdly__q = 0;
    // Body
    __Vdly__q = vlSelfRef.q;
    if (((IData)(vlSelfRef.reset) | ((9U == (0xfU & (IData)(vlSelfRef.q))) 
                                     & (IData)(vlSelfRef.top_module__DOT__enable)))) {
        ++(vlSymsp->__Vcoverage[2]);
        __Vdly__q = (0xfff0U & (IData)(__Vdly__q));
    } else if ((1U & (IData)(vlSelfRef.top_module__DOT__enable))) {
        __Vdly__q = ((0xfff0U & (IData)(__Vdly__q)) 
                     | (0xfU & ((IData)(1U) + (IData)(vlSelfRef.q))));
        ++(vlSymsp->__Vcoverage[0]);
    } else {
        ++(vlSymsp->__Vcoverage[1]);
    }
    ++(vlSymsp->__Vcoverage[3]);
    if (((IData)(vlSelfRef.reset) | (IData)(((0x90U 
                                              == (0xf0U 
                                                  & (IData)(vlSelfRef.q))) 
                                             & ((IData)(vlSelfRef.top_module__DOT__enable) 
                                                >> 1U))))) {
        ++(vlSymsp->__Vcoverage[2]);
        __Vdly__q = (0xff0fU & (IData)(__Vdly__q));
    } else if ((2U & (IData)(vlSelfRef.top_module__DOT__enable))) {
        __Vdly__q = ((0xff0fU & (IData)(__Vdly__q)) 
                     | (0xf0U & (((IData)(1U) + ((IData)(vlSelfRef.q) 
                                                 >> 4U)) 
                                 << 4U)));
        ++(vlSymsp->__Vcoverage[0]);
    } else {
        ++(vlSymsp->__Vcoverage[1]);
    }
    ++(vlSymsp->__Vcoverage[3]);
    if (((IData)(vlSelfRef.reset) | (IData)(((0x900U 
                                              == (0xf00U 
                                                  & (IData)(vlSelfRef.q))) 
                                             & ((IData)(vlSelfRef.top_module__DOT__enable) 
                                                >> 2U))))) {
        ++(vlSymsp->__Vcoverage[2]);
        __Vdly__q = (0xf0ffU & (IData)(__Vdly__q));
    } else if ((4U & (IData)(vlSelfRef.top_module__DOT__enable))) {
        __Vdly__q = ((0xf0ffU & (IData)(__Vdly__q)) 
                     | (0xf00U & (((IData)(1U) + ((IData)(vlSelfRef.q) 
                                                  >> 8U)) 
                                  << 8U)));
        ++(vlSymsp->__Vcoverage[0]);
    } else {
        ++(vlSymsp->__Vcoverage[1]);
    }
    ++(vlSymsp->__Vcoverage[3]);
    if (((IData)(vlSelfRef.reset) | (IData)(((0x9000U 
                                              == (0xf000U 
                                                  & (IData)(vlSelfRef.q))) 
                                             & ((IData)(vlSelfRef.top_module__DOT__enable) 
                                                >> 3U))))) {
        ++(vlSymsp->__Vcoverage[2]);
        __Vdly__q = (0xfffU & (IData)(__Vdly__q));
    } else if ((8U & (IData)(vlSelfRef.top_module__DOT__enable))) {
        __Vdly__q = ((0xfffU & (IData)(__Vdly__q)) 
                     | (0xf000U & (((IData)(1U) + ((IData)(vlSelfRef.q) 
                                                   >> 0xcU)) 
                                   << 0xcU)));
        ++(vlSymsp->__Vcoverage[0]);
    } else {
        ++(vlSymsp->__Vcoverage[1]);
    }
    ++(vlSymsp->__Vcoverage[3]);
    ++(vlSymsp->__Vcoverage[4]);
    vlSelfRef.q = __Vdly__q;
    vlSelfRef.ena = (((0x999U == (0xfffU & (IData)(vlSelfRef.q))) 
                      << 2U) | (((0x99U == (0xffU & (IData)(vlSelfRef.q))) 
                                 << 1U) | (9U == (0xfU 
                                                  & (IData)(vlSelfRef.q)))));
    vlSelfRef.top_module__DOT__enable = (1U | ((((0x999U 
                                                  == 
                                                  (0xfffU 
                                                   & (IData)(vlSelfRef.q))) 
                                                 << 3U) 
                                                | ((0x99U 
                                                    == 
                                                    (0xffU 
                                                     & (IData)(vlSelfRef.q))) 
                                                   << 2U)) 
                                               | ((9U 
                                                   == 
                                                   (0xfU 
                                                    & (IData)(vlSelfRef.q))) 
                                                  << 1U)));
}
