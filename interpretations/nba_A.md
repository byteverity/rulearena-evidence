# Interpretations

This register states the deterministic reading used by `solver/solve.py` whenever the prompt and the supplied CBA excerpt do not fully specify an input or calculation. Each item gives the competing readings, the selected reading, and exact source text. No answer labels were used.

## I-01 — Starting Team Salary, expired contracts, and free-agent holds

**Competing readings:** Treat each stated Team Salary as a complete CBA Team Salary and add nothing; or use the stated salary with the prompt’s express exclusion, then include the CBA Free Agent Amount for each described free agent whose expiring contract salary was excluded.

**Chosen reading:** Use the supplied amount as the starting aggregate, do not add the expired contract’s prior salary, and add the applicable Free Agent Amount for a player whose contract ended after 2023-24. Keep that hold until the player re-signs, signs with another team, or is renounced. This follows the express Team Salary carveout and the CBA’s explicit hold rule. A signing or match replaces that player’s hold with the new contract salary; an offer sheet adds its salary to the New Team while the Prior Team hold remains until the player signs elsewhere or is matched.

**Exact supporting sentences:**

> “the Team Salary of each team listed under "Team Situations:" do not include the amount of contracts that expire at the end of 2023-2024 Salary Cap Year.”

> “Subject to Section 4(a)(2)(ii) above, until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (“Free Agent Amounts”):”

## I-02 — Restricted free-agent holds and unstated Qualifying Offer amounts

**Competing readings:** For a restricted free agent, use only the Free Agent Amount; or use the greatest stated amount among the Free Agent Amount, an outstanding Qualifying Offer, and a First Refusal Exercise Notice. Where a problem says only that a Qualifying Offer was tendered, one could infer its salary from a separate formula, or use only the amount computable from the supplied facts and excerpt.

**Chosen reading:** Use the CBA’s greatest-of rule when each amount is supplied. If the situation says a Qualifying Offer was tendered but supplies neither its salary nor the referenced Qualifying Offer calculation, retain the computable Free Agent Amount and do not invent a Qualifying Offer salary. A Qualifying Offer changes the stored status to restricted; the amount comparison is noted as underdetermined.

**Exact supporting sentences:**

> “With respect to each Veteran Free Agent who last played for a Team who is a Restricted Free Agent, the greater of (A) the Free Agent Amount (as defined in Section 4(d) below) attributable to such Veteran Free Agent, (B) the Salary called for in any outstanding Qualifying Offer (other than a Two-Way Qualifying Offer, as defined in Article XI, Section 1(e)(iii)(B) below) tendered to such Veteran Free Agent (or, if the Restricted Free Agent was also tendered a Maximum Qualifying Offer pursuant to Article XI, Section 4(a)(ii), the Salary called for in such outstanding Maximum Qualifying Offer), or (C) the Salary called for in any First Refusal Exercise Notice (as defined in Article XI, Section 5(g)) issued with respect to such Veteran Free Agent.”

> “A Qualifying Veteran Free Agent, other than a Qualifying Veteran Free Agent described in Section 4(d)(1)(ii) below, will be included at one hundred fifty percent (150%) of his prior Salary if it was equal to or greater than the Estimated Average Player Salary for the prior Salary Cap Year, and one hundred ninety percent (190%) of his prior Salary if it was less than the Estimated Average Player Salary for the prior Salary Cap Year.”

## I-03 — Free Agent Amount class, minimum, and maximum

**Competing readings:** Derive a free-agent amount from total service alone, or classify the player using the required contract coverage and team history. For the benefit-fund minimum, use the full minimum salary or the unreimbursed portion specified by Article IV.

**Chosen reading:** Classify as Qualifying, Early Qualifying, or Non-Qualifying only when the listed contract history establishes the relevant coverage and Prior Team relationship. Apply the 150%/190%, 130%, or 120% multiplier; apply the special 250%/300% rookie-scale amount only when a four-year first-round contract explicitly shows two team-option years. Cap the amount at the maximum salary. Article IV, Section 6(h)’s reimbursement amount is not included in the supplied excerpt, so for a minimum-salary floor the code uses the current service-tier minimum as a proxy and records this limitation. Section 4(d)(6) also refers to Article VII, Section 6(n)(3), whose salary limit is absent from the supplied rules; no limit is invented from another CBA version.

**Exact supporting sentences:**

> “Early Qualifying Veteran Free Agent” means a Veteran Free Agent who, prior to becoming a Veteran Free Agent, played under one (1) or more Player Contracts covering some or all of each of the two (2) preceding Seasons, and who either played exclusively with his Prior Team during such two (2) Seasons, or, if he played for more than one (1) Team during such period, changed Teams only (i) by means of trade, (ii) by means of assignment via the NBA’s waiver procedures, or (iii) by signing with his Prior Team during the first of the two (2) Seasons.”

> “A Qualifying Veteran Free Agent, other than a Qualifying Veteran Free Agent described in Section 4(d)(1)(ii) below, will be included at one hundred fifty percent (150%) of his prior Salary if it was equal to or greater than the Estimated Average Player Salary for the prior Salary Cap Year, and one hundred ninety percent (190%) of his prior Salary if it was less than the Estimated Average Player Salary for the prior Salary Cap Year.”

> “A Qualifying Veteran Free Agent following the second Option Year of his Rookie Scale Contract will be included at two hundred fifty percent (250%) of the player’s prior Salary if it was equal to or greater than the Estimated Average Player Salary for the prior Salary Cap Year, and three hundred percent (300%) of his prior Salary if it was less than the Estimated Average Player Salary for the prior Salary Cap Year.”

> “An Early Qualifying Veteran Free Agent will be included at one hundred thirty percent (130%) of his prior Salary; provided, however, that the player’s Prior Team may, by written notice to the NBA, renounce its rights to sign the player pursuant to the Early Qualifying Veteran Free Agent Exception, in which case the player will be deemed a Non-Qualifying Veteran Free Agent for purposes of this Section 4(d) and Sections 6(b) and 6(j)(5) below.”

> “A Non-Qualifying Veteran Free Agent will be included at one hundred twenty percent (120%) of his prior Salary.”

> “Notwithstanding Sections 4(d)(1)-(3) above, if the player’s prior Salary was equal to or less than the Minimum Player Salary applicable to such player, he will be included at the portion of the then-current Minimum Annual Salary applicable to such player that would not be reimbursed out of the League-wide benefits fund described in Article IV, Section 6(h).”

> “Notwithstanding Sections 4(d)(1)-(3) above, at no time shall a player’s Free Agent Amount exceed the Maximum Player Salary applicable to such player or be less than the portion of the Minimum Annual Salary applicable to such player that would not be reimbursed out of the League-wide benefits fund described in Article IV, Section 6(h).”

> “Notwithstanding Sections 4(d)(1)-(3) above, at no time shall a Free Agent Amount for a Veteran Free Agent following the second or third Season of his Rookie Scale Contract exceed the maximum amount the Team may pay the player pursuant to Section 6(n)(3) below.”

## I-04 — Missing Team Salary for a team

**Competing readings:** Treat an unlisted team’s starting Team Salary as unknown and decline cap/apron arithmetic; or use a deterministic zero starting salary because no amount was supplied.

**Chosen reading:** Use zero for a team with no stated Team Salary, then add any computable free-agent holds and salaries that the described transactions place on it. This is a reproducible default, not a claim that the real team has no other players or salary.

**Exact supporting sentence:**

> “the Team Salary of each team listed under "Team Situations:" do not include the amount of contracts that expire at the end of 2023-2024 Salary Cap Year.”

## I-05 — Years of Service inferred from draft year

**Competing readings:** Treat Years of Service as unknown because the facts do not enumerate NBA seasons played; or estimate it from the draft year.

**Chosen reading:** Use `max(0, 2024 − draft year)` as a service proxy because the scenarios provide draft year and age but no service total or missed seasons. This can misclassify a player who did not render service in every intervening season; no missed season is invented.

**Exact supporting sentences:**

> “for any player who has completed fewer than seven (7) Years of Service”

> “Player A was the 12th first-round pick of Team B in 2008 NBA draft when he was 19 years old.”

## I-06 — Age and birthdays

**Competing readings:** Require a birth date to decide age in a later season; or advance the stated draft age by elapsed calendar years.

**Chosen reading:** Estimate age by adding elapsed calendar years to the stated age at draft. Because birth dates are absent, the special birthday deeming rule cannot be applied; the October 1 season boundary is used only with this age estimate.

**Exact supporting sentences:**

> “For purposes of determining whether a Contract is an Over 38 Contract pursuant to this Section 3(a)(2) only, Seasons shall be deemed to commence on October 1 and conclude on the last day of the Salary Cap Year.”

> “any player whose Over 38 Contract is signed pursuant to Section 8(e)(1) below shall not be considered a Qualifying Veteran Free Agent.”

## I-07 — Over-38 attribution

**Competing readings:** Check only the salary written for the first season; or reallocate salary from the specified later seasons to earlier seasons.

**Chosen reading:** Apply the CBA’s pro-rata attribution to cap-room, Team Salary, trade matching, and apron checks. When the exact birthday is absent, use the age proxy in I-06 to identify whether a covered Season follows the 38th birthday. Preserve the explicit age-35/36 Prior Team exception where the supplied facts establish it.

**Exact supporting sentences:**

> “The following provisions shall apply to any Player Contract entered into, extended, or renegotiated that, beginning with the date such Contract, Extension, or Renegotiation is signed, covers four (4) or more Seasons, including one (1) or more Seasons commencing after such player will reach or has reached age thirty-eight (38) (an “Over 38 Contract”):”

> “Except as provided in Sections 3(a)(2)(ii)-(iii) below, the aggregate Salaries in an Over 38 Contract for Salary Cap Years commencing with the fourth Salary Cap Year of such Over 38 Contract or the first Salary Cap Year that covers a Season that follows the player’s 38th birthday, whichever is later, shall be attributed to the prior Salary Cap Years pro rata on the basis of the Salaries for such prior Salary Cap Years.”

> “Notwithstanding Section 3(a)(2)(i) above, there shall be no re-allocation of Salaries pursuant to this Section 3(a)(2) for any Contract between a Qualifying Veteran Free Agent and his Prior Team covering four (4) or fewer Seasons entered into by a player at age 35 or 36.”

## I-08 — Inferred contract and operation timing

**Competing readings:** Leave an omitted signing year or operation date unknown; or use the current 2024-25 cap year as the transaction year and infer an old signing year from its stated length when needed to determine whether the old contract expired.

**Chosen reading:** Undated operations occur in 2024-25. For a historical contract without a signing year, use `2024 − stated term` as its signing year, the earliest year that makes its final stated season 2023-24. Explicit years and periods always take precedence. Because a missing day/date cannot prove a timing violation, date-dependent restrictions are applied only when the operation supplies enough timing detail, except that a linked sign-and-trade is treated as a pre-Regular-Season signing as stated in I-17.

**Exact supporting sentences:**

> “the Salary Cap for the current (2024-25) NBA Salary Cap Year is $140,588,000”

> “Player A signed a 2-year contract with Team B providing the minimum salary.”

## I-09 — Contract term when only annual pay or raises are described

**Competing readings:** Treat a stated first salary and yearly raise as a complete contract term; or infer only the shortest term that gives the stated annual schedule meaning.

**Chosen reading:** If no term is stated, use two years when the source states a first-year salary and a later annual raise. If the text states annual salaries for more years, use the latest stated year. Do not invent additional seasons, bonuses, or options.

**Exact supporting sentence:**

> “A. Team A signs a 2-year contract with Player A providing annual salary $38,000,000 in the first Salary Cap Year (2024-2025) and 7% increase per year, execute the transaction in in January of 2025.”

## I-10 — Options

**Competing readings:** Treat an option as an extra season beyond the stated term, presume an unmentioned option was declined, or keep it within the stated term and exercised unless the facts say otherwise.

**Chosen reading:** Count option seasons within the stated contract term. Treat a stated team or player option as exercised unless the problem explicitly says it was declined; this gives an unexercised option effect only where the text records the decision. In an apron projection, apply the CBA’s express exercise assumption.

**Exact supporting sentences:**

> “For the avoidance of doubt and consistent with Article VII, Section 9(a)(2), the maximum Contract and Extension lengths described herein are inclusive of any Option Year contained in a Contract or Extension.”

> “all Team or Player Options in respect of such Subsequent Salary Cap Year are exercised”

> “Player A just decided not to exercise the player option.”

## I-11 — Annual salaries, raises, and rounding

**Competing readings:** Apply a stated raise percentage to the prior year’s salary, or to the first-year salary; use a fixed 5% rule for every contract, or select the applicable contract class.

**Chosen reading:** Generate unstated annual salaries by applying the stated percentage to the first-year salary each year. Validate each annual change against the CBA maximum for the relevant class: 5% for ordinary contracts, 8% for eligible Prior Team contracts/extensions. Round generated dollar amounts to the nearest dollar for checks. Explicit annual salaries are checked as stated.

**Exact supporting sentences:**

> “For each Salary Cap Year covered by a Player Contract after the first Salary Cap Year, the player’s: (A) Salary, excluding Incentive Compensation, may increase or decrease in relation to the previous Salary Cap Year’s Salary, excluding Incentive Compensation, by no more than five percent (5%) of the Salary for the first Salary Cap Year covered by the Contract; and (B) Regular Salary may increase or decrease in relation to the previous Salary Cap Year’s Regular Salary by no more than five percent (5%) of the Regular Salary for the first Salary Cap Year covered by the Contract.”

> “For each Salary Cap Year covered by a Player Contract after the first Salary Cap Year, the player’s: (A) Salary, excluding Incentive Compensation, may increase or decrease in relation to the previous Salary Cap Year’s Salary, excluding Incentive Compensation, by no more than eight percent (8%) of the Salary for the first Salary Cap Year covered by the Contract; and (B) Regular Salary may increase or decrease in relation to the previous Salary Cap Year’s Regular Salary by no more than eight percent (8%) of the Regular Salary for the first Salary Cap Year covered by the Contract.”

## I-12 — No unstated compensation or protections

**Competing readings:** Assume unmentioned bonuses, signing bonuses, incentives, or individually negotiated protections; or check only stated compensation terms.

**Chosen reading:** No unstated bonus or incentive is added. Unless the facts expressly state a contrary term, the standard NBA contract is treated as containing no bonus and as fully protected for lack of skill and injury or illness where the CBA requires those terms. An explicit bonus or less-than-full protection term fails the special offer-sheet condition. For a sign-and-trade, an explicit unprotected term fails.

**Exact supporting sentence:**

> “(e) (1) Subject to the rules set forth in Section 2(e) above, a Veteran Free Agent and his Prior Team may enter into a Player Contract pursuant to an agreement between the Prior Team and another Team concerning the signing and subsequent trade of such Contract, but only if (i) the Veteran Free Agent finished the prior Season on his Prior Team’s roster, (ii) the Contract is for at least three (3) Seasons (excluding any Option Year) but no more than four (4) Seasons in length, (iii) the Contract is not signed pursuant to the Non-Taxpayer Mid-Level Salary Exception or the Mid-Level Salary Exception for Room Teams, (iv) the first Season of the Contract is fully protected for lack of skill, (v) the Contract is entered into prior to the first day of the Regular Season, (vi) with respect to any 5th Year Eligible Player (as defined in Article II, Section 7) who met one of the Higher Max Criteria (as defined in Article II, Section 7), the Contract may not provide the player with Salary (plus Unlikely Bonuses) in excess of twenty-five percent (25%) of the Salary Cap (as calculated pursuant to Article II, Section 7) in effect at the time the Contract is signed, and (vii) the acquiring Team has Room for the player’s Salary plus any Unlikely Bonuses provided for in the first Season of the Contract.”

> “If the Offer Sheet provides for Salary for the third Salary Cap Year in accordance with the foregoing sentence, then, subject to Section 5(d)(iii) below, (A) the player’s Salary for the fourth Salary Cap Year may increase or decrease in relation to the third Salary Cap Year’s Salary by no more than four and five tenths percent (4.5%) of the Salary for the third Salary Cap Year, (B) the Offer Sheet cannot contain bonuses of any kind, and (C) the Offer Sheet must provide for one hundred percent (100%) of the Base Compensation in each Season to be protected for lack of skill and injury or illness (with no individually-negotiated conditions or limitations on such protection).”

## I-13 — Exception selection when an operation names none

**Competing readings:** Reject a transaction if the operation does not name a salary-cap exception; or evaluate the CBA routes and accept one that fits.

**Chosen reading:** Evaluate Room and the available exceptions in deterministic order subject to salary, term, prior-team rights, use, and apron restrictions. An operation need not name the exception because the user prompt asks the solver to identify it.

**Exact supporting sentence:**

> “A Team’s Team Salary may not exceed the Salary Cap at any time unless the Team is using one of the Exceptions set forth in Section 6 below.”

## I-14 — Offer-sheet backload

**Competing readings:** Permit the special third-year salary on any 1–2 Years of Service offer sheet; or permit it only when the first two years use the maximum allowed amount.

**Chosen reading:** For a player with one or two Years of Service, the first-year maximum is the NTMLE. The second-year maximum is that first-year amount plus the ordinary 5% increase allowed by Article VII, Section 5(a)(1). A third-year amount above the ordinary 5% rise uses the special maximum-salary provision only when both of those first two years are at their respective maximums. When that backload is used, enforce the stated fourth-year 4.5% limit and the no-bonus/full-protection terms. Otherwise enforce ordinary annual changes. A flat second year at the NTMLE is not the maximum second-year salary.

The competing reading is that both first-year amounts are at the flat NTMLE amount because Section 5(d)(i) names that figure. I choose the first-year NTMLE and second-year 105% maximum because Section 5(d)(i) expressly subjects annual increases to Article VII, Section 5(a)(1), which permits up to a 5% increase from the first-year salary. “Maximum allowable amount” for the first two years includes that permitted increase. The annual-change check is also applied independently.

**Exact supporting sentences:**

> “Notwithstanding any other provision of this Agreement, no such Offer Sheet may provide for Salary plus Unlikely Bonuses in the first Salary Cap Year totaling more than the amount of the Non-Taxpayer Mid-Level Salary Exception for such Salary Cap Year. Annual increases or decreases in Salary and Unlikely Bonuses shall be governed by Article VII, Section 5(a)(1).”

> “For each Salary Cap Year covered by a Player Contract after the first Salary Cap Year, the player’s: (A) Salary, excluding Incentive Compensation, may increase or decrease in relation to the previous Salary Cap Year’s Salary, excluding Incentive Compensation, by no more than five percent (5%) of the Salary for the first Salary Cap Year covered by the Contract; and (B) Regular Salary may increase or decrease in relation to the previous Salary Cap Year’s Regular Salary by no more than five percent (5%) of the Regular Salary for the first Salary Cap Year covered by the Contract.”

> “If an Offer Sheet provides for the maximum allowable amount of Salary for the first two (2) Salary Cap Years pursuant to Section 5(d)(i) above, then, subject to Section 5(d)(iii) below, the Offer Sheet may provide for Salary for the third Salary Cap Year of up to the maximum amount that the player would have been eligible to receive for the third Salary Cap Year absent the restriction in the first sentence of Section 5(d)(i) above and had the player’s Salary for the first two (2) Salary Cap Years been the maximum amount permitted under Article II, Section 7(a) and Article VII, Section 5(b)(1).”

> “If the Offer Sheet provides for Salary for the third Salary Cap Year in accordance with the foregoing sentence, then, subject to Section 5(d)(iii) below, (A) the player’s Salary for the fourth Salary Cap Year may increase or decrease in relation to the third Salary Cap Year’s Salary by no more than four and five tenths percent (4.5%) of the Salary for the third Salary Cap Year, (B) the Offer Sheet cannot contain bonuses of any kind, and (C) the Offer Sheet must provide for one hundred percent (100%) of the Base Compensation in each Season to be protected for lack of skill and injury or illness (with no individually-negotiated conditions or limitations on such protection).”

## I-15 — Matching an offer sheet

**Competing readings:** Read Article XI, Section 5(c)’s list as exhaustive for every restricted free agent; or also apply the specific Non-Taxpayer Mid-Level Exception permission for a Veteran Free Agent with one or two Years of Service. For a match, one could also charge both the pre-match hold and the signed contract salary, or replace the hold.

**Chosen reading:** Allow Room, a Section 6(b) Veteran Free Agent Exception, or the Minimum Player Salary Exception as Article XI, Section 5(c) says. Also allow the Non-Taxpayer Mid-Level Exception for a Veteran Free Agent with one or two Years of Service because Article VII, Section 6(e)(5) expressly permits that use to match an Offer Sheet. Enforce the exception amount and apron limits. When the ROFR Team matches, remove the hold and add the matched contract salary.

**Exact supporting sentences:**

> “The ROFR Team may match an Offer Sheet by using, as applicable, Room, a Veteran Free Agent Exception set forth in Article VII, Section 6(b), or the Minimum Player Salary Exception.”

> “Notwithstanding anything to the contrary in Section 6(e)(3) above, if a Veteran Free Agent with one (1) or two (2) Years of Service receives an Offer Sheet in accordance with the provisions of Article XI, Section 5(d), the player’s Prior Team may use the Non-Taxpayer Mid-Level Salary Exception to match the Offer Sheet.”

> “If the ROFR Team exercises its Right of First Refusal, the player’s Salary for each Salary Cap Year covered by the Contract with the ROFR Team shall be the Salary for such Salary Cap Year as set forth in the Contract.”

## I-16 — Trade salary matching and transaction order

**Competing readings:** Apply the route based on the team’s starting salary or the salary after the trade; allow all routes available to an over-cap team to a below-cap team; or apply the specific room/standard/aggregate/expanded route and its post-trade limits.

**Chosen reading:** Evaluate each team’s salary after the incoming and outgoing players, and choose the route based on its pre-trade status and transaction type. For Section 6(j)(1)(v), a below-cap team’s Room is measured after the simultaneous outgoing assignments reduce Team Salary and before incoming assignments add Salary; compare that Room plus $250,000 to the full incoming post-assignment Salaries. A below-cap team may instead use the Transition or Expanded route where Section 6(j)(2) permits it and the formula passes. Apply the $250,000 allowance unless post-assignment salary would exceed the First Apron, when the allowance is zero. Trade player salaries use their 2024-25 attributed salaries, and an assigned contract’s full Salary is included in the assignee’s Team Salary. A player’s free-agent hold remains in a team’s salary unless that player’s status changes as described in I-01.

**Exact supporting sentences:**

> “(i) Standard Traded Player Exception. Subject to the rules set forth in Section 2(e) above, a Team may use the “Standard Traded Player Exception” to replace one (1) Traded Player with one (1) or more Replacement Players whose Player Contracts are acquired simultaneously or non-simultaneously and whose post-assignment Salaries for the Salary Cap Year in which the Replacement Player(s) are acquired, in the aggregate, are no more than an amount equal to one hundred percent (100%) of the pre-trade Salary of the Traded Player, plus $250,000, provided that any Player Contract acquired non-simultaneously pursuant to this Exception must be acquired within one (1) year following the date on which the Traded Player was traded.”

> “(ii) Aggregated Standard Traded Player Exception. Subject to the rules set forth in Section 2(e) above, a Team may use the “Aggregated Standard Traded Player Exception” to replace two (2) or more Traded Players with one (1) or more Replacement Players whose Player Contracts are acquired simultaneously and whose post-trade Salaries for the then-current Salary Cap Year, in the aggregate, are no more than an amount equal to one hundred percent (100%) of the aggregated pre-trade Salaries of the Traded Players, plus $250,000.”

> “Except as provided in Section 6(j)(2) below, and notwithstanding Section 6(n) below, a Team with a Team Salary below the Salary Cap may acquire one (1) or more players by assignment whose post-assignment Salaries, in the aggregate, are no more than an amount equal to the Team’s room under the Salary Cap plus $250,000.”

> “In lieu of conducting a trade in accordance with Section 6(j)(1)(v) above, and notwithstanding Section 6(n) below and subject to Section 2(e) above and Section 6(j)(6) below, a Team with a Team Salary below the Salary Cap may conduct a trade in accordance with Sections 6(j)(1)(iii)-(iv) above.”

> “Notwithstanding anything to the contrary in Section 6(j)(1) above, if a Team’s post-assignment Team Salary would exceed the First Apron Level, then the $250,000 allowance referenced in each of Sections 6(j)(1)(i)-(v) above shall be reduced to $0.”

The text does not expressly state the measurement instant for “the Team’s room” in Section 6(j)(1)(v). The chosen reading measures Room after outgoing assignments and before incoming assignments. Section 6(j)(1)(v) speaks of “post-assignment Salaries” and does not say “pre-trade” (unlike Sections 6(j)(1)(i)-(iv), which expressly use “pre-trade” Salaries); using post-outgoing Room also lets the room route account for the net Team Salary resulting from the simultaneous transaction. Section 6(j)(2) provides Transition or Expanded routes “in lieu” when a below-cap team elects those formulas.

## I-17 — Sign-and-trade linkage and missing date

**Competing readings:** Treat a signing and a trade of the same player within one operation as independent actions; or link them when the operation describes the signing and subsequent trade as one transaction. An undated sign-and-trade could be treated as occurring after the Regular Season, or as satisfying the required pre-season timing. For the acquiring Team’s Room test, one could use its Room before the simultaneous trade assignments or deduct outgoing player salaries first.

**Chosen reading:** Link only the signing and subsequent trade of the same player in the same operation. When the operation provides no date, assume the linked sign-and-trade occurs before the Regular Season. Measure the acquiring Team’s Room after the same transaction’s outgoing player assignments and before adding the signed-and-traded player, consistent with measuring available Room at the point that player is assigned. Section 8(e)(1)(vii) requires Room for that player’s first-season Salary and bonuses; it does not grant the Section 6(j)(1)(v)’s separate $250,000 allowance. Check the stated contract, Prior Team status, first-season protection, and apron conditions as well. Do not link separate operation letters.

**Exact supporting sentences:**

> “a Veteran Free Agent and his Prior Team may enter into a Player Contract pursuant to an agreement between the Prior Team and another Team concerning the signing and subsequent trade of such Contract”

> “the Contract is entered into prior to the first day of the Regular Season”

> “the acquiring Team has Room for the player’s Salary plus any Unlikely Bonuses provided for in the first Season of the Contract.”

> “a Team with a Team Salary below the Salary Cap may acquire one (1) or more players by assignment whose post-assignment Salaries, in the aggregate, are no more than an amount equal to the Team’s room under the Salary Cap plus $250,000.”

> “any Team with Room may enter into a Player Contract that calls for a Salary in the first Salary Cap Year covered by such Contract that would not exceed the Team’s then-current Room.”

## I-18 — Draft-pick holdings and “following” years

**Competing readings:** Treat an unlisted pick as owned, not owned, or unknown; count the current draft/season within a “following 7 years” period, or count the next seven future drafts.

**Chosen reading:** Use explicit pick holdings and explicit “its”/“their” operation wording to establish ownership. Where the prompt gives no inventory for a round, do not invent a contrary holding fact; a pick described as the team’s own is treated as owned unless another fact says otherwise. “Following 7 years” from the stated 2024-25 season means drafts 2025 through 2031. A foreign pick counts for the receiving team as an asset but retains its original owner identity.

**Exact supporting sentences:**

> “Team A trades its first-round draft pick in 2025 and second-round draft pick in 2027 to Team C for its first-round draft picks in 2029.”

> “Team A has all its first-round draft picks in the following 7 years”

## I-19 — Stepien and second-apron draft-pick freeze

**Competing readings:** Check only consecutive first-round picks explicitly listed, or evaluate the complete known future first-round rights book; project second-apron status in later years, or use only the current status supplied.

**Chosen reading:** Require at least one first-round selection in each pair of consecutive future drafts across the known post-trade rights book. Use the current second-apron status for the freeze and do not predict future apron status without future salary facts. The first draft after seven seasons following 2024-25 is 2032.

**Exact supporting sentences:**

> “No Team may sell its rights to select a player in the first round of any NBA Draft for cash or its equivalent, or trade or exchange its right to select a player in the first round of any NBA Draft if the result of such trade or exchange may be to leave the Team without first-round picks in any two (2) consecutive future NBA Drafts.”

> “the Team shall be prohibited from trading (either conditionally or unconditionally) its first round draft pick in the first NBA Draft that occurs following the seventh Season that follows the Season occurring within such Salary Cap Year”

## I-20 — Operation order, rollback, and tie-breaking

**Competing readings:** Apply each operation independently against the original situation, or carry successful earlier transactions forward. If multiple teams violate in one operation, choose by team-letter order or by a stable transaction role.

**Chosen reading:** Process operation letters in alphabetical order and transactions in source order; successful earlier operations update state. If any transaction in one operation fails, roll back that operation before checking the next letter. If several teams fail checks in the same operation, report the team on the first failed check in deterministic transaction and rule-evaluation order. The CBA specifies which operation to report but does not prescribe a team tie-break, so using the first failed check is a reproducible default that follows the order in which the checker evaluates the operation and is independent of team-letter sorting.

**Exact supporting sentence:**

> “If several violations exist, report the first violating operation in letter order (and its violating team).”

## I-21 — Cash-trade apron test timing

**Competing readings:** Apply the Second Apron ceiling to the Team Salary immediately before a cash trade is processed, or apply it to Team Salary immediately following the complete trade transaction.

**Chosen reading:** Test the paying team’s Team Salary after the trade’s player assignments. The Transaction Restrictions Table rule is expressly triggered by the transaction, and Section 2(e)(2)(i)(A) tests Team Salary “immediately following such transaction.” A pre-trade salary above the Second Apron does not alone bar payment if outgoing assignments bring the payer below it; the payer remains subject to the row I ceiling for the rest of the Salary Cap Year. The row applies to the team that pays cash; receiving cash alone is not row I.

**Exact supporting sentences:**

> “A Team may not engage in a transaction set forth in the Transaction Restrictions Table if, immediately following such transaction, the Team’s Team Salary for such Salary Cap Year would exceed the ‘Applicable Apron Level’ that corresponds with such transaction in the table.”

> “I. Team pays cash to another Team in connection with a trade in accordance with Section 8(a) below — Applicable Apron Level: Second Apron Level”

> “A Team that engages in a transaction set forth in the Transaction Restrictions Table may not, for the remainder of such Salary Cap Year, have an Team Salary that exceeds the Applicable Apron Level that corresponds with such transaction in the table.”

## I-22 — Salary and exception use in a linked sign-and-trade

**Competing readings:** Use the signed contract’s actual salary in current-trade matching and reserve Section 6(j)(5)'s deemed amount for a later Traded Player Exception; or calculate the assignor’s exception using the Section 6(j)(5) deemed amount even when replacement players are acquired in the same trade. A related question is whether row J's second-apron restriction applies only when that resulting exception is used in a later transaction, or also when it is used for simultaneous replacement players.

**Chosen reading:** The linked signing must independently satisfy the basic cap rule: the signing Team uses available Room or the applicable Section 6(b) prior-team Veteran Free Agent Exception. Section 8(e)(1) authorizes the linked signing and trade structure but is not itself a salary-cap exception. When Section 6(j)(5)'s stated conditions are met, use its deemed amount to calculate the assignor's exception, including a replacement acquisition made simultaneously with the sign-and-trade. Section 6(j)(1) expressly permits replacement-player contracts to be acquired “simultaneously or non-simultaneously”; Section 6(j)(5) changes the Salary used “for purposes of calculating” that exception and does not limit the adjustment to a later transaction. If the team uses that exception to acquire replacement players in the same trade, row J also applies because the exception is in respect of the player contract signed and traded under Section 8(e)(1). Use actual contract salary for the Team Salary ledger. When the ordinary Standard limit is insufficient, another exception expressly available for that trade, including Expanded, may be selected if its own formula and apron conditions are satisfied.

**Exact supporting sentence:**

> “If (x) a Qualifying Veteran Free Agent or Early Qualifying Veteran Free Agent and his prior Team enter into a Player Contract, in accordance with Section 6(b)(1) or (3) above, in connection with an agreement to trade the Contract in accordance with Section 8(e) below, (y) the Team’s Team Salary immediately following such Contract signing is above the Salary Cap, and (z) the new Contract to be traded provides for Salary and Unlikely Bonuses for the first Season of such Contract in excess of the Salary and Unlikely Bonuses that could have been provided for by the Contract had the player been a Non-Qualifying Veteran Free Agent and the Contract had been signed pursuant to Section 6(b)(2) above, then for purposes of calculating the assignor Team’s Traded Player Exception, the player’s Salary shall be deemed equal to the greater of (i) the Salary for the last Season of his preceding Contract, or (ii) fifty percent (50%) of the Salary for the first Season of his new Contract.”

> “A Team’s Team Salary may not exceed the Salary Cap at any time unless the Team is using one of the Exceptions set forth in Section 6 below.”

> “If the player is a Qualifying Veteran Free Agent, the new Player Contract may provide for Salary plus Unlikely Bonuses in the first Salary Cap Year totaling up to the maximum amount provided for in Article II, Section 7.”

> “If the player is a Non-Qualifying Veteran Free Agent, then, subject to Article II, Section 7, the new Player Contract may provide in the first Salary Cap Year up to the greater of: (i) one hundred twenty percent (120%) of the Regular Salary for the final Salary Cap Year of the player’s prior Contract, plus one hundred twenty percent (120%) of any Likely Bonuses and Unlikely Bonuses, respectively, called for in the final Salary Cap Year covered by the player’s prior Contract; (ii) Salary plus Unlikely Bonuses totaling one hundred twenty percent (120%) of the then-current Minimum Annual Salary applicable to the player; or (iii) in the case of a Contract between a Team and its Restricted Free Agent, the Salary and Unlikely Bonuses required to be provided in a Qualifying Offer.”

> “If the player is an Early Qualifying Veteran Free Agent, the new Player Contract must cover at least two (2) Seasons (not including a Season covered by an Option Year) and, subject to Article II, Section 7, may provide in the first Salary Cap Year up to the greater of: (A) one hundred seventy-five percent (175%) of the Regular Salary for the final Salary Cap Year covered by his prior Contract, plus one hundred seventy-five percent (175%) of any Likely Bonuses and Unlikely Bonuses, respectively, called for in the final Salary Cap Year covered by the player’s prior Contract, or (B) Salary plus Unlikely Bonuses totaling an amount equal to one hundred five percent (105%) of the Average Player Salary for the prior Salary Cap Year (or if the Audit Report for the prior Salary Cap Year has not been completed, one hundred five percent (105%) of the Average Player Salary for the prior Salary Cap Year as computed by substituting Estimated Total Salaries (as defined in Section 1(i) above) for Total Salaries).”

> “Subject to the rules set forth in Section 2(e) above, a Team may use the ‘Standard Traded Player Exception’ to replace one (1) Traded Player with one (1) or more Replacement Players whose Player Contracts are acquired simultaneously or non-simultaneously and whose post-assignment Salaries for the Salary Cap Year in which the Replacement Player(s) are acquired, in the aggregate, are no more than an amount equal to one hundred percent (100%) of the pre-trade Salary of the Traded Player, plus $250,000, provided that any Player Contract acquired non-simultaneously pursuant to this Exception must be acquired within one (1) year following the date on which the Traded Player was traded.”

> “J. Team acquires a player using a Traded Player Exception (as described in Section 6(j)(1)(i), (ii), (iii), or (iv) below), which Traded Player Exception is in respect of a Player Contract signed and traded pursuant to Section 8(e)(1) below — Applicable Apron Level: Second Apron Level”

## I-23 — Minimum salary outside the Minimum Player Salary Exception

**Competing readings:** Treat the Minimum Player Salary schedule as a universal floor for every signing and Offer Sheet, or apply the schedule only where the supplied CBA text makes it a condition, including the Minimum Player Salary Exception and the specified Free Agent Amount rules.

**Chosen reading:** The supplied excerpt does not state a general minimum-pay rule for all Player Contracts. The code therefore does not reject a salary below the service-tier schedule solely on that basis. It still enforces equality to the applicable minimum and the two-season/no-bonus limits when a Team uses the Minimum Player Salary Exception, and uses the schedule where the excerpt expressly uses it for another calculation. This avoids applying the Minimum Player Salary Exception clause as though it were a universal salary floor.

**Exact supporting sentence:**

> “A Team may sign a player to, or acquire by assignment, a Player Contract, not to exceed two (2) Seasons in length, that provides for a Salary for the first Season equal to the Minimum Player Salary applicable to that player (with no bonuses of any kind).”

## I-24 — Overlap between Qualifying and Early Qualifying Veteran Free Agent definitions

**Competing readings:** A player whose contract covered each of the three preceding Seasons with his Prior Team also literally meets the Early Qualifying definition’s two-season wording, so both exception tiers could apply; or treat the status terms as a hierarchy, applying Qualifying status when the three-season test is met and Early Qualifying status only when that longer test is not met.

**Chosen reading:** Apply Qualifying Veteran Free Agent status when the three-season test is met. Use Early Qualifying status only when the player fails that test but meets the two-season test. The supplied text does not expressly say “but is not a Qualifying Veteran Free Agent” in the Early Qualifying definition; the hierarchy is inferred from “Early Qualifying,” the separate and different Section 6(b) salary limits, and the Non-Qualifying definition’s explicit exclusion of both higher tiers. The more specific three-season qualification controls when both descriptions otherwise fit.

**Exact supporting sentences:**

> “Early Qualifying Veteran Free Agent” means a Veteran Free Agent who, prior to becoming a Veteran Free Agent, played under one (1) or more Player Contracts covering some or all of each of the two (2) preceding Seasons, and who either played exclusively with his Prior Team during such two (2) Seasons, or, if he played for more than one (1) Team during such period, changed Teams only (i) by means of trade, (ii) by means of assignment via the NBA’s waiver procedures, or (iii) by signing with his Prior Team during the first of the two (2) Seasons.

> “Qualifying Veteran Free Agent” means a Veteran Free Agent who, prior to becoming a Veteran Free Agent, played under one (1) or more Player Contracts covering some or all of each of the three (3) preceding Seasons, and who either played exclusively with his Prior Team during such three (3) Seasons, or, if he played for more than one (1) Team during such period, changed Teams only (i) by means of trade, (ii) by means of assignment via the NBA’s waiver procedures during the first of the three (3) Seasons, or (iii) by signing with his Prior Team during the first of the three (3) Seasons.

> “Non-Qualifying Veteran Free Agent” means a Veteran Free Agent who is not a Qualifying Veteran Free Agent or an Early Qualifying Veteran Free Agent.

## I-25 — Consent for trading a one-year veteran contract

**Competing readings:** Infer a player’s consent from the fact that an operation says the Team trades him, or require the prompt to establish consent or an agreed waiver because the CBA makes consent a condition. A linked sign-and-trade may be treated as consent to that identified trade, or the separate consent condition may still require its own express fact.

**Chosen reading:** For an ordinary trade, require an express consent statement in the contract or trade description, or an express agreement at signing eliminating the right; silence does not establish consent. For a linked sign-and-trade expressly described as signing and subsequent trade in the same operation, treat the player’s signing as consent to that identified subsequent trade only. Apply the restriction when the active contract has one non-option Season and the supplied contract history shows that the player would have Qualifying or Early Qualifying Veteran Free Agent status with the assigning Team upon completing it. The CBA does not prescribe how consent must be evidenced in a fact pattern that omits it; the chosen rule does not infer it from the mere fact that a trade is proposed.

**Exact supporting sentences:**

> “A player (other than a Two-Way Player) with a one-year Contract (excluding any Option Year) who would be a Qualifying Veteran Free Agent or an Early Qualifying Veteran Free Agent upon completing the playing services called for under his Contract cannot be traded without the player’s consent; provided, however, that in accordance with Article II, Section 3(h) above, the player and Team may agree at the time of signing such Contract that the player’s right to consent to a trade pursuant to this Section 8(b) shall be eliminated.”

> “Should the player consent (or if the player and Team agreed at the time of signing to eliminate his right to consent) and the player is traded (except if the Contract has an Option for the second year that was exercised prior to the trade), then, for purposes of determining whether the player is a Qualifying Veteran Free Agent, Early Qualifying Veteran Free Agent, or Non-Qualifying Veteran Free Agent at the conclusion of the Contract or any subsequent Contract between the player and the assignee Team, the player shall be considered as having changed Teams by means of signing a Contract with the assignee Team as a Free Agent (and not by means of trade).”

> “a Veteran Free Agent and his Prior Team may enter into a Player Contract pursuant to an agreement between the Prior Team and another Team concerning the signing and subsequent trade of such Contract”

## Independent disagreements reviewed

- **Minimum-salary trace clause:** The generic salary-floor check was removed because the supplied text states only the Minimum Player Salary Exception’s exact salary and term conditions; it does not make that exception a universal pay floor. The exception still checks its own minimum amount and term when used.
- **`nba_L1_001` Operation A:** “minimum applicable annual salary plus $200,000” means first-year Salary equal to the applicable minimum plus $200,000. It is not the Minimum Player Salary Exception: Article VII, Section 6(a)(i) requires a first-season Salary “equal to the Minimum Player Salary applicable to that player (with no bonuses of any kind).” The amount is $3,495,528 for Player C, exceeds the applicable minimum by $200,000, and is instead checked against the available Non-Taxpayer Mid-Level Exception; Team B remains below the First Apron after signing. The prior parse dropped the word “plus” amount and incorrectly passed the minimum exception.
- **Offer sheets `nba_L0_054` and `nba_L0_073`:** Section 5(d)(i) caps year one at the NTMLE but sends annual changes to Section 5(a)(1), so the maximum second-year salary is 105% of year one. `nba_L0_054` uses that maximum second year and may use the special third-year salary, subject to the fourth-year 4.5% condition. `nba_L0_073` keeps year two flat at the NTMLE, below its permitted maximum; its $30 million third year therefore violates the ordinary 5% raise rule.
- **Cash trade `nba_L0_062`:** A cash payer’s apron test is applied after outgoing and incoming player assignments, under Article VII, Section 2(e)(2)(i)(A). The old check tested before the player movements and could reject a trade whose post-trade Team Salary is below the Second Apron; that check now runs against the post-transaction salary and only for the payer.
- **Linked sign-and-trades and below-cap recipient trades (`nba_L0_027`, `nba_L0_032`, `nba_L0_034`, `nba_L0_035`, `nba_L0_062`, `nba_L0_064`, and related cases):** Section 6(j)(1)(v) compares the full incoming post-assignment Salaries with Room after the team’s outgoing assignments. The sentence uses “post-assignment Salaries” and does not specify pre-trade Room, while adjacent Sections 6(j)(1)(i)-(iv) expressly refer to “pre-trade” salary. In `nba_L0_027`, Team B starts with $10,088,000 Room and sends out a $16,800,000 player; after that assignment it has $26,888,000 Room, and its $27,000,000 incoming salary is within Room plus $250,000 (final Team Salary is $140,700,000, just $112,000 above the $140,588,000 cap). Section 8(e)(1)(vii)’s sign-and-trade test likewise measures Room after the recipient’s simultaneous outgoing assignments and before the signed player is assigned; for `nba_L0_032`, Team B’s $14,588,000 initial Room plus $31,000,000 outgoing salary gives $45,588,000 Room for the $42,100,000 signed player. Assigned contracts are separately traced at their full current-year salary under Section 4(c). The Room trade check traces the operative “post-assignment Salaries” sentence, rather than the subsection heading. The earlier pre-trade-Room interpretation is withdrawn: outgoing assignments change the recipient’s Team Salary before incoming Salaries are counted in the same transaction.
- **`nba_L1_005`:** Article VII, Section 4(a)(2) includes the Veteran Free Agent Amount until the player re-signs, signs elsewhere, or is renounced. In `nba_L1_005`, Team B’s expired Player B contract contributes its Free Agent Amount on top of the stated $160 million, placing Team B above the First Apron and making the Non-Taxpayer Mid-Level Exception unavailable. An NTMLE reference does not override this explicit Team Salary hold. Sign-and-trade Room is resolved under I-17; the separate $250,000 room-trade allowance does not apply to Section 8(e)(1)(vii).
- **`nba_L0_002`, `nba_L0_040`, and `nba_L0_043`:** The disagreement appears to omit the Over-38 salary attribution. The stated draft ages and years imply a covered season after age 38 under I-06’s age proxy. Article VII, Section 3(a)(2)(i) expressly reallocates that salary to prior years. The higher first-year charge is retained when that charge exceeds the signing team’s Room.
- **`nba_L0_027`:** Re-reading Section 6(j)(1)(v) after the independent disagreement changed the previous reading. Team B’s $16,800,000 outgoing assignment increases Room from $10,088,000 to $26,888,000 before it receives $27,000,000, which is within the $250,000 allowance. The net post-trade Team Salary is $140,700,000, within the Salary Cap plus $250,000. The room route therefore passes; Expanded TPE need not be used.
- **`nba_L0_020`:** The First Apron limit continues for the remainder of the Salary Cap Year after a row B transaction. Article VII, Section 2(e)(2)(i)(B) expressly imposes that continuing ceiling, so the later salary increase that crosses it remains a violation.
- **`nba_L0_038`:** The player has two Years of Service and a qualifying Offer Sheet. Article VII, Section 6(e)(5) expressly permits the Prior Team to use the Non-Taxpayer Mid-Level Exception to match such an Offer Sheet, despite Article XI, Section 5(c)’s general list. The match is now allowed within that exception’s amount and apron limits.
- **`nba_L1_082`:** The stated Traded Player Exception arose in 2022-23 and is not available for the 2024-25 operation. Article VII, Section 6(j)(4) limits a Traded Player Exception’s life to one year.
- **`nba_L1_037`:** Operation C has a first-round pick tradeability failure for Team B and cash-volume failures for both teams. The team tie-break is not supplied by the CBA; the solver now reports the team on the first failed check, which is the pick-tradeability check for Team B. The previous special priority for cash checks selected Team A even though the pick failure is evaluated first.
- **One-year contracts (`nba_L1_001` and related cases):** Article VII, Section 8(b) bars a trade without player consent when a one-year contract would make the player QVA or EQVA at completion. The affected operation has no consent statement or waiver, so the trade fails; a trade described merely as a Team action does not establish the player’s consent. An expressly linked sign-and-trade is treated as consent to that identified subsequent trade under the linked-agreement language in Section 8(e)(1); the code checks future QVA/EQVA status from the supplied contract coverage and traces Section 8(b).
- **`nba_L0_005`, `nba_L0_008`, and `nba_L0_012`:** The disagreement follows from expiring salaries being excluded while Free Agent Amounts remain included by Article VII, Section 4(a)(2) and Section 4(d). The hold is included until the player signs or is renounced; that can remove Room or trigger an apron restriction before a later operation.
- **`nba_L0_013`, `nba_L0_016`, and `nba_L0_018`:** Salary matching is reevaluated after adding the hold for a described expiring free agent. The applicable trade formula and apron rule are applied to the resulting salary; the hold is not silently dropped because the old playing contract expired.
- **Offer-sheet backload cases:** The special third-year rule is applied when the first two years reach their respective maxima: the NTMLE in year one and up to a 5% increase in year two. A flat NTMLE second year is not the maximum second-year salary; an above-ordinary third-year amount in that case fails the ordinary raise limit.
- **Restricted free-agent matching cases:** Article XI, Section 5(c) lists Room, Veteran Free Agent Exceptions, and the Minimum Player Salary Exception. Article VII, Section 6(e)(5) separately and expressly permits the Prior Team to use the Non-Taxpayer Mid-Level Exception to match an Offer Sheet for a player with one or two Years of Service; the solver honors this specific permission and its amount and apron limits.


## I-26 — Assignment of an expired player contract

**Competing readings:** Treat a historical contract record as sufficient to include a player in a trade after the contract has ended; or require that the assigned Player Contract still cover the current Salary Cap Year.

**Chosen reading:** Only an active Player Contract can be assigned in a player trade. The historical record remains relevant to free-agent status, service and salary history, but an expired contract is no longer a trade asset. A linked sign-and-trade is permitted because the new contract is signed before its assignment in the same operation.

**Exact supporting sentences:**

> “For purposes of calculating Team Salary, with respect to any Player Contract that is assigned, the assignee Team shall, upon assignment, have included in its Team Salary the entire Salary for the then-current Salary Cap Year and for all future Salary Cap Years.”

> “a Veteran Free Agent and his Prior Team may enter into a Player Contract pursuant to an agreement between the Prior Team and another Team concerning the signing and subsequent trade of such Contract”

This is applied to `nba_L1_082`, where both named players’ last contracts end before the 2024-25 Salary Cap Year; neither contract can be assigned in Operation A.

## I-27 — Minimum salary for a contract signed in the prior cap year

**Competing readings:** Value a minimum contract signed in 2023 using the 2024-25 minimum schedule at the player’s current service tier; or use the service tier at signing and reconstruct the 2023-24 salary scale from the supplied prior/current cap assumptions.

**Chosen reading:** Use the Years of Service proxy at the contract’s signing year. For a minimum contract signed in 2023, scale that tier’s supplied 2024-25 minimum by the supplied prior-cap/current-cap ratio, then apply the contract’s stated annual raise to later contract years. For current-year signings, use the 2024-25 table directly. This is a reproducible reconstruction because the excerpt names the applicable minimum but does not reproduce the historical schedule.

**Exact supporting sentences:**

> “Player C signed a 2-year contract (minimum applicable player salary, 5% increase per year) with Team G during 2023 Moratorium Period.”

> “the Salary Cap for the prior (2023-24) Salary Cap Year is $136,000,000”

> “the Salary Cap for the current (2024-25) NBA Salary Cap Year is $140,588,000”

For `nba_L0_051`, this puts the 2024-25 salaries of the two minimum-contract players below amounts computed by applying the current schedule at their current service tiers. With the current-year raise, Team D’s incoming salaries fit its room plus the $250,000 allowance under Article VII, Section 6(j)(1)(v).

## Independent disagreements reviewed (current residual set)

- **`nba_L1_005`, Operation A:** Team A begins at $148,000,000, above the $140,588,000 cap. Its $12,000,000 first-year signing is below the $12,821,626 NTMLE amount, is for three years (within the four-year term), and leaves Team Salary at $160,000,000, below the $178,132,000 First Apron. No prior transaction or exception use is stated. Article VII, Section 6(e)(1) permits use up to 9.12% of the cap and row B only imposes a First Apron ceiling. The supplied facts therefore support legality; the `.146` section heading alone does not add another restriction.
- **`nba_L1_015` and `nba_L1_016`, Operation A:** The one-year deal is exactly the applicable minimum with no bonus, so it meets the express Minimum Player Salary Exception. Section 6(i) has no salary-status restriction or apron ceiling, and Section 6(n)(1)'s list of exceptions requiring at-or-above-cap continuity does not include the Minimum Player Salary Exception. The salary-cap exception therefore permits these signings.
- **`nba_L1_017`, Operation D:** Team B used the NTMLE in Operation C. Row B’s First Apron ceiling continues for the remainder of the Salary Cap Year under Article VII, Section 2(e)(2)(i)(B). The later match increases Team Salary to $179,000,000, above $178,132,000, so the match is prohibited even though the player’s Early Qualifying rights could otherwise match the offer.
- **`nba_L1_001` and `nba_L1_002`, tie-breaking:** The operation/team check results agree with the independent implementation, but the first reported failure differs. The prompt orders operations by letter and does not set a tie-break among failing teams within one operation. I retain the deterministic first-failed-check order documented in I-20; this is not a different CBA rule reading.
- **`nba_L1_014`, Operation B:** The first year is at the NTMLE maximum, but the second year is flat rather than at the 5%-increased maximum permitted by Article VII, Section 5(a)(1). Section 5(d)(ii) therefore does not authorize the $15,000,000 third-year salary. The ordinary annual-change limit applies, so the operation remains illegal. The competing flat-NTMLE trigger reading is plausible, but the cross-reference to the annual-change rule supports the maximum-second-year reading in I-14.
- **`nba_L1_038` and `nba_L1_082`:** The named players’ old contracts ended before 2024-25. Article VII, Section 4(c) describes an assignment as the assignment of a Player Contract and counts the contract’s current-year and future Salaries. A historical contract with no current-year term is not an assignable trade asset; the new sign-and-trade contract in `nba_L1_038` remains assignable.
- **`nba_L1_037`, Operation C:** Team B’s pick tradeability check fails before the operation’s cash checks are evaluated. The $5,000,000 paid in Operation A and $2,500,000 paid in Operation C cannot be netted against cash received; Article VIII, Section 8(a) expressly says payments and receipts are not netted. Both teams therefore exceed the cash limit, and Team B also has the first check failure under the deterministic check order in I-20.
- **`nba_L1_080`, Operation B:** The transaction exchanges Team A and Team C first-round picks; it assigns no player contract and does not change Team B’s salary. Team B remains subject to the First Apron ceiling from its earlier sign-and-trade transaction, but its post-Operation-A Team Salary is $137,100,000, below the $178,132,000 ceiling. Section 6(j)(1)(v)’s Room rule does not apply to a pick-only operation, so a Team B failure cannot be grounded in its Room calculation.
- **`nba_L1_005`, Operation A — recheck of the NTMLE disagreement:** The competing reading treats the Non-Taxpayer Mid-Level heading as requiring an additional condition not stated in the operative rule. Team A starts at $148,000,000, above the $140,588,000 cap and below the First Apron; no current-year transaction or exception use precedes Operation A. Its $12,000,000 first-year salary is below the $12,821,626 NTMLE amount, and Team Salary after signing is $160,000,000. Section 6(n)(1) says: “A Team shall be entitled to use the Disabled Player Exception, Bi-annual Exception, Non-Taxpayer Mid-Level Salary Exception, Taxpayer Mid-Level Salary Exception, and a Traded Player Exception set forth in Sections 6(c), (d), (e), (f), and (j) above, respectively, except as set forth in Sections 6(j)(1)(v) and 6(j)(2) above, only if, at the time any such Exception would arise and at all times until it is used, the Team’s Team Salary is at or above the Salary Cap.” Team A meets that requirement on the supplied starting facts, and no earlier operation changes its salary. Section 6(e)(1) grants the NTMLE for signing contracts up to 9.12% of the cap, with a four-season term limit in Section 6(e)(2). Row B gives a First Apron ceiling. Team A’s amount, three-year term, and post-signing salary comply, so Operation A is legal. The `.146` section heading does not add another restriction.
- **`nba_L1_017`, Operation D — recheck of the match/apron disagreement:** The competing reading allows a Right of First Refusal match under Early Bird rights to override the First Apron ceiling already triggered by Team B’s NTMLE signing in Operation C. Section 2(e)(2)(i)(B) directly forecloses that reading: “A Team that engages in a transaction set forth in the Transaction Restrictions Table may not, for the remainder of such Salary Cap Year, have an Team Salary that exceeds the Applicable Apron Level that corresponds with such transaction in the table.” The match raises Team B’s salary to $179,000,000, above $178,132,000. The match right does not erase the expressly continuing ceiling, so Operation D is illegal.
- **`nba_L1_037`, Operation B — recheck of the Team A disagreement:** The operation text says, “Team B signs a 3-year contract with Player D.” Team A does not sign or acquire a player in this operation. Team A did pay $5,000,000 cash in Operation A, so row I applies to Team A; after Operation A its Team Salary is $82,650,000, and it remains unchanged in Operation B. Row I’s ceiling is the Second Apron ($188,931,000). The competing reading treats Team A’s earlier cash payment as prohibiting it from any later operation involving another team. Section 2(e)(2)(i)(B) instead says: “A Team that engages in a transaction set forth in the Transaction Restrictions Table may not, for the remainder of such Salary Cap Year, have an Team Salary that exceeds the Applicable Apron Level that corresponds with such transaction in the table.” Team A stays below its continuing ceiling. The operation is therefore legal for Team A. Team B’s separate signing takes Team B from $155,350,000 to $160,850,000, below the First Apron.
- **`nba_L1_080`, Operation B — recheck:** The operation’s only assets are Team A’s 2025 first-round pick and Team C’s 2028 and 2029 first-round picks. The competing reading treats Team B’s prior First Apron ceiling as barring any later operation in which it is named or affected, even with no Team B assets or salary change. Team B sends and receives nothing; its Team Salary stays at $137,100,000, below the First Apron. Section 2(e)(2)(i)(B) says: “A Team that engages in a transaction set forth in the Transaction Restrictions Table may not, for the remainder of such Salary Cap Year, have an Team Salary that exceeds the Applicable Apron Level that corresponds with such transaction in the table.” It restricts Team B’s salary level rather than unrelated pick transfers between Teams A and C, so Operation B is legal for Team B.
- **`nba_L2_012`, Operation A — exception fallback:** The competing reading treats the prior-team Non-Qualifying Veteran Free Agent exception as the exclusive signing route even when its salary limit is too low. Player C’s $5,000,000 salary exceeds the $3,964,525 Non-Bird limit, but the NTMLE is an independent exception. Section 6(e)(1) states: “A Team may use the Non-Taxpayer Mid-Level Salary Exception to sign and/or acquire by assignment one (1) or more Player Contracts during each Salary Cap Year that, in the aggregate, provide for Salaries and Unlikely Bonuses (or in the case of assignment, post-assignment Salaries and Unlikely Bonuses) in the first Salary Cap Year totaling up to 9.12% of the Salary Cap for such Salary Cap Year; provided, however, that, prior to the first day of the 2024-25 Salary Cap Year, a Team shall not be permitted to use the Non-Taxpayer Mid-Level Salary Exception to acquire a Player Contract by assignment.” Section 6(e)(3) also bars use when the Team has already used the Room Team MLE in that same Salary Cap Year; that is not stated here. Team B has not used its 2024-25 NTMLE; the $5,000,000 contract is one year and leaves Team Salary at $153,087,519, below the First Apron. The prior-team exception limit does not make the NTMLE unavailable. `_choose_exception` now continues to other available exceptions when the prior-team limit does not cover the proposed salary or term.
- **`nba_L1_001` and `nba_L1_002`, first reported team:** The disagreement concerns only the selected team after the same operation is found illegal for multiple teams; operation/team legality agrees. The prompt’s “first violating operation in letter order” gives no rule for choosing between teams in that operation. I retain the deterministic first-failed-check tie-break in I-20 rather than inventing a CBA team priority.
