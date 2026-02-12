# Random Email Generator

A Python library for generating realistic, human-like email addresses from names and surnames. The generator applies various transformations and patterns to create diverse email variations that appear natural and authentic.

Please, note: this is actually code from a spaghetti coded script of mine that I fastly wrote in an afternoon for another
side project. But since it's actually really useful, I decided to make a minimal refactoring for functional usage.

Needs big optimizations, statistical analysis and further refactor but right now it serves its purpose.

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

## Features

- **Human-like Output**: Generates authentic emails rather than bot-generated
- **Multiple Transformations**: Applies various mutations including leetspeak, vowel dropping, random separators, and digit insertion
- **Configurable Settings**: Customizable generation parameters through settings, though I recommend leaving as they are

## Usage

```python
from src.generate_rd_email import generate_email

# Generate a single email
email = generate_email("john", "doe")
print(email)  # Example: john.doe92@gmail.com
```

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
