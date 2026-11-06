# Functional Code Scheme Record (W77)

The dated record of the W77 functional code scheme and every ruling that changed it, kept so that any delivered code set can be read against the convention in force on its issue date. Read this before coding anything for W77, before auditing a naming document (`csl-technical-docs` 4.9), and before answering "which structure are we on". Update it the day a ruling is made; a verbal ruling is entered as verbal with the written-confirmation request date and stays verbal until the confirmation exists (csl-operating-rules Section 8). Status as of 09/30/26. The method for applying the scheme is `csl-asset-data-cmms` 3.4; the validation rules are in `upload-sheet-qa.md`.

---

## 1. Published scheme

| Item | Value |
|---|---|
| Scheme | Functional code scheme V1.0, six levels: `Enterprise_Site_Bldg_System_Equipment_Device` |
| Reference document | Functional Code Structure v1.1 (the version cited in the 08/24/26 format rulings) |
| Prefix at W77 | `ASML_WLT_077_` (enterprise ASML, site WLT, building 077) |
| Separator | Underscore between every segment |
| Loop association | A column on the record, not a code segment or a parent prefix |
| Owner of the scheme | Client data owner for Planon data structure and imports (T. Dube per the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project)); GFC direction also reaches CSL through that channel per the stakeholder register |

## 2. Rulings ledger (chronological)

| Date | Ruling | Stated by (role) | Written / verbal | Document or record | What it changed | Files built to it |
|---|---|---|---|---|---|---|
| 08/24/26 | Scope narrowed to mechanical/HVAC plus loops; electrical in-house by the client; roof PML already in Planon | Client side (program lead directs the Planon realignment) | Per the 08/24/26 record | Planon weekly record of that date | Which families CSL codes | Everything from mechanical R4 onward |
| 08/24/26 | Prefix `ASML_WLT_077_` with underscores; no building letter | Client data owner side (data structure and imports; GFC direction also via the CRE contact named in the stakeholder register) | Written (references Functional Code Structure v1.1) | Functional Code Structure v1.1; 08/24/26 record | Replaced earlier prefix forms | MEP list R3; mechanical R4 → v_5; New Asset Forms 08/27/26 |
| 08/24/26 | Code resets at the unit: `ASML_WLT_077_AHU22N` | Same | Written | Same | Unit is the reset point; no system token in the unit code | Same |
| 08/24/26 | Children as `<unit>_PUM01`, `<unit>_sensor01` | Same | Written | Same | Child form fixed; pump token left open (see Section 4) | Same |
| 08/24/26 | Loop association carried as a column, not a code segment or parent prefix | Same | Written | Same | Removed loop tokens from codes | Same |
| 08/24/26 | Legacy numeric grouping codes dropped | Same | Written | Same | Legacy CHAMPS grouping numbers not carried | Same |
| 08/24/26 | Spaces required on every record for work-order routing | Same | Written | Same | Space became a required field in validation | Same |
| 08/24/26 | Six levels | Same | Written | Same | Depth as published | MEP list R3 (six-level codes) |
| 08/26/26 (v_3 sequence; confirm from the v_3 R2 Control sheet) | Fan-family child tokens EXF (exhaust) / RDF (redundant) / SEF (smoke exhaust) | Recorded with the v_3 R2 fan recodes | As recorded on the v_3 R2 Control sheet | Mechanical v_3 R2 | Fan recodes | v_3 R2 onward |
| 09/10/26 | Structure extended past six levels | Client data owner side | Per the 09/10/26 record; no versioned spec | Record of 09/10/26 | Depth no longer six | None issued to it; Loops PML 09/23/26 carries depth OPEN |
| 09/22/26 | Eight levels | Client data owner side | Verbal; written confirmation requested 09/22/26 | Call record | Depth stated, not specified | None |
| 09/29/26 | "Up to seven" levels | Client data owner side | Stated 09/29/26; no versioned spec | Record of 09/29/26 | Depth stated, not specified | None |
| 09/29/26 | Import root cause: unaltered CHAMPS templates required ("any change and they will not upload"); six templates exist (Process / Multi-Asset / Standard Asset, each IMP and Update); CSL held one | Attribute to the speaker named in the 09/29/26 record | Stated | Record of 09/29/26 | Template discipline (`csl-asset-data-cmms` 3.5) | Re-import of the mechanical set |

## 3. Convention in force by date (what a file's Control sheet should say)

| File issued between | Convention to state on the Control sheet |
|---|---|
| Before 08/24/26 | Pre-ruling census; codes absent or legacy |
| 08/24/26 to 09/09/26 | Functional Code Structure v1.1 with the 08/24/26 format rulings; six levels |
| 09/10/26 to 09/21/26 | 08/24/26 format rulings; depth "extended past six" per the 09/10/26 record; no versioned spec |
| 09/22/26 to 09/28/26 | 08/24/26 format rulings; depth eight stated verbally 09/22/26, unconfirmed; OPEN |
| 09/29/26 onward | 08/24/26 format rulings; depth "up to seven" stated 09/29/26, no versioned spec; OPEN |

Rule: build to the last written convention; state any later verbal or unspecified ruling on the Control sheet as an open item; never recode an issued set to a verbal ruling.

## 4. Open items

| # | Item | Options on the table | Opened | Blocks | Owner | Status |
|---|---|---|---|---|---|---|
| 1 | Structure depth (versioned spec) | Six / seven / eight levels | 09/10/26 (first departure from six) | QR prints; every code set beyond mechanical; Loops PML finalization before 10/30/26 | Client data owner | OPEN; gate G-13 |
| 2 | Child pump token | PUM (08/24/26 example) / PMP (legacy CHAMPS form seen in CHW01_PMP05) / CWP (condenser-water pumps under HEX) | 08/24/26 | Final child codes; PM records for pumps | Client data owner | OPEN |
| 3 | FAN as a level-2 code | Fan as its own unit family versus fan-family child tokens under the served unit | 08/26/26 | Fan population coding; smoke exhaust SE05–10 | Client data owner | OPEN |
| 4 | Instance padding | 2-digit (`PUM01`) versus 3/4-digit | 08/24/26 | Format validation rule; label width | Client data owner | OPEN |
| 5 | Placeholder code path | BFP01 versus DCW_BFP01 NEW-Placeholder in CHAMPS | Surfaced with the 08/27/26 New Asset Form batch | Watts LF009 RPZ record; merge | Client data owner | OPEN |
| 6 | Tag collision | TCWP-1 at W59: TCWP01 / TCWP02 provisional | Surfaced in the 08/2026 reconciliation | QR prints at W59 | Client data owner; FM PM | OPEN |

## 5. Code examples by record type (08/24/26 convention)

| Record type | Example | Note |
|---|---|---|
| Unit | `ASML_WLT_077_AHU22N` | Reset point; no system token |
| Child pump | `ASML_WLT_077_AHU22N_PUM01` | Token per open item 2 |
| Child sensor | `ASML_WLT_077_AHU22N_sensor01` | Casing as ruled 08/24/26; confirm before validation regex is tightened |
| Fan-family child | `ASML_WLT_077_AHU22N_RDF01` | RDF redundant; EXF exhaust; SEF smoke exhaust (instance illustrative) |
| Parent added to close a dangling child | `ASML_WLT_077_HEX03`, `ASML_WLT_077_CDP03` | v_5, 08/26/26 |
| Backflow preventer | `ASML_WLT_077_BFP01` | Watts LF009 RPZ; placeholder conflict per open item 5 |
| Loop parent (proposed) | `ASML_WLT_077_CHWMAIN` … `PCWWFL` | MainAsset_Parent records; Loops PML 09/23/26 |

## 6. Superseded forms (do not use; recognize on sight)

| Form | Where it appears | Superseded by |
|---|---|---|
| Legacy numeric grouping codes | CHAMPS extract | Dropped 08/24/26 |
| Building letter in the prefix | Pre-08/24/26 drafts | `ASML_WLT_077_` with no letter |
| Loop token inside the code or as a parent prefix | Pre-08/24/26 drafts; the GFC-001 SOP draft's definitions | Loop as a column |
| Structure taught by draft `W77-SOP-GFC-001 Rev 0` (Save-As from PCW-040) | The draft under review | 08/24/26 rulings; finding logged in CSL-W77-MEM-260919 |

---

Maintenance: add a ledger row the day a ruling is made; move an item from Section 4 to Section 2 when it is ruled in writing; never delete a row (the ledger is the record of what each delivered file was built to).
