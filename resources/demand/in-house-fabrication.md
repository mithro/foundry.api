# In-house fabrication (`IHF`)

**What this file covers.** Commercial companies that built, bought or ran their own silicon or MEMS
fabrication capability instead of buying wafers from a merchant foundry — and, where it exists, what
that capability cost. It starts from one company the repository owner asked about by name,
`science.xyz`, and works outwards to comparable cases.

**Why it is evidence.** A company that spends its own money on a fab has, by revealed preference,
been told "no" by the merchant foundry market — or has been quoted a price, a minimum volume or a
lead time it could not live with. That is the cleanest available measurement of demand the existing
industry refuses to serve, which is [H5](../hypotheses.md#h5-there-is-a-long-tail-of-demand-for-chips).
It cuts the other way too: the price of building the capability is the price of *not* being served,
and if that price is low, the "unserved" demand may simply be demand that can serve itself. Where
one of these companies then opens its line to outside customers, it becomes a live experiment in
exactly the business foundry.api proposes, and its prices and its stated reasons are direct evidence
on [H6](../hypotheses.md#h6-small-customers-can-each-be-profitable).

**ID prefix:** `IHF`. Numbering runs `IHF-1` upwards and does not collide with `DEM` or `SMB`.

Everything here was gathered read-only, HTTP GET only, between 2026-09-18 and 2026-09-19. No form
was submitted, no account created, no person contacted by any channel. Sources that could not be
reached are listed in [§ Blocked sources](#blocked-sources) rather than dropped.

---

## 1. Identification: what `science.xyz` is

**Resolved.** `science.xyz` is the website of **Science Corporation**, a US neural-engineering and
medical-device company founded in 2021 by **Max Hodak**, a co-founder and former president of
Neuralink. The working hypothesis given to this research — that the name refers to Max Hodak's
neural-implant company, and that it matters here because it runs its own microfabrication — is
**confirmed, and it is stronger than the hypothesis assumed.** Science does not merely run an
in-house MEMS line for itself. It bought an existing commercial MEMS foundry, kept that foundry's
outside customers, and **sells MEMS fabrication to third parties under the name Science Foundry,
including scheduled multi-project wafer runs at a published starting price.**

### The legal entity

| Field | Value | Source |
|---|---|---|
| Registrant name on file with the SEC | **Science Corp** | EDGAR submissions API, CIK `0001873836` |
| Name used publicly and in `schema.org` metadata on the site | **Science Corporation** | `https://science.xyz/` page source |
| CIK | 0001873836 | EDGAR |
| Jurisdiction of incorporation | **Delaware** | Form D, CIK 0001873836 |
| Year of incorporation | **2021** | Form D (both the 2021 and the 2026 filings state "2021") |
| Business address, 2021 filing | 1010 Atlantic Ave., Alameda, CA 94501 | Form D 0001873836-21-000002 |
| Business address, current | **300 Wind River Way, Alameda, CA 94501** | EDGAR submissions API; Form D 0001873836-26-000001 |
| Other sites | Research Triangle Park / Durham, North Carolina, USA; Paris, France | `schema.org` `Organization` block on `https://science.xyz/` |
| Industry group as self-declared on Form D | "Other Technology" | Form D |

**The name discrepancy is real and is not resolved by any source found:** the SEC registrant is
"Science Corp", the website and its structured metadata say "Science Corporation", and the MEMS
business is operated under two further names — **Science Foundry** (the customer-facing brand) and
**Science Wafer Services** (described by the company as the unit's official name). All four refer to
the same company. Nothing found establishes whether "Science Wafer Services" is a separate legal
entity or an internal division; the announcement calls it "a fairly independent unit, officially
known as Science Wafer Services", which is not the same as saying it is separately incorporated.

### Residual ambiguity, stated plainly

- **"Science" is a badly overloaded company name.** There is at least one well-known and entirely
  unrelated US company called *Science Inc.* (a Santa Monica start-up studio, `science-inc.com`,
  sponsor of the "Science Strategic Acquisition Corp." SPACs that appear in EDGAR), and EDGAR also
  carries *Science Applications International Corp*, *Science 37 Holdings* and *Cambridge Science
  Corp*. None of these is `science.xyz`. The `.xyz` domain and the Alameda address are what
  disambiguate.
- **The owner's brief gave no context beyond the bare domain.** The identification above rests on the
  domain resolving to Science Corporation's own site and that site describing the MEMS foundry
  business. If the owner meant some other "science.xyz", nothing found suggests what it would be: the
  domain has a single, current, unambiguous owner.
- **What "science.xyz" does *not* appear to be:** it is not a foundry-industry body, not an open
  silicon programme, and not a shuttle broker. Its relevance here is entirely through Science
  Foundry.

### Why it bears on this project, in one paragraph

Science Corporation is a commercial company that concluded it could not get the fabrication it needed
from anybody else, bought a fab, and then turned that fab into a merchant service aimed explicitly at
small, early-stage, low-volume customers — the exact segment foundry.api is built around. It states
the reason in its own words (IHF-1, IHF-5), it discloses what the fab cost to buy (IHF-3) and what it
is spending to expand it (IHF-2), and it publishes a starting price for a multi-project wafer run
(IHF-4). That combination — motive, capex and price, all from primary sources — is rare in this
directory.

---

