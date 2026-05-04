#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path.cwd()

def find_file(*parts):
    for p in [ROOT / "ecomstore" / Path(*parts), ROOT / Path(*parts)]:
        if p.exists():
            return p
    return None

stripe_js = find_file("templates", "tags", "stripeJS.html")
if not stripe_js:
    print("ERROR: Cannot find templates/tags/stripeJS.html")
    sys.exit(1)

original = stripe_js.read_text()
backup = stripe_js.with_suffix(stripe_js.suffix + ".bak_mobile_alert_errors")
backup.write_text(original)

text = original

# Add helper functions if missing.
if "function aaIsMobileCheckout" not in text:
    insert_after = 'function clearStripePaymentError() {'
    helper = r'''
function aaIsMobileCheckout() {
    return !!(
        document.getElementById("mobile-credit-card-payment") ||
        document.querySelector("[data-role='page']") ||
        /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
    );
}

function aaShowStripeFailure(message) {
    var friendly = message || "Your payment could not be completed. Please check your card details and try again.";

    // Always try the existing inline error first.
    if (typeof showStripePaymentError === "function") {
        showStripePaymentError(friendly);
    }

    // Mobile jQuery pages sometimes fail to visibly repaint the inline error area.
    // A native alert is the safest customer-facing fallback.
    if (aaIsMobileCheckout()) {
        setTimeout(function () {
            alert(friendly);
        }, 50);
    }
}

'''
    # Put helper before clearStripePaymentError if possible, otherwise after script tag.
    if insert_after in text:
        text = text.replace(insert_after, helper + "\n" + insert_after, 1)
    else:
        text = text.replace('<script type="text/javascript">', '<script type="text/javascript">\n' + helper, 1)

# Replace the result.error branch to call aaShowStripeFailure.
# This targets both older and newer branch variants.
patterns = [
    r'''if \(result\.error\) \{\s*
\s*var stripeErrorMessage = result\.error\.message \|\| "Your payment could not be completed\. Please check your card details and try again\.";\s*
\s*showStripePaymentError\(stripeErrorMessage\);\s*
\s*changeLoadingState\(false\);\s*
\s*setStripeSubmitEnabled\(true\);\s*
\s*return false;\s*
\s*\} else \{''',
    r'''if \(result\.error\) \{\s*
\s*showStripePaymentError\(result\.error\.message\);\s*
\s*setStripeSubmitEnabled\(true\);\s*
\s*return;\s*
\s*\} else \{'''
]

replacement = '''if (result.error) {
                 var stripeErrorMessage = result.error.message || "Your payment could not be completed. Please check your card details and try again.";
                 aaShowStripeFailure(stripeErrorMessage);
                 changeLoadingState(false);
                 setStripeSubmitEnabled(true);
                 return false;
             } else {'''

replaced = False
for pat in patterns:
    new_text, count = re.subn(pat, replacement, text, count=1, flags=re.MULTILINE)
    if count:
        text = new_text
        replaced = True
        break

if not replaced:
    # More generic fallback: inject at the beginning of the first result.error block.
    new_text, count = re.subn(
        r'if \(result\.error\) \{',
        '''if (result.error) {
                 var stripeErrorMessage = result.error.message || "Your payment could not be completed. Please check your card details and try again.";
                 aaShowStripeFailure(stripeErrorMessage);
                 changeLoadingState(false);
                 setStripeSubmitEnabled(true);
                 return false;
             } else if (false) {''',
        text,
        count=1
    )
    text = new_text
    if not count:
        print("WARNING: Could not find result.error block. Please inspect confirmCardPayment manually.")

stripe_js.write_text(text)

print("Updated:", stripe_js)
print("Backup:", backup)
print()
print("Next:")
print("  python manage.py check")
print("  git diff", stripe_js)
print()
print("Test mobile with an invalid CVC/expiration. You should see a native alert with Stripe's error message.")
