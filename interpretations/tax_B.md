# Interpretations used by the solver

The forms specify most arithmetic directly. These are the places where the text leaves a choice, omits a needed taxpayer detail, or describes a conditional line without fully specifying its value. Quotes below are copied from `rules.txt`.

## Rounding

- **Tax Table rounding:** “First divide your taxable income by 50, round it down to the nearest integer, then multiply it by 50, and finally add 25.” The solver applies `floor(taxable_income / 50) * 50 + 25` exactly, then uses the rate and subtraction amount from the selected filing-status row.
- **Education phase-out ratios:** Form 8863 says, “Enter the result as a decimal (rounded to three places).” The solver rounds these ratios to three decimal places using decimal half-up rounding. The text specifies the number of places but not a tie-breaking rule.
- **Child-credit phase-out increment:** Schedule 8812 says, “If more than zero and not a multiple of $1,000, enter the next multiple of $1,000.” The solver rounds a positive, non-multiple amount upward to the next $1,000; exact multiples remain unchanged.
- **Other arithmetic:** The task says, “DO NOT round numbers without explicit instructions.” The solver keeps decimal results exact through the final line and rounds only where the quoted form instructions require it.

## Filing status and standard deduction

- **Age boxes:** The form asks whether the taxpayer or spouse was born before January 2, 1959, and gives ages “on January 2, 2024.” The taxpayer’s exact birthday is not supplied, so a reported age of exactly 65 does not distinguish someone born before January 2, 1959 from someone born on January 2, 1959. The solver treats age 65 or older as meeting the age box. A blindness box is counted independently of age.
- **Spouse boxes:** “You can only check the boxes for your spouse if your spouse is age 65 or older or blind and you file a joint return.” The solver counts either qualifying spouse box only for married filing jointly; the age box still requires age 65, while the blindness box does not.
- **Deduction choice:** “Using Itemized Deductions” selects Schedule A when True. Otherwise, the solver uses the standard deduction oracle keyed by status and eligible boxes. The standard deduction and itemized deduction are not added together.
- **State and local tax cap:** Schedule A says, “Enter the smaller of line 5d or $10,000 ($5,000 if married filing separately).” The solver uses the status-specific cap from the status-constants oracle.

## Tax worksheet selection

- **Tax Table versus Tax Computation Worksheet:** “If your taxable income is less than $100,000, you must use the Tax Table” and “If your taxable income is $100,000 or more, use the Tax Computation Worksheet.” The solver uses the Tax Table strictly below $100,000 and the computation worksheet starting at $100,000, for both regular tax and the corresponding qualified-dividend worksheet steps.
- **Qualified Dividends and Capital Gain Tax Worksheet:** The instruction says to use this worksheet if qualified dividends were reported, if capital gain distributions were reported without filing Schedule D, or if Schedule D lines 15 and 16 are both positive. The problem form set has no Schedule D, so the solver uses this worksheet when Form 1040 line 3a or line 7 is positive. It still computes the worksheet fields when the worksheet is printed, but uses its result for Form 1040 line 16 only when a stated trigger applies.
- **No Schedule D fields:** The worksheet says, “If No, enter the amount from Form 1040 or 1040-SR, line 7.” Since no Schedule D is present in these problems, line 3 uses Form 1040 line 7.

## Credits and missing taxpayer detail

- **Qualifying children under age 17:** The input gives only “Qualifying Children” as a count; it supplies no separate ages. Schedule 8812 asks for the “Number of qualifying children under age 17.” The solver treats the supplied qualifying-child count as the under-17 count. It also treats those children as meeting the required-SSN condition on Worksheet B because no SSN count is supplied.
- **Other dependents:** The Form 1040 gives an “Other Dependents” count but no further age or relationship detail. The solver carries that count to Schedule 8812 line 6, as that line requests other dependents and qualifying children not counted on line 4.
- **Child-credit phase-out:** Schedule 8812 states, “If zero or less, enter -0-,” then describes the next-$1,000 rule for positive amounts. The solver uses zero for a nonpositive phase-out amount and rounds positive amounts upward as described above.
- **Filing-status phase-out thresholds:** Form 8863 says, “Enter: $180,000 if married filing jointly; $90,000 otherwise” and “Enter: $20,000 if married filing jointly; $10,000 otherwise.” Schedule 8812 says, “Married filing jointly—$400,000; All other filing statuses—$200,000.” The solver applies those “otherwise” amounts to every non-MFJ status, including qualifying surviving spouse and married filing separately, through the status-constants oracle.
- **Nonrefundable-credit limits:** The Credit Limit Worksheets state subtraction and “smaller of” operations but do not expressly say to floor a negative remaining tax limit at zero. The solver floors the remaining limit at zero before applying a nonrefundable credit, because a negative amount cannot limit a credit below zero. This applies to Form 8863 Credit Limit Worksheet line 7 and Schedule 8812 Credit Limit Worksheet A lines 3 and 5.
- **Absent credit lines:** Schedule 8812 refers to Schedule 3 lines 6c, 6f, 6g, 6h, 6l, and 6m, and other worksheets refer to lines not printed in the provided Schedule 3. The solver treats an unprinted “if applicable” source line as zero.
- **Schedule 3 line 8 includes line 3:** The instruction says, “Add lines 1 through 4, 5a, 5b, and 7.” Because line 3 is within lines 1 through 4, the total includes the education credit from line 3 as well as line 7. The solver follows that enumerated addition and does not omit line 3.
- **American Opportunity Credit age caution:** Form 8863 says, “If you were under age 24 at the end of the year and meet the conditions described in the instructions, you can’t take the refundable American opportunity credit.” The referenced conditions and student ages are not supplied in these problems. The solver follows the printed 40% calculation; it cannot apply an unstated condition from missing data.
- **Student eligibility for Form 8863 Part III:** “Yes - Stop! Go to line 31 for this student.” (for lines 23, 25, and 26), “No - Stop! Go to line 31 for this student.” (for line 24), and “No - Complete lines 27 through 30 for this student.” (for line 26). The solver uses the supplied Yes/No answers on lines 23–26 and the line 21 expense for that same student. A student who fails the printed American Opportunity Credit conditions is routed to line 31; qualifying expenses are not also used on lines 27–30. These values are in Part III, so extraction for these lines uses their Part III source records rather than the main-line-only source filter.

## Self-employment and sign

- **Negative Schedule C profit:** Schedule SE says, “If line 3 is more than zero, multiply line 3 by 92.35% (0.9235). Otherwise, enter amount from line 3,” followed by “Multiply the smaller of line 4 or line 9 by 12.4% (0.124).” There is no further instruction to floor line 10 or 11 at zero, so the solver applies the stated operations literally if line 3 is negative.
- **Schedule SE line 3 source:** “Net profit or (loss) from Schedule C, line 31; and Schedule K-1 (Form 1065), box 14, code A (other than farming).” Schedule SE line 3 uses the computed Schedule C line 31 value. The provided problems do not include a Schedule K-1 or a filled K-1 box 14 code A amount, so that additional source contributes zero.
- **Earned Income Worksheet line 1a:** “Enter the amount from line 1z of Form 1040, 1040-SR, or 1040-NR.” Form 1040 line 1z is a computed value, so the worksheet copies the already computed line 1z rather than looking only for a taxpayer-filled source value.
- **Refund or balance due:** Form 1040 line 37 says, “Subtract line 33 from line 24. This is the amount you owe.” The solver returns that signed subtraction: positive means owed and negative means overpaid, as requested.
- **Nontaxable combat pay:** Form 1040 line 1z says, “Add lines 1a through 1c,” excluding line 1d. The solver excludes line 1d from line 1z and uses it in the Earned Income Worksheet and Schedule 8812 line 18b as instructed.
