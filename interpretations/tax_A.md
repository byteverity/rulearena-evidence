# Interpretation ledger

The packet and task wording govern the calculations below. Every decision below records the competing readings, the chosen reading, and the supporting sentence from the packet or task wording. Dollar constants and status thresholds are evaluated from the compiled oracle; Python applies the line arithmetic.

## Rounding and decimal amounts

- **Competing readings:** Round each tax-form dollar line to whole dollars under a general tax-preparation convention, or keep cents unless this packet tells us to round.
- **Chosen reading:** Preserve the exact decimal result for every dollar calculation except where a form explicitly directs rounding. This includes credit percentages and the final answer.
- **Supporting sentence:** The task says “DO NOT round numbers without explicit instructions.” The only calculation-specific rounding directions used here are the Tax Table instruction “round it down to the nearest integer” and the Form 8863 directions to enter a ratio “rounded to three places.”
- **Competing readings:** Resolve an exact half-way ratio with half-up rounding or half-even rounding.
- **Chosen reading:** Use decimal round-half-up to three places. The packet specifies three-place rounding but does not specify tie behavior, so the conventional nearest-value rule is used.
- **Supporting sentence:** “Enter the result as a decimal (rounded to three places).”

## Age and standard deduction

- **Age 65 box** — **Competing readings:** Treat every supplied age of 65 or more as meeting the box, or require a known birth date strictly before January 2, 1959.
- **Chosen reading:** Use age 65 or more on January 2, 2024 as meeting the age box. The packet supplies ages but no birth dates, so an exactly-65 person whose birthday is January 2 cannot be distinguished from one born earlier.
- **Supporting sentence:** The form asks whether the filer was “born before January 2, 1959,” while Basic Information supplies “Age (on January 2, 2024).” This leaves the exact-65 birthday edge unresolved.
- **Spouse boxes** — **Competing readings:** Count a qualifying spouse’s age/blindness boxes for any filing status, or count them only on a joint return.
- **Chosen reading:** Count spouse boxes only for married filing jointly. Qualifying surviving spouse is not treated as filing a joint return.
- **Supporting sentence:** “You can only check the boxes for your spouse if your spouse is age 65 or older or blind and you file a joint return.”
- **Deduction choice** — **Competing readings:** Use Schedule A whenever it appears in the packet, or use Schedule A only when the supplied `Using Itemized Deductions` flag is true.
- **Chosen reading:** Use Schedule A only when that flag is true; otherwise use the status and age/blindness standard deduction amount from the oracle.
- **Supporting sentence:** Form 1040 line 12 is “Standard deduction or itemized deductions (from Schedule A),” and Basic Information explicitly says whether itemized deductions are used. The form further says: “If you checked any of the following boxes, figure your standard deduction using the Standard Deduction Chart…”

## Tax calculation worksheets

- **Tax Table versus Tax Computation Worksheet** — **Competing readings:** Use the Tax Table at exactly $100,000 because the table includes the boundary, or switch to the Tax Computation Worksheet at $100,000.
- **Chosen reading:** Use the Tax Table only below $100,000; use the Tax Computation Worksheet at or above $100,000.
- **Supporting sentence:** “If your taxable income is less than $100,000, you must use the Tax Table…” and “If your taxable income is $100,000 or more, use the Tax Computation Worksheet right after the Tax Table.”
- **Tax Table midpoint** — **Competing readings:** Select the interval containing taxable income directly, or use the midpoint produced by the worksheet instruction.
- **Chosen reading:** Divide by $50, round down, multiply by $50, and add $25 before selecting the row and computing the tax.
- **Supporting sentence:** “First divide your taxable income by 50, round it down to the nearest integer, then multiply it by 50, and finally add 25.”
- **Qualified Dividends and Capital Gain Tax Worksheet** — **Competing readings:** Use it only for qualified dividends, or also use it for capital-gain distributions on line 7 when Schedule D is not filed.
- **Chosen reading:** Use it when line 3a is positive or line 7 is positive. Schedule D is absent from these packets, so the worksheet’s “No” branch enters line 7.
- **Supporting sentence:** The triggers include “You reported qualified dividends on Form 1040 or 1040-SR, line 3a” and “You don’t have to file Schedule D and you reported capital gain distributions on Form 1040 or 1040-SR, line 7.” The worksheet says: “If No, enter the amount from Form 1040 or 1040-SR, line 7.”

## Schedule C and Schedule SE

- **Schedule SE line 3** — **Competing readings:** Read Schedule C line 31 from the supplied-value map, or use the value calculated on Schedule C line 31.
- **Chosen reading:** Calculate Schedule C line 31 first and pass that result to Schedule SE line 3. `[__]` marks line 31 as a computed field, not a missing input.
- **Supporting sentence:** Schedule C line 31 says “Subtract line 30 from line 29. Enter here and on both Schedule 1 (Form 1040), line 3, and on Schedule SE, line 2.” Schedule SE line 3 says “Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming).” No Schedule K-1 values are supplied, so that contribution is zero.
- **Schedule SE line 9** — **Competing readings:** Allow a negative wage-base remainder to flow into line 10, or replace it with zero.
- **Chosen reading:** Floor line 9 at zero; retain decimals in other self-employment-tax calculations.
- **Supporting sentence:** Line 9 says “If zero or less, enter -0- here and on line 10 and go to line 11.” No other Schedule SE line gives a rounding instruction.

## Form 8863 education credits

- **Repeated student Parts III** — **Competing readings:** Use only one Part III record, or calculate each student separately and total all student results.
- **Chosen reading:** Number each repeated Part III section, calculate its lines 27–31 separately, then sum all line 30 values for Form 8863 line 1 and all line 31 values for line 10. This fixes the prior single-student aggregation error.
- **Supporting sentence:** Part I line 1 says “enter the total of all amounts from all Parts III, line 30”; Part II line 10 says “enter the total of all amounts from all Parts III, line 31.”
- **American Opportunity Credit eligibility** — **Competing readings:** Send expenses through lines 27–30 for every student, or send them to line 31 when any stop condition applies.
- **Chosen reading:** A student is eligible for the AOC path only when line 23 is No, line 24 is Yes, line 25 is No, and line 26 is No. Otherwise line 27–30 are zero and the student’s expenses go to line 31.
- **Supporting sentence:** Each applicable question says “Yes - Stop! Go to line 31 for this student” or “No - Stop! Go to line 31 for this student”; the final line 26 instruction says “No - Complete lines 27 through 30 for this student.”
- **Refundable portion and line 9** — **Competing readings:** Apply the 40% refundable calculation and subtract it from line 7, or skip line 8 and enter all of line 7 on line 9 under the age exception.
- **Chosen reading:** For the supplied taxpayers, apply line 8 as 40% of line 7 and line 9 as the remaining amount. The youngest supplied taxpayer is age 25 on January 2, 2024, so no supplied taxpayer was under 24 at the end of 2023. In `tax_L1_010`, age 69 also makes the exception inapplicable. The independent disagreement on line 9 does not justify changing this reading.
- **Supporting sentence:** The exception applies “If you were under age 24 at the end of the year and meet the conditions described in the instructions.” Line 8 says “Multiply line 7 by 40% (0.40),” and line 9 says “Subtract line 8 from line 7.” The referenced additional conditions are not included in the packet, but the supplied ages do not meet the stated under-24 prerequisite.
- **Fractional results** — **Competing readings:** Apply ordinary whole-dollar rounding to lines 8 or 9, or preserve the cents produced by the explicit percentage and subtraction arithmetic. The instruction on line 6 to round the phase-out ratio to three places is not an instruction to round later dollar results.
- **Chosen reading:** Preserve the fractional amounts. For example, `tax_L1_047` has line 6 = 0.263, line 7 = 2246 × 0.263 = 590.698, line 8 = 236.2792, and line 9 = 354.4188. This follows the task's no-rounding direction and the exact line 8/9 formulas above.
- **Supporting sentence:** The task says “DO NOT round numbers without explicit instructions”; Form 8863 gives a three-place rounding direction for line 6 but gives line 8 and line 9 only the formulas “Multiply line 7 by 40% (0.40)” and “Subtract line 8 from line 7.”
- **Education phase-out** — **Competing readings:** Use the joint or non-joint thresholds based on an inferred household, or use the filing status printed in Basic Information.
- **Chosen reading:** Use the explicit filing status: $180,000/$90,000 for the upper limit and $20,000/$10,000 for the phase-out range. Apply the ratio rules separately to Parts I and II and round those ratios to three places as directed.
- **Supporting sentence:** Form 8863 says “Enter: $180,000 if married filing jointly; $90,000 otherwise” and “Enter: $20,000 if married filing jointly; $10,000 otherwise.”

## Schedule 3 total credits

- **Competing readings:** Add only taxpayer-filled Schedule 3 lines to line 8, or include the computed education-credit amount on line 3 before totaling.
- **Chosen reading:** Include the computed Schedule 3 line 3 along with the other listed lines. Line 3 is populated from Form 8863 line 19 before line 8 is calculated.
- **Supporting sentence:** Schedule 3 line 8 says: “Add lines 1 through 4, 5a, 5b, and 7.” This includes line 3 even though it is computed rather than supplied as a filled input.

## Schedule 8812 credits and worksheet branches

- **Earned Income Worksheet line 1a** — **Competing readings:** Enter only Form 1040 line 1a wages, or enter Form 1040 line 1z as named by the worksheet. The independent disagreement at `tax_L1_013` concerns this line.
- **Chosen reading:** Enter Form 1040 line 1z. For `tax_L1_013`, that is $31,166 = $28,823 + $195 + $2,148. Form 1040 line 1z excludes line 1d combat pay because its instruction adds only lines 1a through 1c; the Earned Income Worksheet has a separate line 1b for that combat pay.
- **Supporting sentence:** Earned Income Worksheet line 1a says “Enter the amount from line 1z of Form 1040, 1040-SR, or 1040-NR.” Form 1040 line 1z says “Add lines 1a through 1c.” Earned Income Worksheet line 1b separately says “Enter the amount of any nontaxable combat pay received.”
- **Qualifying-child count** — **Competing readings:** Treat the supplied `Qualifying Children` count as the number eligible for the under-17 and required-SSN computations, or require ages and SSN facts not provided in the packet.
- **Chosen reading:** Use the supplied qualifying-child count for those calculations because no child ages or SSN facts are supplied. This is an assumption forced by the incomplete inputs.
- **Supporting sentence:** Schedule 8812 line 4 asks for the “Number of qualifying children under age 17”; Credit Limit Worksheet B line 2 asks for children “under 17 with the required social security number.” Basic Information supplies only “Qualifying Children: N.”
- **Other dependents** — **Competing readings:** Add these people on top of the qualifying-child count even if categories overlap, or treat the two supplied counts as separate categories.
- **Chosen reading:** Use `Other Dependents` only for line 6 and do not infer overlap or another person from the qualifying-child count.
- **Supporting sentence:** Schedule 8812 says “do not include anyone you included on line 4.”
- **Phase-out rounding** — **Competing readings:** Use an AGI amount above the threshold as-is, or round it up to the next $1,000 before applying 5%.
- **Chosen reading:** If AGI exceeds the filing-status threshold, round the excess up to the next $1,000, then multiply by 5% without further rounding.
- **Supporting sentence:** Line 10 says “If more than zero and not a multiple of $1,000, enter the next multiple of $1,000”; line 11 says “Multiply line 10 by 5% (0.05).”
- **Worksheet credit limits** — **Competing readings:** Infer unlisted credits from other lines or count only amounts named by the worksheet and present in the packet.
- **Chosen reading:** Sum only the listed Schedule 3 lines. A listed line absent from the supplied Schedule 3, including lines 6f, 6l, or 6m where applicable, contributes zero. Form 8863 Credit Limit Worksheet line 5 also includes listed line 6l; it contributes zero because that line is not supplied.
- **Supporting sentence:** The worksheets enumerate the exact Schedule 3 lines to add. For Schedule 8812 Worksheet A, the entries are lines 1, 2, 3, 4, 5b, 6d, 6f, 6l, and 6m; Form 8863's worksheet specifies lines 1, 2, 6d, and 6l.
- **Skipped `[__]` fields** — **Competing readings:** Leave a skipped worksheet field uncomputed, or give each marked `[__]` field its direct formula result while honoring the stop/skip branch for downstream credits.
- **Chosen reading:** Record formula results for marked intermediate fields and use the printed branch tests to decide which credit amounts flow to later lines. This follows the task request to calculate all `[__]` fields while retaining the worksheet's branch logic.
- **Supporting sentence:** The task says “calculate all fields marked with [__]”; the worksheets also give their conditional “skip” and “stop” directions.

## Final tax sign

- **Competing readings:** Return line 37's raw sign, or express an amount owed as positive and an overpayment as negative.
- **Chosen reading:** Return `Form 1040 line 24 − line 33`; positive is owed and negative is overpaid, as the task specifies.
- **Supporting sentence:** The task requests “tax OWED ... as a positive number, or tax OVERPAID as a NEGATIVE number.” Form 1040 line 37 says “Subtract line 33 from line 24. This is the amount you owe.”
