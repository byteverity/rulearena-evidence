# Interpretations

This solver follows the literal fee tables and uses only facts present in each question. The rules do not define every input-to-table mapping, so the deterministic choices below make those gaps explicit.

## Ticket price, timing, and taxes

**Competing readings:** Add only the stated ticket price and published fees, or estimate taxes and fees based on ticketing date.

**Chosen:** Start with the listed ticket price and add listed bag charges. Do not estimate taxes. Use the supplied checked-bag fee tables as written; the questions do not give a ticket issue date.

**Text:** “All published bag fees apply at each check-in location and are base rates according to travel dates and destination; applicable taxes are not shown.” The checked-bag section says, “Bag fees have been updated effective for tickets issued on / after February 20, 2024.”

## Which listed items are the personal item, carry-on, or checked bags

**Competing readings:** Infer a role from the item's name (backpack versus luggage box), let the passenger choose any qualifying items, or assign roles by their order in the question.

**Chosen:** The item type is extracted but does not determine its role because the rules do not say that a backpack or luggage box is a personal item or carry-on. In question order, assign the first item within 18 × 14 × 8 inches to the personal-item allowance, then the first remaining item within 22 × 14 × 9 inches to the carry-on allowance. If no item fits the personal-item limit, assign the first qualifying carry-on item to the carry-on allowance. Treat all remaining items as checked bags, in their question order.

**Text:** “You're allowed 1 carry-on bag and 1 personal item in all cabins.” A personal item “must fit under the seat” and its “Dimensions should not exceed 18 x 14 x 8 inches.” A carry-on “must fit in in the overhead bin or under the seat,” and its total dimensions “cannot exceed 22 x 14 x 9 inches.” “If it doesn't fit, it will need to be checked.” The text does not name or prioritize the items in a question.

Dimensions are compared in the stated length × width × height order, without rotating them. The questions provide only numbers, so the solver cannot independently assess whether an item physically fits under a seat, in an overhead bin, or in an airport sizer. For checked size it follows the explicit instruction to add length, width, and height.

**Text:** “We calculate the size limits of your bag by adding the total outside dimensions of each bag, length + width + height.” Carry-on size is stated as “22 x 14 x 9 inches” and “must fit in the sizer at the airport,” but no alternative orientation rule is given.

Special carry-on exceptions and the soft-sided garment-bag limit are not applied: the problem item types are only backpacks and luggage boxes, and no item is identified as a diaper bag, breast pump, cooler, child seat, stroller, medical device, mobility device, or garment bag.

## Numbering checked bags

**Competing readings:** Number every listed item, number only checked items, or choose the order that minimizes fees for bags with different weights and sizes.

**Chosen:** Exclude the personal item and carry-on, then number the remaining checked items in their original question order. The text provides no rule for choosing a cheaper check-in order.

**Text:** The fee tables distinguish the “1st checked bag,” “2nd checked bag,” “Third Bag,” and “Fourth Bag +”; the allowance is one carry-on and one personal item. No sentence assigns a checked-bag number to a particular listed object.

## Matching routes to fee-table regions

**Competing readings:** Match only exact named countries/regions, use the origin or destination alone, or infer a region from both endpoints and any implied connection.

**Chosen:** Map each named city in the questions to its country or region, then match the pair of endpoints to a table row. Treat the trip as a direct one-way route from the stated origin to the stated destination; do not infer an unmentioned connection through Europe or elsewhere. Prefer a specific exception or named route row over a broad region row. For direction-specific Cuba rows, test the direction first. If no row describes the endpoint pair, the oracle's default fee is $0 because no fee is listed for that route.

**Text:** The tables specify routes with phrases such as “Within and between U.S., Puerto Rico and U.S. Virgin Islands,” “To or from Cuba,” “Between Haiti and [other regions],” “Between Panama and [other regions],” and “To or from India, China, Japan, South Korea, Hong Kong, Australia and New Zealand.” One first-bag row also says “connecting via Europe to another destination”; no question supplies connection information, so that case is inferred only when Europe is an endpoint.

When a pair could fit more than one checked-bag row, the implemented precedence is the row-specific route first (including Cuba, Haiti, Honduras, Panama, Guyana/Suriname, and named subregions), then the broader North America, Latin America, Europe/Israel/Qatar, or Asia-Pacific rows. For overweight fees, the direction-specific Cuba row takes precedence, then the explicit Australia/New Zealand or India/China/Japan/South Korea/Hong Kong “To or from” rows, then the Europe/Israel/Qatar row when its other endpoint is one of the regions named in that row, followed by North America and the Latin America fallback. For oversize tables, the row categories are applied by endpoints, with Europe/Israel/Qatar checked before Asia-Pacific, then Panama/South America, then Mexico/Caribbean/Central America/Guyana/Suriname, then U.S./Puerto Rico/U.S. Virgin Islands/Canada. These tables do not state a tie-break rule for trips whose endpoints fall in different broad categories.

**Text:** The fee tables list those route and region rows, but provide no general rule for resolving overlapping rows or for mixed-region trips that do not exactly match a row.

City-to-region membership is inferred from the city names given in the questions. For example, San Juan is treated as Puerto Rico; Port-au-Prince as Haiti; Panama City as Panama; Bogotá, Quito, and Lima as the Colombia/Ecuador/Peru grouping; Buenos Aires and Rio de Janeiro as other South America; Jerusalem as Israel; Doha as Qatar; and the listed European and Asia-Pacific cities as their named regions. This is ordinary geographic identification, not a separate mapping supplied in the rules.

## Dashes and absent fee rows

**Competing readings:** Read a dash in a fee cell as unavailable/not applicable, or as a zero-dollar fee.

**Chosen:** Encode each dash as $0. An absent route row also yields $0 via the oracle default. A dash or missing row displays no amount to charge; the text does not supply an alternate fee.

**Text:** The tables use “—” in some cabin cells and list no fee for endpoint pairs outside their rows. The general statement says published fees “are base rates according to travel dates and destination,” but it does not define the dash symbol or an unlisted route.

## Complimentary checked bags

**Competing readings:** Apply every status, credit-card, military, and airline-operation benefit automatically, or apply only benefits supported by the question's facts.

**Chosen:** Treat each question as the American Airlines itinerary governed by the supplied AA policy, including the general marketed-and-operated-AA condition. Apply complimentary benefits explicitly supported by cabin and route: Premium Economy and Business bags whose table fee is $0; the Main Plus second-bag allowance; confirmed Domestic First first/second bags; and the named-destination first-bag exception outside Basic Economy. Do not infer elite status, card membership, military status, or ticketing/check-in status. If a partner operated a codeshare, the text says free bags “may not apply,” but the questions give no operating-carrier detail. For the destination list, read “traveling to these destinations” as the stated destination of this one-way trip; read “Transatlantic” as a Europe-to-North-America endpoint pair.

**Text:** The general complimentary-bag rule applies on itineraries “marketed and operated by American Airlines.” Main Plus “includes 1 extra free checked bag in addition to the Main Cabin allowance (max of 2).” The destination benefit applies “when traveling to these destinations (excluding Basic Economy).” First and second bags are complimentary for “Confirmed Domestic First customers,” “Confirmed Business customers,” and “Confirmed Premium Economy customers.” Other complimentary benefits explicitly require AAdvantage/oneworld status, card membership, or military status; those facts are absent from the questions.

The destination exception is checked before the cabin's fee-table charge. Since the text says “to these destinations,” a listed place appearing only as the origin does not activate this exception. Other cabin-based free benefits use the table's zero fee or the stated cabin entitlement.

### Main Plus bag numbering and weight

**Competing readings:** Treat Main Plus as waiving the first checked-bag fee, waive the second checked-bag fee as its “extra” bag, or treat the extra free bag as eligible for the 70 lb complimentary allowance.

**Chosen:** Apply Main Plus to checked bag #2 only. Keep the first checked bag's Main Cabin table fee. Its extra free second bag has a 50 lb limit except on Australia/New Zealand routes; Main Plus is neither First nor Business, and the text grants a 70 lb complimentary allowance only to First/Business or to complimentary bags on Australia/New Zealand routes.

**Text:** The checked-bag tables put the footnote marker on the “Main Cabin^” column and state “Main Plus includes 1 extra free checked bag in addition to the Main Cabin allowance (max of 2).” The separate weight rule says “For First / Business, weight is 70 lbs / 32 kgs for complimentary bags and 50 lbs / 23 kgs for excess charged bags”; the Australia/New Zealand exception separately gives “70 lbs / 32kgs for complimentary bags and 50 lbs / 23 kgs for excess charged bags.” The general checked-bag limit is 50 lb. There is no sentence granting Main Plus a 70 lb limit.

For example, the domestic rows list a $40 Main Cabin first-bag fee and a $45 second-bag fee. The “extra” Main Plus bag is the second checked bag, so the first-bag fee remains $40 and checked bag #2's base fee is waived. The independent implementation disagreement on Main Plus cases was reviewed against these sentences; the solver retains this second-bag-free, 50 lb reading because waiving bag #1 or granting 70 lb would go beyond the text.

## Complimentary-bag weight allowance

**Competing readings:** Treat every $0 table cell or waived fee as a 70-pound complimentary allowance, or apply 70 pounds only where the weight rule explicitly grants it.

**Chosen:** Use 70 lb for complimentary First/Business bags, and for complimentary bags on flights to/from Australia or New Zealand. Use 50 lb for charged bags and for complimentary bags in other cabins/routes. A $0 base fee in a non-First/Business cabin does not by itself raise its weight allowance.

**Text:** “For First / Business, weight is 70 lbs / 32 kgs for complimentary bags and 50 lbs / 23 kgs for excess charged bags.” For Australia/New Zealand, the rule says “70 lbs / 32kgs for complimentary bags and 50 lbs / 23 kgs for excess charged bags.”

The weight bands are interpreted as open at the lower boundary and closed at the stated upper boundary: over 50 through 53 lb, over 53 through 70 lb, and over 70 through 100 lb. Values at or below the applicable allowance incur no overweight fee.

**Text:** The band headings say “Over 50 lbs … to 53 lbs,” “Over 53 lbs … to 70 lbs,” and “Over 70 lbs … to 100 lbs.”

## Overweight and oversize fees together

**Competing readings:** Add both overweight and oversize fees when a bag breaches both limits, or compare the two and charge only the higher surcharge.

**Chosen:** Evaluate both applicable oracle fees and charge their maximum, in addition to the checked-bag fee. Do not add the two surcharges.

**Text:** “More than one fee may apply per bag that exceeds standard dimensions for both weight and size. The higher fee between oversize and overweight applies, in addition to the checked bag fee.” The solver reads “more than one fee may apply” as permitting both fee categories to be considered, and the next sentence as selecting the higher one.

## Unlisted extreme measurements

**Competing readings:** Extrapolate beyond the largest displayed table band, or decline to invent a fee.

**Chosen:** Do not extrapolate. If a checked bag exceeds 100 lb, or its total dimensions exceed 115 inches, report a per-problem error with a null answer because the rules give no fee or acceptance rule beyond those limits. The supplied problem set contains no such cases.

**Text:** The largest overweight band ends at “100 lbs / 45 kgs,” and the largest oversize band ends at “115 in / 292 cm.” No row specifies a fee or disposition above those values, except that some routes explicitly say “Not accepted” for the 70-to-100-lb band.

## Per-passenger, per-way scope and other fees

**Competing readings:** Multiply bag fees for round-trip travel or add ancillary charges not mentioned in the question.

**Chosen:** Add one passenger's fees for the one-way itinerary posed in each question. Do not add taxes or unlisted services. The question gives one passenger, one route, one ticket price, and no purchase of upgrades or other chargeable services.

**Text:** “All bag fees are non-refundable and apply per person, each way, even if you buy or get an upgrade that includes free checked bags.” The question asks about one passenger “flying from [origin] to [destination]” and gives a single ticket price. Applicable taxes “are not shown.”
