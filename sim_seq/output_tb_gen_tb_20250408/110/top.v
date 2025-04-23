module top_module (
	input d,
	input ena,
	output logic q
);
	/* verilator lint_off LATCH */
	always@(*) begin
		if (ena)
			q = d;
	end

endmodule
