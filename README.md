# Random Email Generator

A Python library for generating realistic, human-like email addresses from names and surnames. The generator applies various transformations and patterns to create diverse email variations that appear natural and authentic.

Please, note: this is actually code from a spaghetti coded script of mine that I fastly wrote in an afternoon for another
side project. But since it's actually really curious and useful, I decided to make a minimal refactoring so that
other people can benefit from it. Yes, it has some spaghetti coded architecture and optimizations necessary, but I
leave that to every developer's needs. Right now it works quite good and that's what matters.

## Examples

**Sample output for "John Doe" (50 generated emails. This classification was done afterwards, the code won't discriminate on those!):**

| Classic Format | Abbreviated | Numeric Variations | Creative Mutations |
|----------------|-------------|-------------------|-------------------|
| john.doe1920@gmail.com | j.dd1952@icloud.com | 2johndoe@gmail.com | johnbb_do@yahoo.com |
| john.doe2011@gmail.com | j.doe2011@gmail.com | 4john.doe@icloud.com | jhn_done1906@gmail.com |
| john.doe3@gmail.com | j.do1958@gmail.com | 6jj_d213@icloud.com | joohn_doe31@gmail.com |
| john.doe34@icloud.com | j_doo1967@icloud.com | 8john.dovve@gmail.com | jjo_doe335@icloud.com |
| johndoe1901@gmail.com | j_dd1963@icloud.com | 8j.doeaa@icloud.com | john.d4e@gmail.com |
| johndoe2019@gmail.com | jo.doe1980@gmail.com | 9jh0ndoe@outlook.com | johnxx_doe1945@gmail.com |
| john_d2013@yahoo.com | jo.doee67@gmail.com | 3johndoe@gmail.com | john.ddoe@gmail.com |
| john_d65@gmail.com | jdoe2002@icloud.com | 77johndo@gmail.com | johnn_doe2@yahoo.com |
| john.dd1932@gmail.com | jj-do1954@gmail.com | 7john.vvd@gmail.com | john_doee@icloud.com |
| john.do780@icloud.com | jjohn.d65@gmail.com | | jhn_do290@icloud.com |

### Pattern Analysis
- **Separators**: `.`, `_`, `-` (no separator)
- **Abbreviations**: Single letters, truncated names
- **Numeric additions**: Years, random digits, prefixes/suffixes  
- **Mutations**: Letter substitution (`o→0`), duplication (`bb`, `xx`), vowel dropping
- **Domains**: gmail.com, icloud.com, yahoo.com, outlook.com

## Features

- **Human-like Output**: Generates emails that feel authentic rather than bot-generated
- **Multiple Transformations**: Applies various mutations including leetspeak, vowel dropping, random separators, and digit insertion
- **Configurable Settings**: Customizable generation parameters through settings
- **Collision Analysis**: Built-in testing framework to analyze duplicate rates

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd random_email_gen

# Install dependencies
uv sync
```

## Usage

```python
from src.generate_rd_email import generate_email

# Generate a single email
email = generate_email("john", "doe")
print(email)  # Example: john.doe92@gmail.com
```

## Statistical Analysis

### Duplicate Rate Testing

Comprehensive testing was conducted to analyze the generator's collision rates across different scales:

| Sample Size | Runs | Duplicate Rate | Estimated Unique Space |
|-------------|------|----------------|------------------------|
| 100         | 10   | 0.5%          | ~1.0×10⁴               |
| 1,000       | 10   | 3.32%         | ~1.5×10⁴               |
| 10,000      | 10   | 9.6%          | ~4.9×10⁴               |
| 100,000     | 10   | 11.6%         | ~4.0×10⁵               |
| 1,000,000   | 10   | 8.45%         | ~5.6×10⁶               |

### Key Findings

#### 1. Non-Uniform Distribution
The generator exhibits structured, template-based behavior rather than purely random generation. The effective unique space (S) grows with sample size (k), indicating:
- Multiple generation templates with varying probabilities
- Deterministic suffix rules and character set limitations
- Scale-dependent collision-avoidance mechanisms

#### 2. Scale-Dependent Behavior

**Small Scale (100-1,000 emails):**
- Very low collision rates (0.5-3.32%)
- Large apparent unique space
- Template diversity dominates

**Medium Scale (10,000-100,000 emails):**
- Higher collision rates (9.6-11.6%)
- Template limitations become apparent
- Combinatorial constraints emerge

**Large Scale (1,000,000 emails):**
- Stabilized collision rate (~8.45%)
- Systematic generation strategy evident
- Numeric suffix cycling dominates

#### 3. Design Trade-offs

The constrained generation space is **intentional** and represents a deliberate design choice:

✅ **Advantages:**
- Every generated email appears authentically human
- Avoids bot-like patterns
- Maintains realistic email formatting conventions

⚠️ **Limitations:**
- Finite unique space (~10⁴-10⁶ combinations per name pair)
- Higher collision rates at scale
- Not suitable for applications requiring unlimited unique addresses

## Technical Architecture

### Core Components

- **`generate_rd_email.py`**: Main email generation engine
- **`random_choices.py`**: Transformation and mutation functions
- **`settings.py`**: Configuration parameters
- **`testing.py`**: Performance testing utilities

### Generation Pipeline

1. **Name Processing**: Normalize and prepare input names
2. **Separator Selection**: Choose joining characters (., _, etc.)
3. **Mutation Application**: Apply random transformations:
   - Leetspeak conversion (e → 3, a → 4)
   - Vowel dropping
   - Random symbol insertion
   - Digit/s prepending/appending
   - Letter duplication
4. **Domain Assignment**: Select from realistic domain pool with determined probability weights
5. **Validation**: Ensure output meets heuristic standards

## Conclusion

This generator prioritizes **quality over quantity**, producing emails that consistently pass the "human test" while acknowledging the inherent trade-off with uniqueness at scale. The structured approach ensures reliable, realistic output suitable for testing, demos, and applications where authentic-looking email addresses are more valuable than unlimited uniqueness.
