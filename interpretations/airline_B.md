# Interpretations

The rules leave several calculation choices open. This solver uses the readings below. The quotes are exact rule text from `rules.txt`; the quoted table labels are used as written.

## Item roles: personal item, carry-on, or checked bag

**Competing readings:** A listed backpack could be a personal item, a carry-on, or a checked bag. The question does not label any item with an airport handling role. One could also treat all listed items as checked bags because the traveler is asked to account for every item.

**Chosen reading:** In list order, assign at most one backpack that meets the personal-item dimensions to the personal-item slot, then at most one remaining backpack that meets carry-on dimensions to the carry-on slot. Compare dimensions in the listed length, width, height order. Other items count as checked bags. In these problems the first backpack is the only item that fits a free hand-baggage slot; it fits the carry-on limit in every question and fits the personal-item limit in some. The solver does not infer that a luggage box is a personal item or carry-on merely because its dimensions might fit.

**Supporting text:** “You're allowed 1 carry-on bag and 1 personal item in all cabins.” “Your personal item like a purse or small handbag must fit under the seat in front of you. Dimensions should not exceed 18 x 14 x 8 inches (45 x 35 x 20 cm).” “You can bring only one carry-on item along with your personal item. Your carry-on must fit in in the overhead bin or under the seat in front of you. If it doesn't fit, it will need to be checked.” “The total size of your carry-on, including the handles and wheels, cannot exceed 22 x 14 x 9 inches (56 x 36 x 23 cm) and must fit in the sizer at the airport.”

The text does not say how to handle rotation, so the given dimension order is compared directly to the printed limits. Checked-bag dimensions are handled separately by adding the three outside dimensions, as directed below.

The rule also says a carry-on “must fit in the sizer at the airport,” but the questions only state outside dimensions and do not give a sizer measurement. The solver treats an item within the printed carry-on dimensions as fitting the sizer. It treats any item outside those dimensions as checked, consistent with “If it doesn't fit, it will need to be checked.”

## Which checked bag is first, second, third, and fourth+

**Competing readings:** Checked bags could be numbered in the order listed, by size, by weight, or by a traveler-selected loading order. The rules do not specify a sorting method.

**Chosen reading:** After removing the eligible personal item and carry-on, number the remaining items as checked bags in the order they appeared in the question. The first one uses the first-bag table, the second uses the second-bag table, and so on; every ordinal from four onward uses Fourth Bag +.

**Supporting text:** The rule tables are titled “First Bag,” “Second Bag,” “Third Bag,” and “Fourth Bag +.” The questions list each item with an ordinal and ask to compute the total “(don't omit any bag).” No rule says to reorder the list.

## Matching an origin and destination to a region row

**Competing readings:** Region rows overlap, use asymmetric wording (“to” versus “from”), or group several countries together. Some rows describe a particular named country while other rows describe larger regions. The rules do not define a separate route-classification algorithm.

**Chosen reading:** Map each named city to its country or listed geographic region, then choose the most specific row whose stated route includes both endpoints. Use direction when a row distinguishes travel “to” and “from” Cuba. Apply country-specific rows such as Cuba, Haiti, Panama, Colombia, Ecuador, Peru, Israel, or Qatar before broader regional rows. Use an Asia/Oceania row when an endpoint belongs to its named country group; use the Europe/Israel/Qatar row when that row's stated other endpoint group matches. The first-bag and second-bag tables retain their different region groupings rather than sharing a generalized lookup.

**Supporting text:** The first-bag rows distinguish, for example, “From U.S., Puerto Rico, U.S. Virgin Islands, Canada, Mexico and the Caribbean (excluding Haiti) to Cuba” from “From Cuba to U.S., Puerto Rico, U.S. Virgin Islands, Canada, Mexico and the Caribbean (including Haiti).” Other rows separately name “To or from Haiti,” “Between Panama, Colombia, Ecuador, Peru and U.S.,” and “To or from India, China, Japan, South Korea, Hong Kong, Australia and New Zealand.” The second-bag table likewise separates “From all regions to Cuba” from “From Cuba to all regions.”

For a row mentioning multiple possible region groups, if the stated route matches more than one group, the more specific named-country or named-destination row takes precedence. The question gives endpoint cities but no connection details, so “connecting via Europe” is used only when Europe is an endpoint; no unstated connection is inferred.

For rows phrased “between [group A] and [group B],” I require one endpoint from each listed group. A route with both endpoints in a group is not enough unless the row separately names that pairing. Thus the third-bag and overweight rows that add “or between the Caribbean and Central America” cover that extra pairing, but do not imply a fee for every route within Latin America. Rows phrased “to or from” a named country group apply when either endpoint is in that group. I check the Cuba rows before broader regional rows, and only use the Haiti or Guyana/Suriname second-bag row when the other endpoint is among that row's named groups.

**Supporting text:** The Third Bag row says “Between Mexico, Caribbean, Central America, South America and U.S., Puerto Rico, U.S. Virgin Islands, Canada; or Between the Caribbean and Central America.” The over-53-to-70-pound row has the same group structure, while the over-70-to-100-pound row says “Between Mexico, Caribbean, Central America, South America and U.S., Puerto Rico, U.S. Virgin Islands, Canada; or between the Caribbean and Central America.” The second-bag table says “From all regions to Cuba” and “From Cuba to all regions,” then separately limits the Haiti and Guyana/Suriname routes to named endpoint groups.

## Dash cells

**Competing readings:** An em dash in the Premium Economy column could mean no charge, not applicable, or unavailable service. The source distinguishes it from an explicit `$0` but supplies no legend.

**Chosen reading:** Preserve the dash as `not_applicable` in the oracle. For the requested cost total, treat that cell as no separately stated fee ($0) rather than inventing an amount or failing to produce a total.

**Supporting text:** The First Bag table uses both “—” and explicit “$0” cells in different columns. The Second Bag table does the same. No legend defines the em dash.

## Main Plus and other complimentary checked bags

**Competing readings:** The rules do not give Main Plus its own numeric column. “One extra free checked bag in addition to the Main Cabin allowance” could waive the first-bag fee when the Main Cabin rate is positive, or could preserve the Main Cabin first-bag charge and make the second checked bag free. The “max of 2” parenthetical could also be read as changing the numbering of later bags.

**Chosen reading:** Use Main Cabin rates for Main Plus, preserve the first checked bag's Main Cabin rate, and waive the second checked bag's base fee once. “Extra” and “in addition to” place the free bag after the ordinary first checked bag. “Max of 2” limits the combined Main Cabin allowance and Main Plus extra to the first two checked bags; it does not change bag ordinals or remove later bag fees.

**Supporting text:** The footnote under both the First Bag and Second Bag tables says “Main Plus includes 1 extra free checked bag in addition to the Main Cabin allowance (max of 2).” The word “extra” supports retaining the ordinary first-bag rate and applying the benefit to checked bag 2. The tables label the Main Cabin cells with a footnote marker but provide no separate Main Plus fee values.

For the other named cabin classes, the first/second-bag oracle cells are used directly. Their `$0` values implement the stated complimentary first/second checked bags for confirmed Premium Economy, Business, and First customers where those cells are zero. No status, card, military, or operating-carrier facts are supplied, so those conditional benefits are not independently assumed.

## Destination-based complimentary first bag

**Competing readings:** The list of destinations granting a complimentary first bag could be an explanation of the table's zero cells, or an additional exception that overrides a nonzero table cell. The text does not explain how the paragraph and table interact.

**Chosen reading:** Treat the paragraph as a waiver of the first checked-bag base fee for non-Basic Economy passengers traveling to a listed destination. Apply it even if the matched First Bag table cell is nonzero. A city endpoint listed as a destination is used as the destination fact; transatlantic travel is recognized when Europe and an Americas endpoint are paired. The benefit does not waive overweight or oversize charges.

**Supporting text:** “1st checked bag is complimentary for:” followed by the card/status list, “or when traveling to these destinations (excluding Basic Economy):” followed by the country list including El Salvador, Panama, and the transatlantic category. The paragraph describes a complimentary bag, while the tables describe published bag fees.

## Weight limits and overweight bands

**Competing readings:** First/Business and Australia/New Zealand routes have a 70-pound allowance for complimentary bags but 50 pounds for excess charged bags. The text does not define how to determine whether each individual bag is complimentary when a fare or destination benefit applies.

**Chosen reading:** A checked bag whose base checked-bag fee is zero, including a Main Plus or destination waiver, is treated as complimentary for this weight-limit rule. First and Business complimentary bags have a 70-pound limit; their excess charged bags use 50 pounds. On a route to/from Australia or New Zealand, any complimentary bag has a 70-pound limit and any excess charged bag uses 50 pounds. Other bags use 50 pounds. Once a bag exceeds the applicable limit, select the matching published overweight band using the bag's full weight.

**Supporting text:** “For all regions, except to / from Australia or New Zealand, your checked bag allowance is:” “Weight: 50 lbs / 23 kgs” and “For First / Business, weight is 70 lbs / 32 kgs for complimentary bags and 50 lbs / 23 kgs for excess charged bags.” The Australia/New Zealand section says “Weight: 70 lbs / 32kgs for complimentary bags and 50 lbs / 23 kgs for excess charged bags.”

“Over 50 lbs ... to 53 lbs,” “Over 53 lbs ... to 70 lbs,” and “Over 70 lbs ... to 100 lbs” are interpreted as strict lower bounds and inclusive upper bounds. A bag at exactly 50 pounds incurs no overweight fee; one at exactly 53, 70, or 100 pounds uses the band ending at that limit. The questions state weights in pounds, so those values are used without converting to kilograms.

## Oversize limits and combined excess fees

**Competing readings:** The table lists ranges through 115 inches, but does not describe bags above 115 inches. The sentence about “more than one fee” could be read to charge both an overweight and oversize surcharge, while the next sentence specifies a comparison. A route such as Qatar–Japan matches two oversize region labels; the text does not say whether to use its origin's row, destination's row, both, or the first listed row.

**Chosen reading:** Sum each checked bag's three outside dimensions. Do not charge an oversize fee at or below 62 inches; for greater sizes use the band above 62 through 65, or above 65 through 115. If a route matches multiple oversize region labels, use the first matching row in the published table order (for example, a Qatar–Japan route matches “Europe, Israel, Qatar” before “China, Japan, South Korea, Hong Kong, India, Australia, and New Zealand”). If a bag is both overweight and oversize, charge the larger of the two excess fees once, in addition to its checked-bag fee. If an item exceeds a listed acceptance limit or lies outside every published band, return a null answer with an error because the text gives no computable total.

**Supporting text:** “We calculate the size limits of your bag by adding the total outside dimensions of each bag, length + width + height.” The oversize headings are “Over 62 in / 158 cm – 65 in / 165 cm” and “Over 65 in / 165 cm – 115 in / 292 cm.” The oversize table lists “Europe, Israel, Qatar” before “China, Japan, South Korea, Hong Kong, India, Australia, and New Zealand”; it gives no priority rule for routes matching both labels. For combined excess, the text says “More than one fee may apply per bag that exceeds standard dimensions for both weight and size. The higher fee between oversize and overweight applies, in addition to the checked bag fee.” The 70-to-100-pound table explicitly says “Not accepted” for some region groups.

## Fee date, taxes, and trip direction

**Competing readings:** The rate paragraph has an effective ticket-issue date, says applicable taxes are not shown, and applies fees each way. The questions do not state a ticket-issue date, taxes, or a return leg.

**Chosen reading:** Apply the published rates in `rules.txt` as the only available schedule, do not estimate tax, and apply bag fees once for the stated origin-to-destination direction. Add the ticket price to all bag fees for the one passenger.

**Supporting text:** “All published bag fees apply at each check-in location and are base rates according to travel dates and destination; applicable taxes are not shown.” “Bag fees have been updated effective for tickets issued on / after February 20, 2024.” “All bag fees are non-refundable and apply per person, each way.”

## Bags marked “Not accepted”

**Competing readings:** A bag that the table says is “Not accepted” has no fee amount; the text does not prescribe a substitute itinerary or a way to price a changed bag.

**Chosen reading:** Do not invent a fee or silently treat the item as free. Emit `answer: null` and an error identifying the unaccepted bag. The CLI still emits a valid JSON record and continues to later questions in `--all` mode.

**Supporting text:** The 70-to-100-pound overweight table explicitly marks several region rows “Not accepted.”
