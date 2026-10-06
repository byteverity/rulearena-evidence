# Interpretations

The checker uses only the supplied `rules.txt`, `prompt_template.txt`, `clauses.json`, and problem text. Where those sources leave a needed input open, the selected reading is listed below.

## Season and Team Salary baseline

**Reading:** Evaluate operations in the 2024-25 Salary Cap Year. A contract signed during a `YYYY Moratorium Period` begins in Salary Cap Year `YYYY`; an `N-year` contract covers that year and the next `N-1` years. The 2023-24 expiring contract salary is already absent from the supplied Team Salary, so it is not removed a second time.

> “the Salary Cap for the current (2024-25) NBA Salary Cap Year is $140,588,000;”

> “the Team Salary of each team listed under "Team Situations:" do not include the amount of contracts that expire at the end of 2023-2024 Salary Cap Year.”

**Reading:** The supplied Team Salary is the starting total with the expiring contract salaries removed. The CBA separately requires Free Agent Amounts for unsigned Veteran Free Agents to count in Team Salary, so the checker adds the amount supported by each player's prior contract and service class. A stated qualifying-offer salary raises that hold when it is larger. A signed contract replaces the player's hold on the prior team; an outstanding offer sheet counts on the new team.

> “With respect to each Veteran Free Agent who last played for a Team who is an Unrestricted Free Agent, the Free Agent Amount (as defined in Section 4(d) below) attributable to such Veteran Free Agent.”

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”

**Reading:** Free Agent Amount uses the Section 4(d) percentage for the derived status (Qualifying, Early Qualifying, or Non-Qualifying), prior salary, the stated average salary, and the stated maximum-salary table. The rules provide no numerical minimum-salary schedule, so a minimum-salary floor that is needed for a hold uses the documented $1,200,000 proxy. Where the source omits a qualifying-offer salary, only the derived Free Agent Amount is used; no offer amount is invented.

> “An Early Qualifying Veteran Free Agent will be included at one hundred thirty percent (130%) of his prior Salary;”

## Review of verifier disagreements

**Readings for nba_L1_014, nba_L1_015, and nba_L1_016:** A contract signed in the 2022 Cap Year covers 2022-23 and 2023-24 when its stated term is two years, so it has ended before the 2024-25 operations. I treat the “minimal annual salary” wording in nba_L1_015 as the same symbolic minimum salary used elsewhere. Team B may sign that one-year, minimum-salary contract under the Minimum Player Salary Exception. In the offer sheets in nba_L1_014 and nba_L1_015, the first two salaries are both the flat Non-Taxpayer MLE amount, not the maximum second-year salary allowed by the ordinary 5% increase. The special RFA third-year form therefore does not apply; the $15,000,000 and $25,000,000 third-year salaries exceed the ordinary raise limit. The $30,000,000 third year in nba_L1_016 also exceeds the ordinary 5% limit. I retain those offer-sheet violations after adding explicit cap-year and salary-schedule extraction.

> “Annual increases or decreases in Salary and Unlikely Bonuses shall be governed by Section 5(a)(1) above.”
>
> “If an Offer Sheet provides for the maximum allowable amount of Salary for the first two (2) Salary Cap Years pursuant to Section 5(d)(i) above, then, subject to Section 5(d)(iii) below, the Offer Sheet may provide for Salary for the third Salary Cap Year of up to the maximum amount that the player would have been eligible to receive for the third Salary Cap Year absent the restriction in the first sentence of Section 5(d)(i) above and had the player’s Salary for the first two (2) Salary Cap Years been the maximum amount permitted under Article II, Section 7(a) and Article VII, Section 5(b)(1).”
>
> “A Team may sign a player to, or acquire by assignment, a Player Contract, not to exceed two (2) Seasons in length, that provides for a Salary for the first Season equal to the Minimum Player Salary applicable to that player (with no bonuses of any kind).”

**Readings for nba_L1_017 and nba_L2_012:** Team B may match the outstanding offer sheets for Player A using the Early Qualifying Veteran Free Agent Exception. Each player has two Years of Service with the stated prior Team. The $7,000,000 first-year salary in nba_L1_017 and the $10,000,000 first-year salary in nba_L2_012 are below 105% of the assumed $9,700,000 prior-year Average Player Salary ($10,185,000), and both offers cover at least two seasons. The later NTMLE signing in nba_L1_017 does not bar use of this separate prior-team exception to match. I retain the legal match readings because Section 6(b)(3)(ii) expressly authorizes them.

> “If an Early Qualifying Veteran Free Agent with two (2) Years of Service receives an Offer Sheet in accordance with the provisions of Article XI, Section 5(d), the player’s Prior Team may use the Early Qualifying Veteran Free Agent Exception to match the Offer Sheet.”

**Reading for nba_L0_051:** Team D’s $15,750,000 outgoing contract is assigned in the same simultaneous transaction in which Team D receives the signed-and-traded contract. I count that outgoing salary as removed before testing Team D’s Room for the incoming salary. Team D then has $41,338,000 of Room, enough for Player A’s $35,000,000 salary and the two minimum contracts; its resulting Team Salary is below the cap. The Room sentences do not state an explicit ordering for simultaneous assignments, so this remains a textual interpretation. I retain the post-assignment reading because the rule measures incoming “post-assignment Salaries,” the assigned contract is removed from the assignor’s Team Salary, and Section 8(e)(1)(vii) requires Room for the signed-and-traded salary at acquisition.

> “a Team with a Team Salary below the Salary Cap may acquire one (1) or more players by assignment whose post-assignment Salaries, in the aggregate, are no more than an amount equal to the Team’s room under the Salary Cap plus $250,000.”
>
> “the assignee Team shall, upon assignment, have included in its Team Salary the entire Salary for the then-current Salary Cap Year and for all future Salary Cap Years.”
>
> “the acquiring Team has Room for the player’s Salary plus any Unlikely Bonuses provided for in the first Season of the Contract.”

**Readings for nba_L1_005 and nba_L1_037 operation B:** In nba_L1_005, Player B’s $49,205,800 Free Agent Amount remains in Team A’s Team Salary because the operation does not say that Player B signed elsewhere or was renounced. Adding Player C’s $12,000,000 salary would exceed the First Apron, so the NTMLE is unavailable despite the amount being below its dollar limit. In nba_L1_037 operation B, Team B signs Player D, whose two-year 2022 contract ended after 2023-24. Team B’s post-trade salary is $147,790,000; adding $5,500,000 leaves it below the First Apron. Team B may use its unused NTMLE because the amount is below 9.12% of the cap and the three-year term is within the four-season maximum. Operation B names no transaction by Team A, so no separate Team A verdict is supported by its text. These readings follow the quoted hold, apron, and NTMLE rules.

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”
>
> “Player A was traded by Team A to Team B for Player B during 2023 Moratorium Period.”
>
> “A. Team A signs a 3-year contract with Player C providing annual salary $12,000,000 in the first Salary Cap Year (2024-2025) and 5% increase per year.”
>
> “B. Team signs or acquires a player using the Non-Taxpayer Mid-Level Salary Exception (as described in Section 6(e) below) | First Apron Level”
>
> “A Team may use the Non-Taxpayer Mid-Level Salary Exception to sign and/or acquire by assignment one (1) or more Player Contracts during each Salary Cap Year that, in the aggregate, provide for Salaries and Unlikely Bonuses (or in the case of assignment, post-assignment Salaries and Unlikely Bonuses) in the first Salary Cap Year totaling up to 9.12% of the Salary Cap for such Salary Cap Year; provided, however, that, prior to the first day of the 2024-25 Salary Cap Year, a Team shall not be permitted to use the Non-Taxpayer Mid-Level Salary Exception to acquire a Player Contract by assignment.”
>
> “The term of a Player Contract signed pursuant to the Non-Taxpayer Mid-Level Salary Exception may not exceed four (4) Seasons in length, and the remaining term of a Player Contract acquired by assignment pursuant to the Non-Taxpayer Mid-Level Salary Exception may not exceed four (4) Seasons in length.”
>
> “B. Team signs or acquires a player using the Non-Taxpayer Mid-Level Salary Exception (as described in Section 6(e) below) | First Apron Level”

**Readings for nba_L1_038 and nba_L1_082:** A player can be traded by assignment only while a Player Contract remains to be assigned. Player D’s two-year 2022 contract in nba_L1_038 and Players A and B’s three-year 2021 contracts in nba_L1_082 ended no later than the 2023-24 Salary Cap Year. The option terms in nba_L1_082 are included within the stated three-year terms; they do not add a fourth season. I retain the violations for attempting to trade those expired contracts.

> “For purposes of calculating Team Salary, with respect to any Player Contract that is assigned, the assignee Team shall, upon assignment, have included in its Team Salary the entire Salary for the then-current Salary Cap Year and for all future Salary Cap Years.”
>
> “the maximum Contract and Extension lengths described herein are inclusive of any Option Year contained in a Contract or Extension.”

**Reading for nba_L1_080 operation B:** The operation transfers Team A’s 2025 pick and Team C’s 2028 and 2029 picks. Team B is not a sender or recipient in operation B. The 2026 Team C pick held by Team B is a separate first-round selection and remains with Team B after its own 2026 pick is traded in operation C. Team C also holds Team D’s 2028 pick after operation B. I therefore do not find that operation B leaves Team B or Team C without picks in two consecutive future drafts. Operation D is illegal because Team B exchanges its 2029 first-round right for cash alone.

> “No Team may sell its rights to select a player in the first round of any NBA Draft for cash or its equivalent, or trade or exchange its right to select a player in the first round of any NBA Draft if the result of such trade or exchange may be to leave the Team without first-round picks in any two (2) consecutive future NBA Drafts.”

**Readings for nba_L1_001 and nba_L1_002:** The relevant operation has violations by more than one team. The Agreement and task instruction specify operation-letter priority but do not state a team tie-break. I return the first violating team mentioned in the operation text; this source-order tie-break does not depend on the team label itself.

> “If several violations exist, report the first violating operation in letter order (and its violating team).”

**Final residual review — nba_L1_005 operation A:** I retain the violation. Player B was traded to Team A in 2023 and his four-year 2020 contract then covered the 2023-24 season, so his Free Agent Amount belongs to Team A while unsigned. Adding that hold to Team A’s stated $148,000,000 yields $197,205,800 before the signing; the proposed $12,000,000 NTMLE signing would leave $209,205,800, above the First Apron. Team A cannot use the NTMLE for that transaction under the apron table. Player C’s prior team is Team C, so Team A cannot use its Veteran Free Agent Exception for him. The independent legal reading would require omitting Player B’s hold or disregarding the NTMLE apron row, neither of which the text supports.

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”
>
> “B. Team signs or acquires a player using the Non-Taxpayer Mid-Level Salary Exception (as described in Section 6(e) below) | First Apron Level”
>
> “A Team may not engage in a transaction set forth in the Transaction Restrictions Table if, immediately following such transaction, the Team’s Team Salary for such Salary Cap Year would exceed the ‘Applicable Apron Level’ that corresponds with such transaction in the table.”

**Final residual review — nba_L1_017 operation D:** I retain the legal match. Player A signed a two-season contract with Team B for 2022-23 and 2023-24, so he has two Years of Service and meets the stated Early Qualifying Veteran Free Agent definition. The $7,000,000 two-season offer sheet is within the Section 6(b)(3)(i) first-year ceiling and contract length. Section 6(b)(3)(ii) specifically permits Team B to use the Early Qualifying Veteran Free Agent Exception to match. Team B’s prior use of the NTMLE for a different player does not remove this separate matching authorization.

> “Notwithstanding anything to the contrary in Section 5(a)(2) above or this Section 6(b)(3), if an Early Qualifying Veteran Free Agent with two (2) Years of Service receives an Offer Sheet in accordance with the provisions of Article XI, Section 5(d), the player’s Prior Team may use the Early Qualifying Veteran Free Agent Exception to match the Offer Sheet.”
>
> “B. Team A provides Player A with an offer sheet - a 2-year contract providing salary $7,000,000 in the first Salary Cap Year (2024-2025), 5% increase per year for the first two Salary Cap Years.”
>
> “D. Team B matches the offer by team A.”

**Final residual review — nba_L1_037 operation B / Team A:** No Team A transaction or change in Team A’s salary or picks is stated in operation B; Team A therefore has no operation-specific verdict for that operation. Team B signs Player D, whose two-year 2022 contract with Team E covers 2022-23 and 2023-24 and has expired by the current cap year. Team B’s $5,500,000, three-year signing is within the NTMLE amount and term limits, and the post-sign Team Salary remains below the First Apron. I keep the signing legal. Operation A separately has an ownership violation because Player B’s active contract is with Team A, not Team B, despite having been drafted by Team B.

> “A Team may use the Non-Taxpayer Mid-Level Salary Exception to sign and/or acquire by assignment one (1) or more Player Contracts during each Salary Cap Year that, in the aggregate, provide for Salaries and Unlikely Bonuses (or in the case of assignment, post-assignment Salaries and Unlikely Bonuses) in the first Salary Cap Year totaling up to 9.12% of the Salary Cap for such Salary Cap Year; provided, however, that, prior to the first day of the 2024-25 Salary Cap Year, a Team shall not be permitted to use the Non-Taxpayer Mid-Level Salary Exception to acquire a Player Contract by assignment.”
>
> “The term of a Player Contract signed pursuant to the Non-Taxpayer Mid-Level Salary Exception may not exceed four (4) Seasons in length”
>
> “B. Team B signs a 3-year contract with Player D providing annual salary $5,500,000 in the first Salary Cap Year (2024-2025) and 5% increase per year.”

**Final residual review — nba_L1_080 operation B / Team B:** Operation B transfers Team A’s 2025 first-round pick and Team C’s 2028 and 2029 picks. Team B is not a sender or recipient, and its pick holdings do not change in that operation. The Stepien restriction applies to the Team trading or exchanging its first-round right; it does not supply a basis for a Team B verdict on this transaction. I keep Team B unchecked for operation B. The later operation D separately violates the express prohibition on exchanging a first-round pick for cash alone.

> “No Team may sell its rights to select a player in the first round of any NBA Draft for cash or its equivalent, or trade or exchange its right to select a player in the first round of any NBA Draft if the result of such trade or exchange may be to leave the Team without first-round picks in any two (2) consecutive future NBA Drafts.”
>
> “B. Team A trades its first-round draft pick in 2025 to Team C for its first-round draft picks in 2028 and 2029.”

**Final residual review — nba_L2_012 operation A:** I retain the legal reading. Team B’s unsigned Free Agent Amounts total $10,800,000, putting its Team Salary at $150,800,000 before the signing. The $5,000,000 contract replaces Player C’s $3,600,000 hold, leaving $152,200,000, below the First Apron. Team B can use the NTMLE: the rule allows it to sign “one (1) or more Player Contracts” up to the stated amount and term, without limiting that route to players who were not its own free agents. The Veteran Free Agent Exception’s lower ceiling governs a contract signed under that exception; it does not displace the separately authorized NTMLE route. The offer is below the NTMLE amount and its one-year term is within the four-season ceiling.

> “A Team may use the Non-Taxpayer Mid-Level Salary Exception to sign and/or acquire by assignment one (1) or more Player Contracts during each Salary Cap Year that, in the aggregate, provide for Salaries and Unlikely Bonuses (or in the case of assignment, post-assignment Salaries and Unlikely Bonuses) in the first Salary Cap Year totaling up to 9.12% of the Salary Cap for such Salary Cap Year; provided, however, that, prior to the first day of the 2024-25 Salary Cap Year, a Team shall not be permitted to use the Non-Taxpayer Mid-Level Salary Exception to acquire a Player Contract by assignment.”
>
> “The term of a Player Contract signed pursuant to the Non-Taxpayer Mid-Level Salary Exception may not exceed four (4) Seasons in length”
>
> “A. Team B signs a 1-year contract with Player C providing annual salary $5,000,000.”

> “A Non-Qualifying Veteran Free Agent will be included at one hundred twenty percent (120%) of his prior Salary.”

> “A Qualifying Veteran Free Agent, other than a Qualifying Veteran Free Agent described in Section 4(d)(1)(ii) below, will be included at one hundred fifty percent (150%) of his prior Salary if it was equal to or greater than the Estimated Average Player Salary for the prior Salary Cap Year, and one hundred ninety percent (190%) of his prior Salary if it was less than the Estimated Average Player Salary for the prior Salary Cap Year.”

> “A Qualifying Veteran Free Agent following the second Option Year of his Rookie Scale Contract will be included at two hundred fifty percent (250%) of the player’s prior Salary if it was equal to or greater than the Estimated Average Player Salary for the prior Salary Cap Year, and three hundred percent (300%) of his prior Salary if it was less than the Estimated Average Player Salary for the prior Salary Cap Year.”

## Contract terms and incomplete salary schedules

**Reading:** Stated annual salary amounts and explicit year-by-year amounts control cap checks. An independently stated total contract value is retained as a fact but is not used to replace annual amounts when the two disagree.

> “B. Team A provides an offer sheet for Player A providing annual salary $9,258,000 in the first Salary Cap Year (2024-2025) and $9,721,000 in the second Salary year, $10,279,000 in the third Salary year and $17,742,000 in the fourth Salary year, totally $40,000,000 for four years.”

**Reading:** The special restricted-free-agent third-year maximum form applies only when the offer sheet pays the maximum schedule permitted for the first two years under Section 5(d)(i). If those first two salaries are below that schedule, a third-year increase remains subject to the ordinary 5% rule.

> “If an Offer Sheet provides for the maximum allowable amount of Salary for the first two (2) Salary Cap Years pursuant to Section 5(d)(i) above, then, subject to Section 5(d)(iii) below, the Offer Sheet may provide for Salary for the third Salary Cap Year of up to the maximum amount that the player would have been eligible to receive for the third Salary Cap Year absent the restriction in the first sentence of Section 5(d)(i) above and had the player’s Salary for the first two (2) Salary Cap Years been the maximum amount permitted under Article II, Section 7(a) and Article VII, Section 5(b)(1).”

> “Notwithstanding any other provision of this Agreement, no such Offer Sheet may provide for Salary plus Unlikely Bonuses in the first Salary Cap Year totaling more than the amount of the Non-Taxpayer Mid-Level Salary Exception for such Salary Cap Year.”

> “For each Salary Cap Year covered by a Player Contract after the first Salary Cap Year, the player’s: (A) Salary, excluding Incentive Compensation, may increase or decrease in relation to the previous Salary Cap Year’s Salary, excluding Incentive Compensation, by no more than five percent (5%) of the Salary for the first Salary Cap Year covered by the Contract; and (B) Regular Salary may increase or decrease in relation to the previous Salary Cap Year’s Regular Salary by no more than five percent (5%) of the Regular Salary for the first Salary Cap Year covered by the Contract.”

**Reading:** If an operation omits contract duration, the checker leaves the duration unknown and skips tests that require a duration. It does not infer a one-year contract.

> “B. Team A provides an offer sheet for Player A providing annual salary $10,000,000 in the first Salary Cap Year (2024-2025) and 4% increase per year.”

**Reading:** The supplied rules state the Minimum Player Salary symbolically but do not include a numerical minimum-salary schedule. For arithmetic that cannot otherwise be completed, the implementation uses a $1,200,000 minimum proxy. Minimum salaries remain identified as symbolic in parser facts. This proxy can affect cap-room or trade-dollar checks near a threshold.

> “A Team may sign a player to, or acquire by assignment, a Player Contract, not to exceed two (2) Seasons in length, that provides for a Salary for the first Season equal to the Minimum Player Salary applicable to that player (with no bonuses of any kind).”

**Reading:** The rookie-scale extension percentage table is applied only to the categories listed in `rules.txt`. For All-NBA Third Team and Defensive Player of the Year cases, the text supplies the 25%-to-30% range but no negotiated percentage; the checker uses the maximum permitted 30% as the ceiling.

> “The player and Team may instead provide in the Extension that the player’s Salary (in the first Season of the extended term) will equal ‘[_____]% of the Salary Cap in effect during the first Season of the extended term.’ The percentage to be included where brackets are indicated in the foregoing language shall equal the percentage that is agreed upon by the Team and player, which shall in no event be less than twenty-five percent (25%) or greater than thirty percent (30%).”

## Missing dates, options, and eligibility facts

**Reading:** Dates not stated in an operation are not invented. The checker uses the current cap year for salary calculations and applies anniversary tests from the stated moratorium year when available. It cannot decide trade-deadline, 30-day, December 15, January 15, off-season-only, or notice-deadline rules without the relevant dates.

> “No player who signs a Standard NBA Contract as a Free Agent (or who signs a Standard NBA Contract while under a Two-Way Contract) may be traded before the later of (A) three (3) months following the date on which such Contract was signed or (B) the December 15 of the Salary Cap Year in which such Contract was signed;”

**Reading:** A stated option decision applies to the pending option year only. If the source names multiple option years but does not say what happened to each one, earlier options are treated as already exercised when a later option decision is stated. An option decision that names no contract option cannot alter contract length.

> “Player A just decided not to exercise the player option.”

**Reading:** A one-year Qualifying or Early Qualifying Veteran Free Agent contract requires the player’s consent to a trade unless the source says consent was given or waived. Silence is treated as no consent stated.

> “A player (other than a Two-Way Player) with a one-year Contract (excluding any Option Year) who would be a Qualifying Veteran Free Agent or an Early Qualifying Veteran Free Agent upon completing the playing services called for under his Contract cannot be traded without the player’s consent;”

**Reading:** Free-agent service class is derived from contract seasons covering each required prior season, plus stated trade history. A contract transferred by trade continues to cover those seasons for the new Prior Team; a team change without a permitted basis is not treated as a trade. Unstated contract seasons and trade history are not presumed.

> “Qualifying Veteran Free Agent” means a Veteran Free Agent who, prior to becoming a Veteran Free Agent, played under one (1) or more Player Contracts covering some or all of each of the three (3) preceding Seasons, and who either played exclusively with his Prior Team during such three (3) Seasons, or, if he played for more than one (1) Team during such period, changed Teams only (i) by means of trade, (ii) by means of assignment via the NBA’s waiver procedures during the first of the three (3) Seasons, or (iii) by signing with his Prior Team during the first of the three (3) Seasons.

> “Early Qualifying Veteran Free Agent” means a Veteran Free Agent who, prior to becoming a Veteran Free Agent, played under one (1) or more Player Contracts covering some or all of each of the two (2) preceding Seasons, and who either played exclusively with his Prior Team during such two (2) Seasons, or, if he played for more than one (1) Team during such period, changed Teams only (i) by means of trade, (ii) by means of assignment via the NBA’s waiver procedures, or (iii) by signing with his Prior Team during the first of the two (2) Seasons.”

**Reading for nba_L0_023, nba_L0_024, and nba_L0_025:** Player A’s four-year contract began in 2021, and the stated decline of its final player option leaves the first three seasons covering 2021-22 through 2023-24. The stated trade from Team B to Team A occurred during that span, so Team A is the Prior Team and Player A is a Qualifying Veteran Free Agent. The new 8% raises comply with the QFA-specific ceiling; the first-year salary is below the maximum. These signings do not violate the cited salary rules.

> “For each Salary Cap Year covered by a Player Contract after the first Salary Cap Year, the player’s: (A) Salary, excluding Incentive Compensation, may increase or decrease in relation to the previous Salary Cap Year’s Salary, excluding Incentive Compensation, by no more than eight percent (8%) of the Salary for the first Salary Cap Year covered by the Contract; and (B) Regular Salary may increase or decrease in relation to the previous Salary Cap Year’s Regular Salary by no more than eight percent (8%) of the Regular Salary for the first Salary Cap Year covered by the Contract.”

> “If the player is a Qualifying Veteran Free Agent, the new Player Contract may provide for Salary plus Unlikely Bonuses in the first Salary Cap Year totaling up to the maximum amount provided for in Article II, Section 7.”

**Reading:** If a recent draftee's first stated contract is with the drafting team and has no signing year, the draft year is used as the contract's start year for free-agent classification.

> “Player A signed a 2-year contract with Team B providing the minimum salary.”

**Reading:** Years of Service are approximated as the 2024-25 cap-year start year minus draft year, with no missed seasons. The problem gives draft year and age but no season-by-season service history.

> “Player A was the 44th second-round pick of Team B in 2022 NBA draft when he was 19 years old.”

**Reading:** A qualifying-offer operation establishes the offer and potential ROFR only when the named team is the prior team and a free-agent class can be derived. If the offer amount is not stated, the checker does not invent its salary or add a numeric qualifying-offer cap hold.

> “Team B provides a qualifying offer for Player A.”

## Transaction readings

**Reading:** A player signed and immediately traded in the same operation is checked as a sign-and-trade. The receiving team must have Room for the first-year signed-and-traded salary immediately before acquiring the contract, and its post-trade Team Salary must remain at or below the Salary Cap. Trade-matching and apron restrictions are checked separately. Room and Bird rights are considered when the signing team’s exception is not specified; Room MLE and Non-Taxpayer MLE are not treated as sign-and-trade exceptions.

> “a Veteran Free Agent and his Prior Team may enter into a Player Contract pursuant to an agreement between the Prior Team and another Team concerning the signing and subsequent trade of such Contract”

**Reading:** Trade cash before the `for` separator is paid by the trading team; cash after it is paid by the counterparty. Cash paid and received both count against the annual limit and are never netted.

> “the amounts paid or received by a Team in connection with one (1) or more trades occurring during a Salary Cap Year shall not be netted against each other”

**Reading:** A franchise owns its first-round picks by default for future years. Explicitly stated omissions and cross-team holdings replace that default; picks routed to a third team are checked as transfers to that destination.

> “Team A has all its first-round draft picks in the following 7 years.”

**Reading:** “Second Apron Team” status is approximated using post-operation Team Salary because the problem does not identify the date of the team’s final regular-season game or its full season salary projection.

> “Second Apron Team” means, for a Salary Cap Year, a Team that, as of the start of the Team’s last Regular Season game occurring within such Salary Cap Year, has an Team Salary for such Salary Cap Year that exceeds the Second Apron Level for such Salary Cap Year.

**Reading:** When multiple teams violate the same earliest operation, the checker returns the first violating team mentioned in that operation's text. The prompt fixes operation-letter order but does not specify a team tie-break; using source order preserves the same participant when team labels are swapped.

> “If several violations exist, report the first violating operation in letter order (and its violating team).”

**Reading for nba_L0_002:** Team A’s signing violates the Room limit after the Over-38 allocation. Player A’s 2020 four-year contract expired after 2023-24, so its salary is excluded from Team A’s stated starting Team Salary; Player A’s free-agent hold remains with prior Team B and does not reduce Team A’s Room. For the new four-year offer, the $40,250,000 fourth-year salary is attributed pro rata to years 1-3. That raises the first-year cap salary from $35,000,000 to $47,777,778, above Team A’s $40,588,000 Room. Its adjusted first-year amount is below the $49,205,800 maximum, so the Room violation is the reason operation A is illegal.

> “Except as provided in Sections 3(a)(2)(ii)-(iii) below, the aggregate Salaries in an Over 38 Contract for Salary Cap Years commencing with the fourth Salary Cap Year of such Over 38 Contract or the first Salary Cap Year that covers a Season that follows the player’s 38th birthday, whichever is later, shall be attributed to the prior Salary Cap Years pro rata on the basis of the Salaries for such prior Salary Cap Years.”

> “Subject to the other provisions of this Agreement, including, without limitation, Article II, Section 7, any Team with Room may enter into a Player Contract that calls for a Salary in the first Salary Cap Year covered by such Contract that would not exceed the Team’s then-current Room.”

**Over-38 age and allocation reading:** The situations give draft year and age at draft, but not full birth dates. I estimate the 38th-birthday year as draft year plus 38 minus age at draft. For the Over-38 test, the CBA treats seasons as beginning October 1, so the estimated birthday year identifies the first season start after the birthday. The rule applies to a contract of at least four seasons only if it includes a season starting after that estimated birthday year. For the default allocation, salaries in the later of year four or that first qualifying year are aggregated and allocated to the prior years in proportion to their stated salaries. The special five-year Qualifying Veteran Free Agent allocation and the age-35/36 exemption are implemented separately. The July 1 equal-share redistribution is not calculated because these questions ask about 2024-25 operations and provide no later contract-termination facts.

**Residual adjudication for nba_L0_040 through nba_L0_047:** The players whose facts say they were 19 at the 2008 draft are estimated to turn 38 in 2027. A new four-season contract beginning in 2024-25 covers a fourth Season beginning October 1, 2027, so the Over-38 rule applies. These are new contracts with teams other than the players’ Prior Teams, so neither the Prior-Team age-35/36 exemption nor the special five-year Qualifying Veteran Free Agent form applies. The year-four amount is attributed pro rata to years 1-3. The resulting first-year cap salaries exceed the receiving teams’ Room in each cited operation: $21,841,270 versus $20,588,000 in nba_L0_040 operation C; $23,206,349 versus $20,588,000 in nba_L0_041 operation B; $49,142,857 versus $40,588,000 in nba_L0_042 operation C and $39,588,000 in nba_L0_043 operation A; $23,206,349 versus $19,588,000 in nba_L0_044 operation A; $23,888,889 versus $20,588,000 in nba_L0_045 operation A and nba_L0_047 operation A; and $24,571,429 versus $20,588,000 in nba_L0_046 operation C. I retain these Room violations because Section 3(a)(2)(i) expressly attributes the later contract salaries to prior Salary Cap Years for cap calculations; treating the stated first-year salary as the sole Room charge would omit that attribution.

> “The following provisions shall apply to any Player Contract entered into, extended, or renegotiated that, beginning with the date such Contract, Extension, or Renegotiation is signed, covers four (4) or more Seasons, including one (1) or more Seasons commencing after such player will reach or has reached age thirty-eight (38) (an ‘Over 38 Contract’):”

> “Except as provided in Sections 3(a)(2)(ii)-(iii) below, the aggregate Salaries in an Over 38 Contract for Salary Cap Years commencing with the fourth Salary Cap Year of such Over 38 Contract or the first Salary Cap Year that covers a Season that follows the player’s 38th birthday, whichever is later, shall be attributed to the prior Salary Cap Years pro rata on the basis of the Salaries for such prior Salary Cap Years.”

> “For purposes of determining whether a Contract is an Over 38 Contract pursuant to this Section 3(a)(2) only, Seasons shall be deemed to commence on October 1 and conclude on the last day of the Salary Cap Year.”

> “For purposes of determining whether a Contract is an Over 38 Contract pursuant to this Section 3(a)(2) only, Seasons shall be deemed to commence on October 1 and conclude on the last day of the Salary Cap Year.”

> “If a Qualifying Veteran Free Agent who is age 35 or 36 enters into an Over 38 Contract with his Prior Team covering five (5) Seasons, the Salary in such Over 38 Contract for the fifth Salary Cap Year shall be attributed to the prior Salary Cap Years pro rata on the basis of the Salaries for such prior Salary Cap Years.”

> “there shall be no re-allocation of Salaries pursuant to this Section 3(a)(2) for any Contract between a Qualifying Veteran Free Agent and his Prior Team covering four (4) or fewer Seasons entered into by a player at age 35 or 36.”

**Reading for nba_L0_008 and nba_L0_010:** Team A’s $145,000,000 starting Team Salary includes a $49,205,800 Free Agent Amount for Player A, who finished the prior contract with Team A. This puts Team A above the Second Apron before operation A. Signing Player B for $10,000,000 cannot use the Non-Taxpayer MLE because that exception may not take Team Salary above the First Apron, and it cannot use the Taxpayer MLE because the resulting Team Salary would exceed the Second Apron. Player B’s prior contract was with Team B, so Team A has no stated Bird exception for him. Operation A therefore violates the cap rules. In nba_L0_010, operation C also attempts a second contract with Player A while operation B’s five-year contract is active; operation A remains first in letter order.

> “A Team’s Team Salary may not exceed the Salary Cap at any time unless the Team is using one of the Exceptions set forth in Section 6 below.”

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”

> “A Team may use the Non-Taxpayer Mid-Level Salary Exception to sign and/or acquire by assignment one (1) or more Player Contracts during each Salary Cap Year that, in the aggregate, provide for Salaries and Unlikely Bonuses (or in the case of assignment, post-assignment Salaries and Unlikely Bonuses) in the first Salary Cap Year totaling up to 9.12% of the Salary Cap for such Salary Cap Year; provided, however, that, prior to the first day of the 2024-25 Salary Cap Year, a Team shall not be permitted to use the Non-Taxpayer Mid-Level Salary Exception to acquire a Player Contract by assignment.”

> “A Team may use the Taxpayer Mid-Level Salary Exception to sign one (1) or more Player Contracts during each Salary Cap Year not to exceed two (2) Seasons in length, that, in the aggregate, provide for Salaries and Unlikely Bonuses in the first Salary Cap Year totaling up to the amounts set forth below, provided that the Team’s Team Salary immediately following the Team’s use of such Exception exceeds the First Apron Level:”

> “A Team may not engage in a transaction set forth in the Transaction Restrictions Table if, immediately following such transaction, the Team’s Team Salary for such Salary Cap Year would exceed the ‘Applicable Apron Level’ that corresponds with such transaction in the table.”

**Reading for nba_L0_005:** Team A must include Player A’s $34,500,000 Free Agent Amount while Player A remains an unsigned Qualifying Veteran Free Agent. That leaves $5,588,000 of Room against the $140,588,000 cap, so Team A cannot extend a $30,000,000 Offer Sheet for Player B. The minimum-salary exception does not authorize this offer because the stated salary is not the applicable Minimum Player Salary. The independent reading that omits Player A’s hold conflicts with Sections 4(a)(2)(i) and 4(d); the prompt excludes expiring contract salary, while Section 4(d) separately includes a Free Agent Amount.

> “With respect to each Veteran Free Agent who last played for a Team who is an Unrestricted Free Agent, the Free Agent Amount (as defined in Section 4(d) below) attributable to such Veteran Free Agent.”

> “A Team may sign a player to, or acquire by assignment, a Player Contract, not to exceed two (2) Seasons in length, that provides for a Salary for the first Season equal to the Minimum Player Salary applicable to that player (with no bonuses of any kind).”

> “In order to extend an Offer Sheet, the New Team must have Room for the player’s Player Contract at the time the Offer Sheet is signed and must continue to have such Room at all times while the Offer Sheet is outstanding.”

**Reading for nba_L0_012:** Team A’s unsigned Player A hold raises its Team Salary from $130,000,000 to $179,205,800, above the First Apron. The $7,200,000 signing for Player B exceeds the supplied 2024-25 Taxpayer MLE amount (the $5,000,000 2023-24 amount scaled by the current cap ratio), and it is not a minimum-salary contract or a contract with Team A’s own free agent. The signing therefore has no stated cap exception. I keep the violation reading because the exception and apron text bars the available MLE routes at those amounts and salary levels.

> “For each subsequent Salary Cap Year [the Taxpayer Mid-Level Salary Exception] is $5 million multiplied by a fraction, the numerator of which is the Salary Cap for that Salary Cap Year and the denominator of which is the Salary Cap for the 2023-24 Salary Cap Year.”

> “A Team may use the Taxpayer Mid-Level Salary Exception to sign one (1) or more Player Contracts during each Salary Cap Year not to exceed two (2) Seasons in length, that, in the aggregate, provide for Salaries and Unlikely Bonuses in the first Salary Cap Year totaling up to the amounts set forth below, provided that the Team’s Team Salary immediately following the Team’s use of such Exception exceeds the First Apron Level.”

**Reading for nba_L0_014 and nba_L0_015:** Team A’s listed salary plus the applicable Free Agent Amount for its own unsigned free agent is already above the Salary Cap. The new player came from a different Prior Team, so Team A has no Veteran Free Agent Exception for him. The proposed $36,000,000 signing in nba_L0_014 and $18,000,000 signing in nba_L0_015 each exceed the available Mid-Level exceptions; neither is a minimum-salary contract. I retain the violations because the text prohibits above-cap Team Salary unless an applicable exception authorizes the contract.

> “A Team’s Team Salary may not exceed the Salary Cap at any time unless the Team is using one of the Exceptions set forth in Section 6 below.”

**Reading for nba_L0_004:** Team A’s first-year offer-sheet salary of $11,000,000 is below the $12,821,626 first-year ceiling, so the offer does not provide the maximum allowable salary for the first two Salary Cap Years. Its $30,000,000 third-year salary therefore cannot use the special RFA third-year form and exceeds the ordinary annual-change limit. Operation B violates Article XI, Section 5(d).

**Reading for nba_L0_013, nba_L0_016, and nba_L0_018:** The unsigned-player Free Agent Amounts are part of each team’s Team Salary when determining whether it can use the under-cap trade route and which trade restrictions apply. In nba_L0_013, Team A’s $125,000,000 listed salary plus Player A’s $49,205,800 hold is above the cap; its $39,900,000 incoming salary exceeds the $33,000,000 salary of the one outgoing player, and the trade takes Team Salary above the First Apron, removing the $250,000 allowance. In nba_L0_016, Team A’s $120,000,000 salary plus Player A’s $24,570,000 hold also puts it above the cap, so it cannot use the room-under-cap route; the $34,800,000 incoming salary exceeds both the standard and expanded matching limits for the $16,800,000 outgoing contract. In nba_L0_018, Team A’s $7,200,000 hold causes the incoming $18,560,000 salary to take post-trade Team Salary above the First Apron; the expanded exception is then unavailable under the Transaction Restrictions Table, and aggregated standard matching is limited to the $13,650,000 outgoing salaries with no $250,000 allowance. I retain these violations because the text expressly counts Free Agent Amounts and makes the under-cap route conditional on Team Salary below the Salary Cap.

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”

> “a Team with a Team Salary below the Salary Cap may acquire one (1) or more players by assignment whose post-assignment Salaries, in the aggregate, are no more than an amount equal to the Team’s room under the Salary Cap plus $250,000.”

> “a Team may use the ‘Standard Traded Player Exception’ to replace one (1) Traded Player with one (1) or more Replacement Players whose Player Contracts are acquired simultaneously or non-simultaneously and whose post-assignment Salaries for the Salary Cap Year in which the Replacement Player(s) are acquired, in the aggregate, are no more than an amount equal to one hundred percent (100%) of the pre-trade Salary of the Traded Player, plus $250,000”

> “a Team may use the ‘Aggregated Standard Traded Player Exception’ to replace two (2) or more Traded Players with one (1) or more Replacement Players whose Player Contracts are acquired simultaneously and whose post-trade Salaries for the then-current Salary Cap Year, in the aggregate, are no more than an amount equal to one hundred percent (100%) of the aggregated pre-trade Salaries of the Traded Players, plus $250,000.”

> “if a Team’s post-assignment Team Salary would exceed the First Apron Level, then the $250,000 allowance referenced in each of Sections 6(j)(1)(i)-(v) above shall be reduced to $0.”

> “E. Team acquires a player using an Expanded Traded Player Exception (as described in Section 6(j)(1)(iv) below) | First Apron Level”

> “B. Team signs or acquires a player using the Non-Taxpayer Mid-Level Salary Exception (as described in Section 6(e) below) | First Apron Level”

> “K. Team signs a player using the Taxpayer Mid-Level Salary Exception (as described in Section 6(f) below) | Second Apron Level”

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”

**Revised reading for below-cap trade Room and sign-and-trade Room:** I measure the acquiring Team’s Room after accounting for the outgoing contracts transferred in the same simultaneous transaction and before adding the incoming contracts. The Agreement defines Room as the amount available for a new first-year Salary, and an assigned contract ceases to be part of the former Team’s Team Salary when assigned. In a simultaneous trade, that removal is part of the same transaction. Under Section 6(j)(1)(v), the acquired post-assignment Salaries are limited by the resulting Room plus $250,000, with that allowance reduced to zero if post-assignment Team Salary exceeds the First Apron. Section 6(j)(2) remains an alternate route for a below-cap Team to use the Expanded Traded Player Exception. Section 8(e)(1)(vii) likewise tests the acquiring Team’s Room for a signed-and-traded Salary after deducting the Team’s outgoing assigned Salaries; the separate post-trade cap check still tests net Team Salary. This interpretation follows these sentences:

> “a Team with a Team Salary below the Salary Cap may acquire one (1) or more players by assignment whose post-assignment Salaries, in the aggregate, are no more than an amount equal to the Team’s room under the Salary Cap plus $250,000.”
>
> “the assignee Team shall, upon assignment, have included in its Team Salary the entire Salary for the then-current Salary Cap Year and for all future Salary Cap Years.”
>
> “the acquiring Team has Room for the player’s Salary plus any Unlikely Bonuses provided for in the first Season of the Contract.”

For nba_L0_027, Team B’s $16,800,000 outgoing salary creates enough Room for its $27,000,000 incoming salary under Section 6(j)(1)(v), including the $250,000 allowance and subject to the apron rule. For nba_L0_032, Team B’s $31,000,000 outgoing salaries create Room for the $42,100,000 sign-and-traded Salary, and its net Team Salary remains below the cap. This supersedes the earlier reading in this document that excluded outgoing salaries from Room.

**Reading for nba_L1_005:** Operation A is illegal because Team A’s $49,205,800 Free Agent Amount for Player B remains in Team Salary while Team A signs Player C. The operation does not say that Player B signs elsewhere or is renounced, and signing Player C does not itself renounce Player B. Thus Team A’s salary for the proposed NTMLE signing is $209,205,800, above the First Apron. Operation B is allowed under the NTMLE: Team B’s resulting salary is below the First Apron, and the $12,000,000 first-year amount and three-year term fit the exception. I do not infer an unstated renunciation to make Operation A legal. This follows the exact Free Agent Amount and NTMLE restrictions:

> “until a Team’s Veteran Free Agent re-signs with his Team, signs with another NBA Team, or is renounced, he will be included in his Prior Team’s Team Salary at one of the following amounts (‘Free Agent Amounts’).”
>
> “A Team may use the Non-Taxpayer Mid-Level Salary Exception to sign and/or acquire by assignment one (1) or more Player Contracts during each Salary Cap Year that, in the aggregate, provide for Salaries and Unlikely Bonuses (or in the case of assignment, post-assignment Salaries and Unlikely Bonuses) in the first Salary Cap Year totaling up to 9.12% of the Salary Cap for such Salary Cap Year; provided, however, that, prior to the first day of the 2024-25 Salary Cap Year, a Team shall not be permitted to use the Non-Taxpayer Mid-Level Salary Exception to acquire a Player Contract by assignment.”
>
> “(A) A Team may not engage in a transaction set forth in the Transaction Restrictions Table if, immediately following such transaction, the Team’s Team Salary for such Salary Cap Year would exceed the “Applicable Apron Level” that corresponds with such transaction in the table; and”

**Reading for nba_L0_020:** Operation C violates the MLE aggregate limit. Team A uses $5,150,000 of the NTMLE in operation A on a two-year contract. After operation B replaces Player B’s $21,840,000 hold with a $24,000,000 contract, Team A is at $177,150,000. Operation C’s $4,800,000 contract takes Team Salary to $181,950,000, above the First Apron; without the earlier NTMLE signing, it would be $176,800,000. Section 6(f)(5) therefore deems the prior NTMLE amount to be Taxpayer MLE usage. The 2024-25 Taxpayer MLE limit is $5,168,676, so the combined $9,950,000 cannot be authorized under that exception. Team A has no other exception for Player C. Operation C is illegal.

> “In the event that, during a Salary Cap Year, a Team: (i) does not use the Non-Taxpayer Mid-Level Salary Exception to acquire any Player Contracts by assignment; (ii) uses the Non-Taxpayer Mid-Level Salary Exception in order to sign one (1) or more new Player Contracts during a Salary Cap Year, not to exceed two (2) Seasons in length that, in the aggregate, provide for Salaries and Unlikely Bonuses in the first Salary Cap Year of the Contract(s) totaling no more than the amounts set forth in Section 6(f)(1) above, and (iii) but for the Team’s use of the Non-Taxpayer Mid-Level Salary Exception as described in clause (ii) above, the Team otherwise would be permitted to engage in a transaction that causes the Team’s Team Salary to exceed the First Apron Level for such Salary Cap Year in accordance with the rules set forth in Section 2(e) above, then the Team shall be permitted to engage in such transaction, whereupon the Team will be deemed to have used the Taxpayer Mid-Level Salary Exception instead of the Non-Taxpayer Mid-Level Salary Exception for all purposes under this Article VII, and the Team’s ability to use the Non-Taxpayer Mid-Level Salary Exception during such Salary Cap Year shall thereupon be extinguished.”

> “A Team may use the Taxpayer Mid-Level Salary Exception to sign one (1) or more Player Contracts during each Salary Cap Year not to exceed two (2) Seasons in length, that, in the aggregate, provide for Salaries and Unlikely Bonuses in the first Salary Cap Year totaling up to the amounts set forth below, provided that the Team’s Team Salary immediately following the Team’s use of such Exception exceeds the First Apron Level.”

**Reading for nba_L0_038:** Team B may match Player A’s four-year, $11,000,000 offer sheet using the Non-Taxpayer MLE. Player A has two Years of Service, the first-year offer is below the current NTMLE limit of $12,821,626, and the contract term is within the NTMLE’s four-year limit. Section 6(e)(5) expressly allows the Prior Team to use the NTMLE to match an offer sheet for a player with one or two Years of Service. The 2024-25 salary after matching remains below the First Apron. Operation D is legal.

> “Notwithstanding anything to the contrary in Section 6(e)(3) above, if a Veteran Free Agent with one (1) or two (2) Years of Service receives an Offer Sheet in accordance with the provisions of Article XI, Section 5(d), the player’s Prior Team may use the Non-Taxpayer Mid-Level Salary Exception to match the Offer Sheet.”

**Reading for nba_L0_054:** The offer sheet is legal under the supplied terms. Its first two seasons use the maximum schedule allowed by Article XI, Section 5(d)(i): the $12,821,626 NTMLE amount in year one and a 5% increase in year two. The $25,000,000 third-year salary is below the maximum the player could receive for that season, and year four’s $1,000,000 increase is below 4.5% of the third-year salary ($1,125,000). For offer-sheet Room, the first-year charge is the four-year average ($19,321,083), which fits Team P’s $60,588,000 Room. The text allows salaries “up to” the third-year maximum; it does not require the offer to equal that maximum.

> “If an Offer Sheet provides for the maximum allowable amount of Salary for the first two (2) Salary Cap Years pursuant to Section 5(d)(i) above, then, subject to Section 5(d)(iii) below, the Offer Sheet may provide for Salary for the third Salary Cap Year of up to the maximum amount that the player would have been eligible to receive for the third Salary Cap Year absent the restriction in the first sentence of Section 5(d)(i) above and had the player’s Salary for the first two (2) Salary Cap Years been the maximum amount permitted under Article II, Section 7(a) and Article VII, Section 5(b)(1).”

> “If the Offer Sheet provides for Salary for the third Salary Cap Year in accordance with the foregoing sentence, then, subject to Section 5(d)(iii) below, (A) the player’s Salary for the fourth Salary Cap Year may increase or decrease in relation to the third Salary Cap Year’s Salary by no more than four and five tenths percent (4.5%) of the Salary for the third Salary Cap Year, (B) the Offer Sheet cannot contain bonuses of any kind, and (C) the Offer Sheet must provide for one hundred percent (100%) of the Base Compensation in each Season to be protected for lack of skill and injury or illness (with no individually-negotiated conditions or limitations on such protection).”

**Reading for nba_L0_073:** Operation B is illegal. The offer has the NTMLE amount in both of its first two years, but the maximum permitted second-year salary is 5% above the first-year salary under Article VII, Section 5(a)(1). Because year two is below that maximum, the special third-year form in Article XI, Section 5(d)(ii) is unavailable. The $30,000,000 third-year salary then exceeds the ordinary 5% annual-change limit. A flat second-year salary is allowed; it simply does not satisfy the special form’s “maximum allowable amount” condition.

> “Annual increases or decreases in Salary and Unlikely Bonuses shall be governed by Article VII, Section 5(a)(1).”

> “If an Offer Sheet provides for the maximum allowable amount of Salary for the first two (2) Salary Cap Years pursuant to Section 5(d)(i) above, then, subject to Section 5(d)(iii) below, the Offer Sheet may provide for Salary for the third Salary Cap Year of up to the maximum amount that the player would have been eligible to receive for the third Salary Cap Year absent the restriction in the first sentence of Section 5(d)(i) above and had the player’s Salary for the first two (2) Salary Cap Years been the maximum amount permitted under Article II, Section 7(a) and Article VII, Section 5(b)(1).”

**Reading for nba_L0_034, nba_L1_007, nba_L1_008, and nba_L1_009:** The first-round pick trade in the flagged operation leaves the named team without picks in two consecutive future drafts: 2027 and 2028 in nba_L0_034 and nba_L1_008, and 2029 and 2030 in nba_L1_007 and nba_L1_009. The bylaw bars a trade when its result may leave a team without first-round picks in any two consecutive future drafts. In these problems the earlier sign-and-trade already violates salary-matching or Room requirements, so the later pick violation is additional and does not change which operation is reported first.

> “No Team may sell its rights to select a player in the first round of any NBA Draft for cash or its equivalent, or trade or exchange its right to select a player in the first round of any NBA Draft if the result of such trade or exchange may be to leave the Team without first-round picks in any two (2) consecutive future NBA Drafts.”

**Reading for nba_L1_037:** In operation A, “Team A trades Player A and $5,000,000 to Team B for Player B and C” makes Team B the side offering Player B. The Player Situations say Player B signed a four-year contract with Team A in 2022, which remains active in 2024-25. I treat an assignment as a transfer by the team holding that Player Contract; Team B cannot assign Player B while the stated contract is with Team A. Operation A therefore violates the trade rules for Team B. This reading uses the operation’s “for” phrase to identify the counterparty’s consideration and the stated current contract holder to identify who can assign it.

> “For purposes of calculating Team Salary, with respect to any Player Contract that is assigned, the assignee Team shall, upon assignment, have included in its Team Salary the entire Salary for the then-current Salary Cap Year and for all future Salary Cap Years.”

> “Player B signed a 4-year contract with Team A (annual salary $7,000,000, 4% increase per year) during 2022 Moratorium Period.”

> “For purposes of calculating Team Salary, with respect to any Player Contract that is assigned, the assignee Team shall, upon assignment, have included in its Team Salary the entire Salary for the then-current Salary Cap Year and for all future Salary Cap Years.”

**Reading for nba_L1_055:** Team K’s operation B trade pays $3,600,000, and operation C pays another $4,150,000. Its total paid cash is $7,750,000, above the 2024-25 limit of 5.15% of the $140,588,000 cap ($7,240,282). Cash received in another trade is not netted against these payments. Operation C is illegal for Team K.

The same gross-cash reading makes operation C illegal for Team B in nba_L1_010: Team B pays $3,500,000 in operation A and another $4,000,000 in operation C, for $7,500,000 total.

> “A Team shall be permitted to pay or receive in connection with one (1) or more trades occurring during a Salary Cap Year, directly or indirectly, up to an aggregate amount equal to 5.15% of the Salary Cap for such Salary Cap Year in cash across all such trades”

> “the amounts paid or received by a Team in connection with one (1) or more trades occurring during a Salary Cap Year shall not be netted against each other”

**Reading for nba_L1_005:** Team A’s salary plus Player B’s stated free-agent hold is already above the Second Apron. Operation A signs Player C for $12,000,000 per year over three years. The Minimum Player Salary Exception cannot authorize this contract: the offered salary is not the applicable minimum and the term is longer than two seasons. Player C’s prior Team is Team C, so this is not a contract with Team A’s own free agent. The signing has no matching exception and violates the Salary Cap rule.

> “A Team’s Team Salary may not exceed the Salary Cap at any time unless the Team is using one of the Exceptions set forth in Section 6 below.”

> “A Team may sign a player to, or acquire by assignment, a Player Contract, not to exceed two (2) Seasons in length, that provides for a Salary for the first Season equal to the Minimum Player Salary applicable to that player (with no bonuses of any kind).”

**Reading for nba_L1_019:** Operation C is illegal for Team B. Player B’s prior contract paid $8,000,000; as a Non-Qualifying Veteran Free Agent, his prior-team first-year salary ceiling is the greater of 120% of that salary ($9,600,000), 120% of the applicable minimum, or the qualifying-offer amount. The proposed $10,000,000 first-year salary exceeds the supported ceiling. Section 8(e)(1) also requires the player to have finished the prior Season on the Prior Team’s roster. The only stated contract ended after 2022-23, so the text does not establish Team B roster status for 2023-24; the checker treats that sign-and-trade prerequisite as unsatisfied. The salary ceiling independently makes operation C illegal for Team B.

> “If the player is a Non-Qualifying Veteran Free Agent, then, subject to Article II, Section 7, the new Player Contract may provide in the first Salary Cap Year up to the greater of: (i) one hundred twenty percent (120%) of the Regular Salary for the final Salary Cap Year of the player’s prior Contract, plus one hundred twenty percent (120%) of any Likely Bonuses and Unlikely Bonuses, respectively, called for in the final Salary Cap Year covered by the player’s prior Contract; (ii) Salary plus Unlikely Bonuses totaling one hundred twenty percent (120%) of the then-current Minimum Annual Salary applicable to the player; or (iii) in the case of a Contract between a Team and its Restricted Free Agent, the Salary and Unlikely Bonuses required to be provided in a Qualifying Offer.”

> “Subject to the rules set forth in Section 2(e) above, a Veteran Free Agent and his Prior Team may enter into a Player Contract pursuant to an agreement between the Prior Team and another Team concerning the signing and subsequent trade of such Contract, but only if (i) the Veteran Free Agent finished the prior Season on his Prior Team’s roster, (ii) the Contract is for at least three (3) Seasons (excluding any Option Year) but no more than four (4) Seasons in length, (iii) the Contract is not signed pursuant to the Non-Taxpayer Mid-Level Salary Exception or the Mid-Level Salary Exception for Room Teams, (iv) the first Season of the Contract is fully protected for lack of skill, (v) the Contract is entered into prior to the first day of the Regular Season, (vi) with respect to any 5th Year Eligible Player (as defined in Article II, Section 7) who met one of the Higher Max Criteria (as defined in Article II, Section 7), the Contract may not provide the player with Salary (plus Unlikely Bonuses) in excess of twenty-five percent (25%) of the Salary Cap (as calculated pursuant to Article II, Section 7) in effect at the time the Contract is signed, and (vii) the acquiring Team has Room for the player’s Salary plus any Unlikely Bonuses provided for in the first Season of the Contract.”

**Reading for nba_L1_082:** Operation A cannot assign Players A or B under the stated contracts. Each three-year contract began in 2021 and expired after the 2023-24 Salary Cap Year; no active Player Contract remains in 2024-25 to transfer. Operation A therefore violates the trade rules for Team A. Operation B separately sends an active Player D contract to a Team already above the Salary Cap with no outgoing player salary; the stated $4,000,000 Traded Player Exception arose in 2022-23 and is outside the one-year use period.

> “a Team may use the ‘Standard Traded Player Exception’ to replace one (1) Traded Player with one (1) or more Replacement Players whose Player Contracts are acquired simultaneously or non-simultaneously and whose post-assignment Salaries for the Salary Cap Year in which the Replacement Player(s) are acquired, in the aggregate, are no more than an amount equal to one hundred percent (100%) of the pre-trade Salary of the Traded Player, plus $250,000, provided that any Player Contract acquired non-simultaneously pursuant to this Exception must be acquired within one (1) year following the date on which the Traded Player was traded.”

## Clauses without required facts

Some clauses cannot be decided from these problems because they omit the necessary facts: the exact Moratorium birthday adjustment and future July 1 Over-38 reallocations; bonuses, incentive compensation, deferred compensation, and guarantees; Two-Way status; minimum-salary schedules; exception acquisition histories and expiration dates; draft-pick penalties across multiple future seasons; contract consent waivers not stated in the situation; and the dates or notices needed for offer-sheet response, withdrawal, and post-extension trade restrictions. Those clauses are identified as `not_applicable` in `mapping.json` with the specific missing input. The current-year Over-38 allocation is evaluated using the age-at-draft interpretation above.

> “A Rookie Scale Extension entered into pursuant to this subsection may not include any Incentive Compensation.”

The supplied Section 7 text mentions renegotiations but does not include the substantive Section 7(c) rules; the checker parses renegotiations and applies the explicit rule that Section 8(e)(2) sign-and-trade amendments cannot be renegotiations. The excerpt provides no numerical minimum-salary schedule, and it does not provide every historical, compensation, or date fact needed to evaluate every clause for every operation. These missing facts are left explicit rather than supplied from outside the text.

## Sign-and-trade trade matching

**Reading:** For a qualifying or early qualifying free agent who signs with his prior Team and is immediately traded, first evaluate Section 6(j)(5) using the prior Team's Team Salary after replacing that player's free-agent hold with the new contract salary. If that post-signing salary is above the cap and the new first-year salary exceeds the amount permitted to a Non-Qualifying Veteran Free Agent under Section 6(b)(2), use the greater of the prior contract's final-year salary and half the new first-year salary as the signed-and-traded player's outgoing salary for trade-exception matching. The trade's final Team Salary still removes the assigned contract from the signing Team and includes it at actual salary on the receiving Team. Stated salaries are treated as having no unstated Unlikely Bonuses.

> “If (x) a Qualifying Veteran Free Agent or Early Qualifying Veteran Free Agent and his prior Team enter into a Player Contract, in accordance with Section 6(b)(1) or (3) above, in connection with an agreement to trade the Contract in accordance with Section 8(e) below, (y) the Team’s Team Salary immediately following such Contract signing is above the Salary Cap, and (z) the new Contract to be traded provides for Salary and Unlikely Bonuses for the first Season of such Contract in excess of the Salary and Unlikely Bonuses that could have been provided for by the Contract had the player been a Non-Qualifying Veteran Free Agent and the Contract had been signed pursuant to Section 6(b)(2) above, then for purposes of calculating the assignor Team’s Traded Player Exception, the player’s Salary shall be deemed equal to the greater of (i) the Salary for the last Season of his preceding Contract, or (ii) fifty percent (50%) of the Salary for the first Season of his new Contract.”

**Reading:** When the assignor uses a trade exception generated by a signed-and-traded contract to acquire another player, apply Transaction Restrictions Table row J's Second Apron ceiling in addition to the matching formula for the chosen standard, aggregated standard, or expanded route. For an expanded exception, row E's First Apron ceiling also applies; for an aggregated standard exception, row H's Second Apron ceiling applies. An under-cap room route remains available when its own room calculation permits the acquisition and does not use a trade exception in respect of the signed-and-traded contract.

> “J. Team acquires a player using a Traded Player Exception (as described in Section 6(j)(1)(i), (ii), (iii), or (iv) below), which Traded Player Exception is in respect of a Player Contract signed and traded pursuant to Section 8(e)(1) below | Second Apron Level”

**Reading for nba_L0_011:** Player A's qualifying status and $49,200,000 first-year salary trigger Section 6(j)(5): the prior salary and half the new salary are compared for Team A's outgoing matching salary. The receiving salary from Player B must fit the adjusted matching amount. Team A's post-trade salary also exceeds row J's Second Apron ceiling for a TPE in respect of Player A's sign-and-trade contract. Both checks follow the quoted clauses; the first violating team in the operation is Team A.

**Reading for nba_L0_030:** Team A's $35,000,000 sign-and-trade contract triggers Section 6(j)(5) based on its qualifying status and the prior Team Salary. Team A's post-trade salary after receiving Player B exceeds the Second Apron, so it cannot use the TPE generated in respect of the signed-and-traded contract for that acquisition.

**Revised reading for nba_L0_032:** Section 6(j)(5) reduces Player A's outgoing salary to $29,000,000. Team A's $31,000,000 incoming salary fits the Expanded TPE limit of $36,753,015 calculated from that adjusted amount, and its $173,000,000 post-trade Team Salary stays below row E's First Apron and row J's Second Apron. Player A's $42,100,000 first-year salary is also below the $42,176,400 maximum for a Qualifying Veteran Free Agent. Team B starts at $126,000,000 and has $14,588,000 of Room. Its outgoing $31,000,000 salary creates Room of $45,588,000 before the incoming contract is added; the $42,100,000 sign-and-traded Salary fits that Room. The Section 6(j)(1)(v) route also permits up to $45,838,000 including the $250,000 allowance, and the final $137,100,000 Team Salary remains below the cap. Operation A is legal for both teams.

> “In lieu of conducting a trade in accordance with Section 6(j)(1)(v) above, and notwithstanding Section 6(n) below and subject to Section 2(e) above and Section 6(j)(6) below, a Team with a Team Salary below the Salary Cap may conduct a trade in accordance with Sections 6(j)(1)(iii)-(iv) above.”

## Overlapping free-agent service definitions

**Reading:** The Qualifying Veteran Free Agent definition requires the three preceding Seasons, while the Early Qualifying Veteran Free Agent definition requires the two preceding Seasons. A player who meets the three-season test therefore also meets the two-season definition when its team-change conditions are satisfied. For Free Agent Amount and contract-limit calculations, use the qualifying status that requires more service (Qualifying before Early Qualifying); the Early Qualifying definition remains a satisfied underlying fact. This follows the separate Free Agent Amount rules for each named class and avoids reducing a qualifying player's applicable rights to the lesser two-season category.

> “A Qualifying Veteran Free Agent, other than a Qualifying Veteran Free Agent described in Section 4(d)(1)(ii) below, will be included at one hundred fifty percent (150%) of his prior Salary if it was equal to or greater than the Estimated Average Player Salary for the prior Salary Cap Year, and one hundred ninety percent (190%) of his prior Salary if it was less than the Estimated Average Player Salary for the prior Salary Cap Year.”

> “An Early Qualifying Veteran Free Agent will be included at one hundred thirty percent (130%) of his prior Salary;”
